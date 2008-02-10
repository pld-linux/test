Summary:	testing
Name:		devtest
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications/System
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package should be never installed.

%prep
%setup -qcT

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/dev
touch $RPM_BUILD_ROOT/dev/testfile

%files
%defattr(644,root,root,755)
/dev/testfile
