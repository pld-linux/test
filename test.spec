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
Source0:	test.c
# Source0-md5:	144269a4ffe67704e0b71fb8d91fabe9
URL:		http://www.pld-linux.org/
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testing something.

%prep
%setup -qcT

%{__cc} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 %{SOURCE0} -o test
strace ./test
test $(sha256sum file-normal|cut -f1 -d' ') = $(sha256sum file-direct-io|cut -f1 -d' ')

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
touch $RPM_BUILD_ROOT/a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/a
