Summary:	Distfiles Fetcher
Name:		distfiles
Version:	1.9
Release:	1
License:	GPL
Group:		Networking/Hacking
Source0:	Locale-Maketext-1.17.tar.gz
# Source0-md5:	0e5b8a5973a75a329b8cdb5e60f6f588
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
