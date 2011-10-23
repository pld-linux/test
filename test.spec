Summary:	fetch files from fedora distfiles
Name:		test
Version:	2.1.7
Release:	0.10
License:	GPL
Group:		Applications/System
# http://pkgs.fedoraproject.org/repo/pkgs/<PACKAGE>
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/bouncycastle-mail/bcmail-jdk16-146-FEDORA.tar.gz/d7b27678d5fdebaf79a19ef34ae9d9b3/bcmail-jdk16-146-FEDORA.tar.gz
# Source0-md5:	d7b27678d5fdebaf79a19ef34ae9d9b3
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
