Summary:	test
Name:		luatest
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/System
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_shell			/bin/posh

%description
This package should be never installed.

%prep
%setup -qcT

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%post	-p %add_etc_shells -p /bin/posh
%preun	-p %remove_etc_shells -p /bin/posh

%files
%defattr(644,root,root,755)
