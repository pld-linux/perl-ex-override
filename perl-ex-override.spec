#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ex
%define	pnam	override
Summary:	ex::override - Perl pragma to override core functions
Summary(pl.UTF-8):   ex::override - możliwość przeciążania głównych funkcji Perla
Name:		perl-ex-override
Version:	1.1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1247bd4ec9dae4cb2f250fd5af990668
URL:		http://search.cpan.org/dist/ex-override/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"ex::override" is an easy way to override core Perl functions:

  use ex::override
    length => \&mylength,
    open   => \&myopen;

Overriding a core function happens at compile time. Arguments are
passed to "ex::override" in a name based, or hash style. The key is
the name of the core function to override, the value is your
subroutine to replace the core's.

%description -l pl.UTF-8
"ex::override" to prosty sposób przeciążania głównych funkcji Perla:

  use ex::override
    length => \&mylength,
    open   => \&myopen;

Przeciążanie głównej funkcji następuje w czasie kompilacji. Argumenty
są przekazywane do "ex::override" w oparciu o nazwy lub w stylu
tablicy asocjacyjnej. Kluczem jest nazwa głównej funkcji do
przeciążenia, a wartością własna procedura mająca zastąpić perlową.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes
%{perl_vendorlib}/ex/*.pm
%{_mandir}/man3/*
