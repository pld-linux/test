Summary:	University of Cambridge Mail Transfer Agent
Name:		deptest
Version:	4.69
Release:	3
Epoch:		2
License:	GPL
Group:		Networking/Daemons
Requires:	%%{runtimedep}
Conflicts:	%%{runtimeconflict}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Smail like Mail Transfer Agent with single configuration file.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/test
install -d $RPM_BUILD_ROOT/test/aa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/test
