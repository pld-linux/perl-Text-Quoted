#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Quoted
Summary:	Text::Quoted - extract the structure of a quoted mail message
Summary(pl):	Text::Quoted - wydzielenie struktury cytowanej wiadomo¶ci pocztowej
Name:		perl-Text-Quoted
Version:	1.5
Release:	1
# Artistic (README says: same as perl)
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	24f2eda17ae8f39084005051f0c2545a
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Text-Autoformat
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Quoted Perl module examines the structure of some text which may
contain multiple different levels of quoting, and turns the text into
a nested data structure.

%description -l pl
Modu³ Perla Text::Quoted analizuje strukturê pewnego tekstu, który
mo¿e zawieraæ wiele ró¿nych poziomów cytowania i przekszta³ca tekst w
zagnie¿d¿on± strukturê danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
find -type f | xargs %{__perl} -pi -e 's,/usr/local,/usr,g'
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install\
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
