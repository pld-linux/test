Summary:	University of Cambridge Mail Transfer Agent
Name:		deptest
Version:	4.69
Release:	3
Epoch:		2
License:	GPL
Group:		Networking/Daemons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Smail like Mail Transfer Agent with single configuration file.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_emacs_lispdir}/{%{name}-mode,site-start.d}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/test
