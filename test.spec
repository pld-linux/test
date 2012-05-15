Summary:	fetch files from fedora distfiles
Name:		test
Version:	2.1.7
Release:	0.10
License:	GPL
Group:		Applications/System
# http://pkgs.fedoraproject.org/repo/pkgs/<PACKAGE>
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/aqute-bnd/bnd-0.0.363.jar/1d36d0271381964304c08b00b5fd1b4a/bnd-0.0.363.jar
# Source0-md5:	1d36d0271381964304c08b00b5fd1b4a
Source1:	http://pkgs.fedoraproject.org/repo/pkgs/aqute-bnd/aqute-service.tar.gz/11fe2398149f85066f6d0b6dc8af225b/aqute-service.tar.gz
# Source1-md5:	11fe2398149f85066f6d0b6dc8af225b
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
