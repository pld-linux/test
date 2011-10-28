%include	/usr/lib/rpm/macros.perl
Summary:	testing something
Name:		builder-md5patch
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
# http://forums.cacti.net/download.php?id=10980
Source1:	sharednetworkclass0.40.zip
# Source1-md5:	b438751d7b696a10a8958ea6e0f407f3
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
