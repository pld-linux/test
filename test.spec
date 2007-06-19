%include	/usr/lib/rpm/macros.java
Summary:	test package to run COMMAND like commands on builder :/
Name:		test
Version:	8.57
Release:	0.10
License:	GPL
Group:		Applications/System
Requires:	uname(release) >= 2.6.12
Suggests:	uname(release) >= 2.6.12
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
this package should be never installed.

%prep
%setup -qcT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
