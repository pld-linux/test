%bcond_with	i18n
%define		_urlprefix	http://ep09.pld-linux.org/~arekm/kde/
%define		artsver	1.5.5
%define		kdevelopver 3.3.4
Summary:	Fetch KDE packages to distfiles
Name:		kdefetch
Version:	3.5.5
Release:	1
License:	GPL
Group:		Networking/Hacking
Source0:	http://www.sk.ee/files/ESTEID-SK%202007.PEM.cer
# Source0-md5:	2b1a2a77f565d68fdf5f19f6cc3a5600
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alien allows you to convert Debian, Stampede and Slackware Packages
into PLD packages, which can be installed with rpm. It can also
convert into Slackware, Debian, and Stampede packages. This is a tool
only suitable for binary packages.

%prep
exit 1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
