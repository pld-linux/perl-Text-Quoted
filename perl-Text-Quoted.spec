#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Quoted
Summary:	Text::Quoted - extract the structure of a quoted mail message
Summary(pl.UTF-8):   Text::Quoted - wydzielenie struktury cytowanej wiadomości pocztowej
Name:		perl-Text-Quoted
Version:	1.8
Release:	2
# Artistic (README says: same as perl)
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cab9d462b480437bab72b6044ac6c788
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
Moduł Perla Text::Quoted analizuje strukturę pewnego tekstu, który
może zawierać wiele różnych poziomów cytowania i przekształca tekst w
zagnieżdżoną strukturę danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
rm Makefile pm_to_blib

%build
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
