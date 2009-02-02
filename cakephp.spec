Summary:	OpenSource Rapid Development PHP Framework
Name:		cakephp
Version:	1.2.1.8004
Release:	0.1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://cakeforge.org/frs/download.php/697/cake_%{version}.tar.bz2/donation=%{name}-%{version}.tar.bz2
# Source0-md5:	0d01d1bc4e2df9ccf82130a838b06dd6
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

%prep
%setup -q -n cake_%{version}

mv cake/{LICENSE,VERSION}.txt .
find -name empty | xargs rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a app cake vendors $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_appdir}
