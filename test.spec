Summary:	webapp test
Name:		test
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications/System
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	webapps
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}

%description
zz

%prep
%setup -qcT
touch lighttpd.conf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}
cp -p lighttpd.conf $RPM_BUILD_ROOT%{_sysconfdir}/lighttpd.conf

%triggerin -- lighttpd
set -x
echo triggerin:%{N}-%{V}-%{R}
%webapp_register lighttpd %{_webapp}

%triggerun -- lighttpd
set -x
echo triggerun:%{N}-%{V}-%{R}
%webapp_unregister lighttpd %{_webapp}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lighttpd.conf
