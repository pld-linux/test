# skeleton for rpm testing.
# create your own test in separate branch, keep master branch clean
# git checkout -b somebranch
# git push origin -u somebranch
Summary:	testing something
Name:		test
Version:	1
Release:	1
License:	GPL
Group:		Applications/System
Source0:    test.tgz
# Source0-md5:   a23576184c7a93c5f02401aca9907dbd
URL:		http://www.pld-linux.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testing something

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean

%files
%defattr(644,root,root,755)
