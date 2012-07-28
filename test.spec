Summary:	fetch files from fedora distfiles
Name:		test
Version:	1
Release:	0.10
License:	GPL
Group:		Applications/System
# http://pkgs.fedoraproject.org/repo/pkgs/<PACKAGE>
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/dwz/dwz-0.6.tar.bz2/e72adeacdae79647f34f139f7957bcb1/dwz-0.6.tar.bz2
# Source0-md5:	e72adeacdae79647f34f139f7957bcb1
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
