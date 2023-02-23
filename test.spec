# skeleton for rpm testing.
# create your own test in separate branch, keep master branch clean
#
# git checkout -b test/feature
# git push origin -u test/feature
Summary:	testing something
Name:		test
Version:	1
Release:	7
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testing something.

%prep
%setup -qcT

%build
env | sort

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

env | sort

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
