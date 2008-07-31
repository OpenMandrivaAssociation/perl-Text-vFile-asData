%define realname   Text-vFile-asData

Name:		perl-%{realname}
Version:    0.05
Release:    %mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Parse vFile formatted files into data structures
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-vFile-asData-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires: perl(Class::Accessor::Chained)

BuildArch: noarch

%description
Text::vFile::asData - parse vFile formatted files into data structures

%prep
%setup -q -n Text-vFile-asData-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Text/*
%{_mandir}/man3/*
