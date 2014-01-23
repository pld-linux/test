# skeleton for rpm testing.
# create your own test in separate branch, keep master branch clean
# git checkout -b somebranch
# git push origin -u somebranch
Summary:	testing something
Name:		test
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:    df-test.tar
# Source0-md5:   688587187200aae69f9a63c4496843ca
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
