%define upstream_name    Text-vFile-asData
%define upstream_version 0.08
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.08
Release:	2

Summary:	Parse vFile formatted files into data structures
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Text/Text-vFile-asData-0.08.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor::Chained)

BuildArch:	noarch

%description
Text::vFile::asData - parse vFile formatted files into data structures

%prep
%setup -q -n Text-vFile-asData-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{perl_vendorlib}/Text/*
%{_mandir}/man3/*


%changelog
* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 573809
- update to 0.07

* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 572238
- update to 0.06

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 406192
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.05-4mdv2009.0
+ Revision: 258623
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.05-3mdv2009.0
+ Revision: 246642
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.05-1mdv2008.1
+ Revision: 136362
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 23 2007 Michael Scherer <misc@mandriva.org> 0.05-1mdv2008.0
+ Revision: 29944
- Import perl-Text-vFile-asData



* Wed May 23 2007 Michael Scherer <misc@mandriva.org> 0.05-1mdv2008.0
- First Mandriva package

