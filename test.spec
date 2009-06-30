%include	/usr/lib/rpm/macros.perl
Summary:	Pakages converter (tgz, rpm, deb, slp)
Summary(pl.UTF-8):	Konwerter pakietów (tgz, rpm, deb, slp)
Name:		alien
Version:	8.72
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://ftp.de.debian.org/debian/pool/main/a/alien/%{name}_%{version}.tar.gz
# Source0-md5:	7d789be2b9e0867c6551af65f37ab71a
URL:		http://kitenet.net/programs/alien/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	/usr/bin/rpm2cpio
Requires:	binutils
Requires:	cpio
Suggests:	/usr/bin/822-date
Suggests:	debhelper
BuildArch:	noarch
BuildConflicts:	lzo < 100:100
BuildConflicts:	blahblahsomething
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alien allows you to convert Debian, Stampede and Slackware Packages
into PLD packages, which can be installed with rpm. It can also
convert into Slackware, Debian, and Stampede packages. This is a tool
only suitable for binary packages.

%description -l pl.UTF-8
Alien pozwala przekonwertować pakiety Debiana, Stampede oraz Slackware
w pakiety używane w PLD, które mogą być zainstalowane przy użyciu
rpm-a i odwrotnie. Narzędzie to jest przydatne wyłącznie dla pakietów
binarnych.

%prep
%setup -q -c -T

%build

%install

%clean

%files
%defattr(644,root,root,755)
