Summary:	Distfiles Fetcher
Name:		linux-firmware
Version:	20120720
Release:	1
License:	GPL
Group:		Networking/Hacking
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/linux-firmware/linux-firmware-20120720.tar.gz/a26f3e6042afccf12a4633050e1c8c0c/linux-firmware-20120720.tar.gz
# Source0-md5:	a26f3e6042afccf12a4633050e1c8c0c
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fake package to fool distfiles.

%prep
exit 1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
