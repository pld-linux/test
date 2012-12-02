%define		ver		7.3
%define		patchlevel	7
Summary:	Distfiles Fetcher
Name:		distfiles
Version:	%{ver}.%{patchlevel}
Release:	0.1
License:	GPL
Group:		Networking/Hacking
#Source0:	ftp://ftp.vim.org/pub/editors/vim/patches/7.3/7.3.738
%patchset_source -f ftp://ftp.vim.org/pub/editors/vim/patches/%{ver}/%{ver}.%03g 1 %{patchlevel}
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
