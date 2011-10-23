Summary:	fetch files from fedora distfiles
Name:		test
Version:	2.1.7
Release:	0.10
License:	GPL
Group:		Applications/System
# http://pkgs.fedoraproject.org/repo/pkgs/<PACKAGE>
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/pdf-renderer/pdf-renderer-128svn-20110310.tar.bz2/f46cdc9f014e3ec9d47704e46b249209/pdf-renderer-128svn-20110310.tar.bz2
# Source0-md5:	f46cdc9f014e3ec9d47704e46b249209
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
