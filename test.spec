%define		plugin configmanager
Summary:	testing something
Name:		builder
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
Source0:	https://swfupload.googlecode.com/files/SWFUpload%20v%{version}%20Core.zip
# Source0-md5:	1bf14f5a7a9a3ecc529378ee50f0c59b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testing something

%prep
%setup -qcT

%install
install -d $RPM_BUILD_ROOT
install a $RPM_BUILD_ROOT

%clean

%files
%defattr(644,root,root,755)
/a
