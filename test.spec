%define		plugin configmanager
Summary:	testing something else
Name:		builder
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
#Source0:	jdk-6u39-linux-i586.bin
## Source0-md5:	40f5f4511a9c6ed4bcac687787066db1
Source1:	syslog-ng-ose-v3.3-guide-admin-en.pdf
# Source1-md5:	c5fb4bd364a10dced391dbf63350b115
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testing something

%prep
%setup -qcT

%install
install -d $RPM_BUILD_ROOT
install a $RPM_BUILD_ROOT
ln -s /not-existing-crap $RPM_BUILD_ROOT/test

%clean

%files
%defattr(644,root,root,755)
/*
