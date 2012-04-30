Summary:	fetch files from fedora distfiles
Name:		test
Version:	2.1.7
Release:	0.10
License:	GPL
Group:		Applications/System
# http://pkgs.fedoraproject.org/repo/pkgs/<PACKAGE>
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/linux-firmware/linux-firmware-20120418.tar.gz/7652141968b9c53af4d38317a85f88b8/linux-firmware-20120418.tar.gz
# Source0-md5:	7652141968b9c53af4d38317a85f88b8
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
