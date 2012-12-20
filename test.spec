%define		plugin configmanager
Summary:	testing something else
Name:		builder
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
Source0:	jdk-6u38-linux-i586.bin
# Source0-md5:	5bae3dc304d32a7e3c50240eab154e24
Source1:	jdk-6u38-linux-x64.bin
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
