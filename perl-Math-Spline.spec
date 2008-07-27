#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Spline
Summary:	Math::Spline - Cubic Spline Interpolation of data
Summary(pl.UTF-8):	Math::Spline - interpolacja danych splajnami kubicznymi
Name:		perl-Math-Spline
Version:	0.01
Release:	13
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a9ebe29ba1794d1dca60aa0c44178197
Patch0:		%{name}-man.patch
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Math-Derivative
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides cubic spline interpolation of numeric data. The
data is passed as references to two arrays containing the x and y
ordinates. It may be used as an exporter of the numerical functions
or, more easily as a class module.

%description -l pl.UTF-8
Ten pakiet udostępnia interpolację danych numerycznych przy pomocy
splajnów kubicznych. Dane są przekazywane jako referencje do dwóch
tablic zawierających współrzędne x i y. Moduł może być używany do
eksportowania funkcji numerycznych albo, łatwiej, jako klasa.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/Spline.pm
%{_mandir}/man3/*
