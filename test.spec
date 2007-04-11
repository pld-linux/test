Summary:	Fetch opera packages to distfiles
Name:		operafetch
Version:	9.20
Release:	1
License:	GPL
Group:		Networking/Hacking
Source0:	ftp://ftp.opera.com/pub/opera/linux/920/final/en/sparc/static/opera-9.20-20070409.1-static-qt.sparc-en.tar.bz2
# Source0-md5:	43c9cc58c26979db270f05141ee7cc99
Source1:	ftp://ftp.opera.com/pub/opera/linux/920/final/en/i386/shared/opera-9.20-20070409.5-shared-qt.i386-en.tar.bz2
# Source1-md5:	9446ed1e968d511f43c1681eee44ab7a
Source2:	ftp://ftp.opera.com/pub/opera/linux/920/final/en/ppc/shared/gcc-2.95/opera-9.20-20070409.3-shared-qt.ppc-en.tar.bz2
# Source2-md5:	70ea569449bdee0c3a62f55b45a7f37b
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
