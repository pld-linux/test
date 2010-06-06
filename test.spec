Summary:	Distfiles Fetcher
Name:		distfiles
Version:	1.9
Release:	1
License:	GPL
Group:		Networking/Hacking
Source0:	http://sunsite.icm.edu.pl/pub/CPAN/modules/by-module/POE/POE-Component-Server-Syslog-1.18.tar.gz
# Source0-md5:	6f2738b00dc954cf0e1575f315398593
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
