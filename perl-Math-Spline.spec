%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Spline
Summary:	Math::Spline - Cubic Spline Interpolation of data
Summary(pl):	Math::Spline - interpolacja danych splajnami kubicznymi
Name:		perl-Math-Spline
Version:	0.01
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-man.patch
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Math-Derivative
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides cubic spline interpolation of numeric data. The
data is passed as references to two arrays containing the x and y
ordinates. It may be used as an exporter of the numerical functions
or, more easily as a class module.

%description -l pl
Ten pakiet udostêpnia interpolacjê danych numerycznych przy pomocy
splajnów kubicznych. Dane s± przekazywane jako referencje do dwóch
tablic zawieraj±cych wspó³rzêdne x i y. Modu³ mo¿e byæ u¿ywany do
eksportowania funkcji numerycznych albo, ³atwiej, jako klasa.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Math/Spline.pm
%{_mandir}/man3/*
