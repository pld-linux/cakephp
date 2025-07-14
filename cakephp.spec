# TODO
# - SimpleTest dependency for -tests: http://simpletest.org/en/download.html
Summary:	OpenSource Rapid Development PHP Framework
Name:		cakephp
Version:	1.2.1.8004
Release:	0.5
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://cakeforge.org/frs/download.php/697/cake_%{version}.tar.bz2/donation=%{name}-%{version}.tar.bz2
# Source0-md5:	0d01d1bc4e2df9ccf82130a838b06dd6
Patch0:		console.patch
Patch1:		config.patch
URL:		http://www.cakephp.org/
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{php_data_dir}/cake

%description
CakePHP is a rapid development framework for PHP that provides an
extensible architecture for developing, maintaining, and deploying
applications. Using commonly known design patterns like MVC and ORM
within the convention over configuration paradigm, CakePHP reduces
development costs and helps developers write less code.

%package console
Summary:	Cake Command-line code generation utility
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description console
Cake Command-line code generation utility to automate programmer
chores.

%package tests
Summary:	Tests for CakePHP
Summary(pl.UTF-8):	Testy dla CakePHP
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for CakePHP.

%description tests -l pl.UTF-8
Testy dla CakePHP.

%package demo
Summary:	Demo for CakePHP
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu CakePHP
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for CakePHP.

%description demo -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu CakePHP.

%prep
%setup -q -n cake_%{version}
%patch -P0 -p1
%patch -P1 -p1

mv cake/{LICENSE,VERSION}.txt .
rm cake/console/cake.bat
mv cake/console/cake cake.sh
find -name empty | xargs rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_bindir},%{_examplesdir}/%{name}-%{version}}
cp -a cake/* $RPM_BUILD_ROOT%{_appdir}
cp -a app vendors $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -p cake.sh $RPM_BUILD_ROOT%{_bindir}/cake

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_appdir}
%exclude %{_appdir}/tests
%exclude %{_appdir}/console

%files console
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cake
%{_appdir}/console

%files tests
%defattr(644,root,root,755)
%{_appdir}/tests

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
