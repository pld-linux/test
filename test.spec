%define		plugin configmanager
Summary:	testing something else
Name:		builder
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
Source0:	jdk-6u43-linux-i586.bin
# Source0-md5:	42ba71917ecf17d216c3980bbc732479
Source1:	jdk-6u43-linux-x64.bin
# Source1-md5:	931b2e22c7006dae5554a9c1a620d8f8
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
