%define		plugin configmanager
Summary:	testing something else
Name:		builder
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
Source0:	jdk-7u21-linux-i586.tar.gz
# Source0-md5:	fc0241e1a3e243602698ac700abc94e9
Source1:	jdk-7u21-linux-x64.tar.gz
# Source1-md5:	3ceef66377b6d87144b802960f5e715b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testing git

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
