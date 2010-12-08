Summary:	Distfiles Fetcher
Name:		distfiles
Version:	1.9
Release:	1
License:	GPL
Group:		Networking/Hacking
Source0:	http://glen.alkohol.ee/pld/selinux-bcond.patch
# Source0-md5:	6b4672efdbd08f4bb70ea379e56bbd17
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
