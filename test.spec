%define		plugin configmanager
Summary:	testing something else
Name:		builder
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
Source0:	jdk-7u17-linux-i586.tar.gz
# Source0-md5:	694f9592d894b86a8a3cb56bf71768e6
Source1:	jdk-7u17-linux-x64.tar.gz
# Source1-md5:	d9b5870a94c47efa0282d6c1863d0667
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
