%define	module	Pod-Strip
%define	name	perl-%{module}
%define version 1.02
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Remove POD from Perl code 
Url:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/Pod/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
Buildrequires:	perl(Module::Build)
Buildrequires:	perl(Pod::Simple)
Requires:	    perl(Pod::Simple)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Pod::Strip is a subclass of Pod::Simple that strips all POD from Perl Code.

%prep
%setup -q -n %{module}-%{version}

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


