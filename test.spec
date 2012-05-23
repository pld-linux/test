Summary:	fetch files from fedora distfiles
Name:		test
Version:	2.1.7
Release:	0.10
License:	GPL
Group:		Applications/System
# http://pkgs.fedoraproject.org/repo/pkgs/<PACKAGE>
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/libclastfm/libclastfm-20120314git968af0ab.tar.bz2/2e17a7981e2f16b9533994e543ed318a/libclastfm-20120314git968af0ab.tar.bz2
# Source0-md5:	2e17a7981e2f16b9533994e543ed318a
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
