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
Summary: subpackage

%description sub
Subpackage

%package sub2
Summary: subpackage

%description sub2
Subpackage

%define var1 foo
%define var2 %{var1}
%define var1 bar

%prep
%setup -qcT
echo %{var1} %{var2}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/dir
touch $RPM_BUILD_ROOT/dir/file
touch $RPM_BUILD_ROOT/dir/file2
cd $RPM_BUILD_ROOT/dir

%preun sub
echo "sub script"

%preun sub2
echo "sub2 script"

%clean

%files
%defattr(644,root,root,755)
%dir /dir

%files sub
%defattr(644,root,root,755)
/dir/file

%files sub2
%defattr(644,root,root,755)
/dir/file2

