%define	pdir	Math
%define	pnam	Spline
%include	/usr/lib/rpm/macros.perl
Summary:	Math-Spline perl module
Summary(pl):	Modu³ perla Math-Spline
Name:		perl-Math-Spline
Version:	0.01
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-man.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Math-Derivative
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-Spline perl module.

%description -l pl
Modu³ perla Math-Spline.

%prep
%setup -q -n Math-Spline-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Math/Spline.pm
%{_mandir}/man3/*
