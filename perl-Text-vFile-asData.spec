%define upstream_name    Text-vFile-asData
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Parse vFile formatted files into data structures
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-vFile-asData-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor::Chained)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Text::vFile::asData - parse vFile formatted files into data structures

%prep
%setup -q -n Text-vFile-asData-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes META.yml
%{perl_vendorlib}/Text/*
%{_mandir}/man3/*
