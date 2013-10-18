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
URL:		http://www.pld-linux.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testing something

%package sub
Summary:	tes
Release:	2

%description sub
x

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/tmp

:>$RPM_BUILD_ROOT/tmp/xxx
:>$RPM_BUILD_ROOT/tmp/yyy

%clean

%files
%defattr(644,root,root,755)
/tmp/xxx

%files sub
%defattr(644,root,root,755)
/tmp/yyy
