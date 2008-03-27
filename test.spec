Summary:	University of Cambridge Mail Transfer Agent
Name:		exim
Version:	4.69
Release:	1
Epoch:		2
License:	GPL
Source0:	ftp://ftp.porcupine.org/mirrors/postfix-release/official/postfix-2.5.1.tar.gz
# Source0-md5:	95a559c509081fdd07d78eafd4f4c3b4
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

%triggerpostun -- exim  < 3.90
set -x
echo "triggerpostun %{name}-%{version}-%{release}"

%files
%defattr(644,root,root,755)
