Summary:	University of Cambridge Mail Transfer Agent
Name:		bug120
Version:	4.69
Release:	1.52
License:	GPL
Group:		Networking/Daemons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Smail like Mail Transfer Agent with single configuration file.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- %{name} < 3.90
set -x
echo "triggerpostun %{name}-%{version}-%{release}"

%files
%defattr(644,root,root,755)
