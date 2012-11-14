%define		plugin configmanager
Summary:	testing something else
Name:		builder
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
Source0:	jdk-6u34-linux-i586.bin
# Source0-md5:	60f304b5ecae14dab5ab0b0144b9c012
Source1:	jdk-6u34-linux-x64.bin
# Source1-md5:	96278470b5c981dfd3b9f3308e5057f9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testing something.

%prep
%setup -qcT

%install
install -d $RPM_BUILD_ROOT
install a $RPM_BUILD_ROOT

%clean

%files
%defattr(644,root,root,755)
/a
