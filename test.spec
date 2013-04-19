%define		plugin configmanager
Summary:	testing something else
Name:		builder
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
Source0:	jdk-6u45-linux-i586.bin
# Source0-md5:	3269370b7c34e6cbfed8785d3d0c5cbd
Source1:	jdk-6u45-linux-x64.bin
# Source1-md5:	40c1a87563c5c6a90a0ed6994615befe
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
