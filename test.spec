Summary:	fetch files from fedora distfiles
Name:		test
Version:	2.1.7
Release:	0.10
License:	GPL
Group:		Applications/System
# http://pkgs.fedoraproject.org/repo/pkgs/<PACKAGE>
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/mysql-connector-c++/mysql-connector-c++-bzr895.tgz/ef824818419b8fb0f1396e37ce040d7a/mysql-connector-c++-bzr895.tgz
# Source0-md5:	ef824818419b8fb0f1396e37ce040d7a
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rpm5.org distributes now in src.rpm format, but we need tar.gz

%prep
%setup -qcT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
