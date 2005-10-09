%include	/usr/lib/rpm/macros.perl
Summary:	Pakages converter (tgz, rpm, deb, slp)
Summary(pl):	Konwerter pakietów (tgz, rpm, deb, slp)
Name:		alien
Version:	8.56
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://kitenet.net/programs/alien/%{name}_%{version}.tar.gz
# Source0-md5:	a6b1f6278ab819635e65b0836186c777
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	44f9b3381776077447bbdb8c64d3f215
Source2: http://ep09.pld-linux.org/~arekm/kde/arts-1.4.3.tar.bz2
Source3: http://ep09.pld-linux.org/~arekm/kde/kdeaccessibility-3.4.3.tar.bz2
Source4: http://ep09.pld-linux.org/~arekm/kde/kdeaddons-3.4.3.tar.bz2
Source5: http://ep09.pld-linux.org/~arekm/kde/kdeadmin-3.4.3.tar.bz2
Source6: http://ep09.pld-linux.org/~arekm/kde/kdeartwork-3.4.3.tar.bz2
Source7: http://ep09.pld-linux.org/~arekm/kde/kdebase-3.4.3.tar.bz2
Source8: http://ep09.pld-linux.org/~arekm/kde/kdebindings-3.4.3.tar.bz2
Source9: http://ep09.pld-linux.org/~arekm/kde/kdeedu-3.4.3.tar.bz2
Source10: http://ep09.pld-linux.org/~arekm/kde/kdegames-3.4.3.tar.bz2
Source11: http://ep09.pld-linux.org/~arekm/kde/kdegraphics-3.4.3.tar.bz2
Source12: http://ep09.pld-linux.org/~arekm/kde/kdelibs-3.4.3.tar.bz2
Source13: http://ep09.pld-linux.org/~arekm/kde/kdemultimedia-3.4.3.tar.bz2
Source14: http://ep09.pld-linux.org/~arekm/kde/kdenetwork-3.4.3.tar.bz2
Source15: http://ep09.pld-linux.org/~arekm/kde/kdepim-3.4.3.tar.bz2
Source16: http://ep09.pld-linux.org/~arekm/kde/kdesdk-3.4.3.tar.bz2
Source17: http://ep09.pld-linux.org/~arekm/kde/kdetoys-3.4.3.tar.bz2
Source18: http://ep09.pld-linux.org/~arekm/kde/kdeutils-3.4.3.tar.bz2
Source19: http://ep09.pld-linux.org/~arekm/kde/kdevelop-3.2.3.tar.bz2
Source20: http://ep09.pld-linux.org/~arekm/kde/kdewebdev-3.4.3.tar.bz2
Source21: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-af-3.4.3.tar.bz2
Source22: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ar-3.4.3.tar.bz2
Source23: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-bg-3.4.3.tar.bz2
Source24: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-bn-3.4.3.tar.bz2
Source25: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-br-3.4.3.tar.bz2
Source26: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-bs-3.4.3.tar.bz2
Source27: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ca-3.4.3.tar.bz2
Source28: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-cs-3.4.3.tar.bz2
Source29: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-cy-3.4.3.tar.bz2
Source30: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-da-3.4.3.tar.bz2
Source31: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-de-3.4.3.tar.bz2
Source32: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-el-3.4.3.tar.bz2
Source33: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-en_GB-3.4.3.tar.bz2
Source34: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-eo-3.4.3.tar.bz2
Source35: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-es-3.4.3.tar.bz2
Source36: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-et-3.4.3.tar.bz2
Source37: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-eu-3.4.3.tar.bz2
Source38: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-fi-3.4.3.tar.bz2
Source39: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-fr-3.4.3.tar.bz2
Source40: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-fy-3.4.3.tar.bz2
Source41: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ga-3.4.3.tar.bz2
Source42: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-he-3.4.3.tar.bz2
Source43: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-hi-3.4.3.tar.bz2
Source44: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-hsb-3.4.3.tar.bz2
Source45: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-hu-3.4.3.tar.bz2
Source46: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-is-3.4.3.tar.bz2
Source47: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-it-3.4.3.tar.bz2
Source48: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ja-3.4.3.tar.bz2
Source49: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-lt-3.4.3.tar.bz2
Source50: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-mk-3.4.3.tar.bz2
Source51: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-nb-3.4.3.tar.bz2
Source52: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-nds-3.4.3.tar.bz2
Source53: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-nl-3.4.3.tar.bz2
Source54: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-nn-3.4.3.tar.bz2
Source55: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-pa-3.4.3.tar.bz2
Source56: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-pl-3.4.3.tar.bz2
Source57: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-pt-3.4.3.tar.bz2
Source58: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-pt_BR-3.4.3.tar.bz2
Source59: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ro-3.4.3.tar.bz2
Source60: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ru-3.4.3.tar.bz2
Source61: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-se-3.4.3.tar.bz2
Source62: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-sk-3.4.3.tar.bz2
Source63: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-sl-3.4.3.tar.bz2
Source64: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-sr-3.4.3.tar.bz2
Source65: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-sr@Latn-3.4.3.tar.bz2
Source66: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-sv-3.4.3.tar.bz2
Source67: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ta-3.4.3.tar.bz2
Source68: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-tg-3.4.3.tar.bz2
Source69: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-tr-3.4.3.tar.bz2
Source70: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-uk-3.4.3.tar.bz2
Source71: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-zh_CN-3.4.3.tar.bz2
Patch0:		%{name}-DESTDIR.patch
URL:		http://kitenet.net/programs/alien/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	cpio
Requires:	%{_bindir}/rpm2cpio
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alien allows you to convert Debian, Stampede and Slackware Packages
into PLD packages, which can be installed with rpm. It can also
convert into Slackware, Debian, and Stampede packages. This is a tool
only suitable for binary packages.

%description -l pl
Alien pozwala przekonwertowaæ pakiety Debiana, Stampede oraz
Slackware w pakiety u¿ywane w PLD, które mog± byæ zainstalowane przy
u¿yciu rpm-a i odwrotnie. Narzêdzie to jest przydatne wy³±cznie dla
pakietów binarnych.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/alien
%{_datadir}/alien
%{perl_vendorlib}/Alien
%{_mandir}/man*/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(pl) %{_mandir}/pl/man1/*
