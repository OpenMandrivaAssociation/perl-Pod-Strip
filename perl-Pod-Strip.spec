%define	upstream_name	 Pod-Strip
%define upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:	Remove POD from Perl code 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
Buildrequires:	perl(Module::Build)
Buildrequires:	perl(Pod::Simple)
Requires:	    perl(Pod::Simple)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Pod::Strip is a subclass of Pod::Simple that strips all POD from Perl Code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%check
./Build test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Pod
%{_mandir}/man3/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.0
+ Revision: 404296
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.02-7mdv2009.0
+ Revision: 258268
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.02-6mdv2009.0
+ Revision: 246320
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.02-4mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-4mdv2008.0
+ Revision: 90069
- rebuild


* Wed Nov 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-3mdv2007.0
+ Revision: 88326
- force requires on Pod::Simple

* Tue Nov 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-2mdv2007.1
+ Revision: 87874
- fix buildrequires
- Import perl-Pod-Strip

* Tue Nov 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2007.1
- first mdv release

