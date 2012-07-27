%define		plugin configmanager
Summary:	testing something else
Name:		builder
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
Source0:	http://forums.cacti.net/download/file.php?id=21891#/%{plugin}-%{version}.zip
# Source0-md5:	d3cdb035a4d47ff464916774dd953457
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
