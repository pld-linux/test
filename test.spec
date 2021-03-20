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
Source0:	http://execve.pl/u/u?r=23#/xxx
# Source0-md5:	6de9439834c9147569741d3c9c9fc010
URL:		http://www.pld-linux.org/
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testing something.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
touch $RPM_BUILD_ROOT/a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/ba
