Summary:	testing
Name:		test
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications/System
ExclusiveArch:	i686
BuildRequires:	a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package should be never installed.

%prep
%setup -qcT
exit 13

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%pretrans
exit 1

%files
%defattr(644,root,root,755)
