#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Spline
Summary:	Math::Spline - Cubic Spline Interpolation of data
Summary(pl):	Math::Spline - interpolacja danych splajnami kubicznymi
Name:		perl-Math-Spline
Version:	0.01
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a9ebe29ba1794d1dca60aa0c44178197
Patch0:		%{name}-man.patch
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Ten pakiet udost�pnia interpolacj� danych numerycznych przy pomocy
splajn�w kubicznych. Dane s� przekazywane jako referencje do dw�ch
tablic zawieraj�cych wsp�rz�dne x i y. Modu� mo�e by� u�ywany do
eksportowania funkcji numerycznych albo, �atwiej, jako klasa.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/Spline.pm
%{_mandir}/man3/*
