%define		prefix	http://carme.pld-linux.org/~glen/horde/
Summary:	Distfiles Fetcher
Name:		distfiles
Version:	1.9
Release:	1
License:	GPL
Group:		Networking/Hacking
Source0:	linux-2.6.38.tar.bz2
# Source0-md5:	7d471477bfa67546f902da62227fa976
Patch1:		patch-2.6.38.8.bz2
# Patch1-md5:	c0f416f6a2e916633f697287cc7cb914
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
