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
# Source2-md5:	58585969a9a33784601122c77bd15a1e
Source3: http://ep09.pld-linux.org/~arekm/kde/kdeaccessibility-3.4.3.tar.bz2
# Source3-md5:	02f8ffe95f253aaab8a13ab7211494dc
Source4: http://ep09.pld-linux.org/~arekm/kde/kdeaddons-3.4.3.tar.bz2
# Source4-md5:	e927d60e94adba69e78f82d82305f4ce
Source5: http://ep09.pld-linux.org/~arekm/kde/kdeadmin-3.4.3.tar.bz2
# Source5-md5:	ded1ff7ea33f6634ee342b671bbe6677
Source6: http://ep09.pld-linux.org/~arekm/kde/kdeartwork-3.4.3.tar.bz2
# Source6-md5:	a571991c6e21321177febafadb61efaa
Source7: http://ep09.pld-linux.org/~arekm/kde/kdebase-3.4.3.tar.bz2
# Source7-md5:	7b25feba2774c077601d472dae5352c8
Source8: http://ep09.pld-linux.org/~arekm/kde/kdebindings-3.4.3.tar.bz2
# Source8-md5:	0fb123df324b4d007351c89051532dee
Source9: http://ep09.pld-linux.org/~arekm/kde/kdeedu-3.4.3.tar.bz2
# Source9-md5:	9f4059beb1c3495973dd80d11bcae462
Source10: http://ep09.pld-linux.org/~arekm/kde/kdegames-3.4.3.tar.bz2
# Source10-md5:	40ae2b318b94ab1832b484d2a4d3ab83
Source11: http://ep09.pld-linux.org/~arekm/kde/kdegraphics-3.4.3.tar.bz2
# Source11-md5:	e2b2926301204a0f587d9e6e163c06d9
Source12: http://ep09.pld-linux.org/~arekm/kde/kdelibs-3.4.3.tar.bz2
# Source12-md5:	0cd7c0c8a81e5d11b91b407a4aaaf3ff
Source13: http://ep09.pld-linux.org/~arekm/kde/kdemultimedia-3.4.3.tar.bz2
# Source13-md5:	49fed5afad01c322d3bc8c6a175d1898
Source14: http://ep09.pld-linux.org/~arekm/kde/kdenetwork-3.4.3.tar.bz2
# Source14-md5:	9c762557e6572b2d53736fefc33b028a
Source15: http://ep09.pld-linux.org/~arekm/kde/kdepim-3.4.3.tar.bz2
# Source15-md5:	b2c145f3779578c9208dcbec9a4a5aea
Source16: http://ep09.pld-linux.org/~arekm/kde/kdesdk-3.4.3.tar.bz2
# Source16-md5:	d0d51c35769709b00b2ff7d59ed90631
Source17: http://ep09.pld-linux.org/~arekm/kde/kdetoys-3.4.3.tar.bz2
# Source17-md5:	1dae200dc1be8527a5f7dca690cbffc1
Source18: http://ep09.pld-linux.org/~arekm/kde/kdeutils-3.4.3.tar.bz2
# Source18-md5:	d467284b523bb1268da776cd016ede4d
Source19: http://ep09.pld-linux.org/~arekm/kde/kdevelop-3.2.3.tar.bz2
# Source19-md5:	7dfae96e274c6dcb4748419452ebdf35
Source20: http://ep09.pld-linux.org/~arekm/kde/kdewebdev-3.4.3.tar.bz2
# Source20-md5:	e3750c242404449ac9640fbf5ed7d042
Source21: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-af-3.4.3.tar.bz2
# Source21-md5:	eea5169ceefe911123cfa4be1d2263a4
Source22: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ar-3.4.3.tar.bz2
# Source22-md5:	ce01c8fd9addbc389b6847a0f71ca3d2
Source23: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-bg-3.4.3.tar.bz2
# Source23-md5:	b861ea9ffd502da8147265345ba8a39b
Source24: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-bn-3.4.3.tar.bz2
# Source24-md5:	1f287e0484fb9c48d08a7d045bd2b004
Source25: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-br-3.4.3.tar.bz2
# Source25-md5:	91112b5ac824987fc0065a6abfedbca4
Source26: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-bs-3.4.3.tar.bz2
# Source26-md5:	48ede0b61bff3bfea8e757d71f9967f8
Source27: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ca-3.4.3.tar.bz2
# Source27-md5:	27af429dce051fec177beb9d2afa622b
Source28: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-cs-3.4.3.tar.bz2
# Source28-md5:	65fcbfd8c18c2b3b29b52456c38d8819
Source29: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-cy-3.4.3.tar.bz2
# Source29-md5:	df2a5b4ffde2eaafeeb9d11aa45a4473
Source30: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-da-3.4.3.tar.bz2
# Source30-md5:	ec644dbe2ad27c1a550bfd2f0496dcff
Source31: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-de-3.4.3.tar.bz2
# Source31-md5:	1fa9c6c26696f338ac1e86fbcd1a909c
Source32: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-el-3.4.3.tar.bz2
# Source32-md5:	cd796b785298559e7c51ea843ac83916
Source33: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-en_GB-3.4.3.tar.bz2
# Source33-md5:	0e5035fec7b827f88e42d540e40bf2a3
Source34: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-eo-3.4.3.tar.bz2
# Source34-md5:	707b492c0e85aa0fb54935be5c580a34
Source35: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-es-3.4.3.tar.bz2
# Source35-md5:	70196022518c5c81b2f8b2ee50f0dd0a
Source36: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-et-3.4.3.tar.bz2
# Source36-md5:	fe591f6640f5ef30f5b3e0d45433abee
Source37: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-eu-3.4.3.tar.bz2
# Source37-md5:	306f05bf924bbb00d567c9531d0f97e2
Source38: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-fi-3.4.3.tar.bz2
# Source38-md5:	a3d8caeaf28d116b10945801e3b12c4f
Source39: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-fr-3.4.3.tar.bz2
# Source39-md5:	b87c4c18e47985cf9033d002e5cc1125
Source40: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-fy-3.4.3.tar.bz2
# Source40-md5:	de17112c336c0dfa66797d47c35cb025
Source41: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ga-3.4.3.tar.bz2
# Source41-md5:	394944fb0424c635fdb1df8e403770c1
Source42: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-he-3.4.3.tar.bz2
# Source42-md5:	7cf7d8d7ef4b3224cf5744ff85413aa3
Source43: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-hi-3.4.3.tar.bz2
# Source43-md5:	52c74b0408402bac5342a1edfcf7838e
Source44: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-hsb-3.4.3.tar.bz2
# Source44-md5:	0b0f7122386d2774cc7f6df4b74559db
Source45: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-hu-3.4.3.tar.bz2
# Source45-md5:	63e89048b260f707e8a4d1fe2387dbb5
Source46: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-is-3.4.3.tar.bz2
# Source46-md5:	857a45f709ebd0813d7e353f84ed2428
Source47: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-it-3.4.3.tar.bz2
# Source47-md5:	47b6f1a8df42579d966533c00cd4286c
Source48: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ja-3.4.3.tar.bz2
# Source48-md5:	89a9d0bf0e3505bd30029ef95a1a23f2
Source49: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-lt-3.4.3.tar.bz2
# Source49-md5:	26e273369cf75a2a9b841bfbf0d7791f
Source50: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-mk-3.4.3.tar.bz2
# Source50-md5:	22200cebfd40341b977500e0a24904c3
Source51: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-nb-3.4.3.tar.bz2
# Source51-md5:	746dbc6b53c199d74dab338b8ab34a6e
Source52: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-nds-3.4.3.tar.bz2
# Source52-md5:	5abb97b9dbed7434b66b4ad7e6ea8f71
Source53: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-nl-3.4.3.tar.bz2
# Source53-md5:	783c361891bd5800f9d56c90b8b59cae
Source54: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-nn-3.4.3.tar.bz2
# Source54-md5:	daf6a7c419d39805c3dcccf057050f31
Source55: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-pa-3.4.3.tar.bz2
# Source55-md5:	ac47ec3d56f0d451fe6d0bb97576be17
Source56: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-pl-3.4.3.tar.bz2
# Source56-md5:	9e770a34bdade6f8c1e136ba3e8d43f4
Source57: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-pt-3.4.3.tar.bz2
# Source57-md5:	35a2c05d396c257f3f0647151ce6d25a
Source58: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-pt_BR-3.4.3.tar.bz2
# Source58-md5:	fe4af050de12249999eb1aa43ac683ab
Source59: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ro-3.4.3.tar.bz2
# Source59-md5:	5c493025f972fc7b63045756977e6ac9
Source60: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ru-3.4.3.tar.bz2
# Source60-md5:	4e5a7ddc4ac505f5c494c923646209b5
Source61: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-se-3.4.3.tar.bz2
# Source61-md5:	ff20d24d689ad581b25b4d3a2cb9e760
Source62: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-sk-3.4.3.tar.bz2
# Source62-md5:	6f4125979eaf18c3bb24ccc0b461da46
Source63: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-sl-3.4.3.tar.bz2
# Source63-md5:	83d38b7a3bf7dda5e3817e465a5d8c5d
Source64: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-sr-3.4.3.tar.bz2
# Source64-md5:	4c440703d722df7969b17f09441e7ef4
Source65: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-sr@Latn-3.4.3.tar.bz2
# Source65-md5:	4c7e5f42bf79218d1de318e8cb312b9d
Source66: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-sv-3.4.3.tar.bz2
# Source66-md5:	b9f30d8d32883e462bafbb47cabf9e83
Source67: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ta-3.4.3.tar.bz2
# Source67-md5:	5ee503892416d20e64119c0d05da294c
Source68: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-tg-3.4.3.tar.bz2
# Source68-md5:	832372d20f761260d37a69475ed3e94d
Source69: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-tr-3.4.3.tar.bz2
# Source69-md5:	f7334b33ffb57b8f4b9480ec6ed793c8
Source70: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-uk-3.4.3.tar.bz2
# Source70-md5:	3d716310e45ee12040fc140d8ba2c502
Source71: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-zh_CN-3.4.3.tar.bz2
# Source71-md5:	6efbbf16c3cd3db89b8806101e2a6a0e
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
