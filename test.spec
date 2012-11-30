%define		prefix	http://carme.pld-linux.org/~glen/horde/
Summary:	Distfiles Fetcher
Name:		distfiles
Version:	7.3
Release:	0.1
License:	GPL
Group:		Networking/Hacking
Source0:	ftp://ftp.vim.org/pub/editors/vim/patches/7.3/7.3.738
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
