Summary:	package to satisfy poldek
Name:		satisfy
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications/System
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is out there to satisfy poldek verify for packages which are
present in ac-main but are obsoleted in ac-updates.

This package should be never installed.

%prep
%setup -q

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%pretrans
exit 1

%files
%defattr(644,root,root,755)
