%include	/usr/lib/rpm/macros.perl
Summary:	Pakages converter (tgz, rpm, deb, slp)
Name:		test
Version:	8.56
Release:	0.1
License:	GPL
Group:		Applications/System
BuildRequires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alien allows you to convert Debian, Stampede and Slackware Packages
into PLD packages, which can be installed with rpm. It can also
convert into Slackware, Debian, and Stampede packages. This is a tool
only suitable for binary packages.

%description -l pl
Alien pozwala przekonwertowa� pakiety Debiana, Stampede oraz Slackware
w pakiety u�ywane w PLD, kt�re mog� by� zainstalowane przy u�yciu
rpm-a i odwrotnie. Narz�dzie to jest przydatne wy��cznie dla pakiet�w
binarnych.

%prep
%setup -qcT
set +e

rpm -qf /usr/bin/pear
rpm -qf /usr/bin/php
rpm -qa 'php*'
ls -la /usr/share/pear
ls -la /usr/share/pear/.registry


exit 1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/no/files/installed
