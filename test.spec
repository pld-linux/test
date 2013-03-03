%define		plugin configmanager
Summary:	testing something else
Name:		builder
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
Source0:	jdk-7u15-linux-i586.tar.gz
# Source0-md5:	6ebab8e0942706af2f7f5e0195a96f2c
Source1:	jdk-7u15-linux-x64.tar.gz
# Source1-md5:	118a16aab9ff2c3f7c7788658cc77734
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
