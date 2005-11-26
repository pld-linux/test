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
Source2: http://ep09.pld-linux.org/~arekm/kde/arts-1.5.0.tar.bz2
# Source2-md5:	e90a32ee47d5cdc51fe1b7f6f6c0df63
Source3: http://ep09.pld-linux.org/~arekm/kde/kdeaccessibility-3.5.0.tar.bz2
# Source3-md5:	f88f3340acdd219050759df86e3d97d0
Source4: http://ep09.pld-linux.org/~arekm/kde/kdeaddons-3.5.0.tar.bz2
# Source4-md5:	a61bcb10580208c3abb8c47aed198597
Source5: http://ep09.pld-linux.org/~arekm/kde/kdeadmin-3.5.0.tar.bz2
# Source5-md5:	9d0f914d2d0d3fbef8ed51cfdab36d40
Source6: http://ep09.pld-linux.org/~arekm/kde/kdeartwork-3.5.0.tar.bz2
# Source6-md5:	052c736c9c12defbb2e7de04ff0b2ae6
Source7: http://ep09.pld-linux.org/~arekm/kde/kdebase-3.5.0.tar.bz2
# Source7-md5:	ab5a1b3541825c88646c926083e3aefd
Source8: http://ep09.pld-linux.org/~arekm/kde/kdebindings-3.5.0.tar.bz2
# Source8-md5:	137924318ff5fc49cee3c82ee0ce5cf5
Source9: http://ep09.pld-linux.org/~arekm/kde/kdeedu-3.5.0.tar.bz2
# Source9-md5:	ac66cfcc8e23227973596cf62cf78a4c
Source10: http://ep09.pld-linux.org/~arekm/kde/kdegames-3.5.0.tar.bz2
# Source10-md5:	ba86fe9280ca57698ce3be0e0242b140
Source11: http://ep09.pld-linux.org/~arekm/kde/kdegraphics-3.5.0.tar.bz2
# Source11-md5:	389a00d4387e621d4dd325a59c7657c4
Source12: http://ep09.pld-linux.org/~arekm/kde/kdelibs-3.5.0.tar.bz2
# Source12-md5:	2b11d654e2ea1a3cd16dcfdcbb7d1915
Source13: http://ep09.pld-linux.org/~arekm/kde/kdemultimedia-3.5.0.tar.bz2
# Source13-md5:	dd0ba9ccb2f522508c6543cd24e54c98
Source14: http://ep09.pld-linux.org/~arekm/kde/kdenetwork-3.5.0.tar.bz2
# Source14-md5:	c83dce8cc496b6ec8773483df1c85119
Source15: http://ep09.pld-linux.org/~arekm/kde/kdepim-3.5.0.tar.bz2
# Source15-md5:	e19a2a40e422ecd483884ce6e9ac8925
Source16: http://ep09.pld-linux.org/~arekm/kde/kdesdk-3.5.0.tar.bz2
# Source16-md5:	dc91ffcfa8114cf4f9d40bc9ffe47d97
Source17: http://ep09.pld-linux.org/~arekm/kde/kdetoys-3.5.0.tar.bz2
# Source17-md5:	aebe4a9586728b37543bd515d35e76e1
Source18: http://ep09.pld-linux.org/~arekm/kde/kdeutils-3.5.0.tar.bz2
# Source18-md5:	d6b2cbe8b7d15166eff261f20ece2718
Source19: http://ep09.pld-linux.org/~arekm/kde/kdevelop-3.3.0.tar.bz2
# Source19-md5:	1048c89c1aad0daf6581bb04e15206c4
Source20: http://ep09.pld-linux.org/~arekm/kde/kdewebdev-3.5.0.tar.bz2
# Source20-md5:	58bb4d025fa125c5ad0dc43769ba9786
Source21: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-af-3.5.0.tar.bz2
# Source21-md5:	147f1e8d2fbc34044803a001d7bcdfa5
Source22: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ar-3.5.0.tar.bz2
# Source22-md5:	ddae126b0e6f157c7ab216886da9a9cc
Source23: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-bg-3.5.0.tar.bz2
# Source23-md5:	14a1c0ffca9b70befd62aac08a76ce26
Source24: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-bn-3.5.0.tar.bz2
# Source24-md5:	76eb28c1ace6f2279657d8574f9f0814
Source25: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-br-3.5.0.tar.bz2
# Source25-md5:	88ada204a76c69b594d704fdefc102eb
Source26: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-bs-3.5.0.tar.bz2
# Source26-md5:	f7c7e067fc001592eda493be30d84f8d
Source27: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ca-3.5.0.tar.bz2
# Source27-md5:	1757ccb438e4cc2edb9c5af7c0ffc736
Source28: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-cs-3.5.0.tar.bz2
# Source28-md5:	d7ccfd209c90ddb92e60476481bd20e3
Source29: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-cy-3.5.0.tar.bz2
# Source29-md5:	77be5513037a06d51e287d262a50afbe
Source30: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-da-3.5.0.tar.bz2
# Source30-md5:	2fabb8a20a0c197b4749b93359d25fc1
Source31: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-de-3.5.0.tar.bz2
# Source31-md5:	71e66fbc6d497808364ff2ae02e2f9a3
Source32: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-el-3.5.0.tar.bz2
# Source32-md5:	bd70e25fc9ad9ac7c09584bab498cf4c
Source33: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-en_GB-3.5.0.tar.bz2
# Source33-md5:	bb505653bdd061665b48dd1438a7373d
Source34: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-eo-3.5.0.tar.bz2
# Source34-md5:	0028cfb93075bba73d902d68d56ab529
Source35: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-es-3.5.0.tar.bz2
# Source35-md5:	8bf984ce3aaaa7d58156458d4eafd5bd
Source36: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-et-3.5.0.tar.bz2
# Source36-md5:	4c6be2284f34897fffa4cdce85f51fb4
Source37: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-eu-3.5.0.tar.bz2
# Source37-md5:	ef6917edb2c87f2386feb7c1b2d175c7
Source38: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-fi-3.5.0.tar.bz2
# Source38-md5:	f4b68d979d9181561e04e0ec3cb6c5f2
Source39: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-fr-3.5.0.tar.bz2
# Source39-md5:	aec9d5ab04f9dc5a3cc4a8093bd9f7d4
Source40: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-fy-3.5.0.tar.bz2
# Source40-md5:	643d1f5d1ff3a21e2b16a8bcdd4b477d
Source41: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ga-3.5.0.tar.bz2
# Source41-md5:	b98c98d80e2a5f8e4d1935df49ad92f0
Source42: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-he-3.5.0.tar.bz2
# Source42-md5:	3a5c77420709d437521c2a9b7d4183a5
Source43: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-hi-3.5.0.tar.bz2
# Source43-md5:	afdc78d57f13e7999178d5784222e0be
Source44: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-hr-3.5.0.tar.bz2
# Source44-md5:	04fcf08871542ff837a56c33b1544f5e
Source45: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-hu-3.5.0.tar.bz2
# Source45-md5:	9e4108754b8b9d84157f8a139749f96e
Source46: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-is-3.5.0.tar.bz2
# Source46-md5:	9ecfc0c82796bca3f7cbb621b2535b51
Source47: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-it-3.5.0.tar.bz2
# Source47-md5:	1d2c594bf5c6f853822ae869ae101373
Source48: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ja-3.5.0.tar.bz2
# Source48-md5:	404c4ad98acc237eb4ea36b1b637f708
Source49: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-lt-3.5.0.tar.bz2
# Source49-md5:	f03e5c7dac20f93f215c01e4f76de2bc
Source50: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-mk-3.5.0.tar.bz2
# Source50-md5:	e047bf6f6eb21af2530781aabe871c55
Source51: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-nb-3.5.0.tar.bz2
# Source51-md5:	a9d408cb53d33d9ad2a27b7e75878ff2
Source52: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-nds-3.5.0.tar.bz2
# Source52-md5:	11c2c720ca547e95ae0e3ff620525219
Source53: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-nl-3.5.0.tar.bz2
# Source53-md5:	5253d78852e4692abbfaf422eb13612f
Source54: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-nn-3.5.0.tar.bz2
# Source54-md5:	e8f4d8fc6600f34667c2426908e9e87c
Source55: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-pa-3.5.0.tar.bz2
# Source55-md5:	c62a690a4e8e2f20da3e69ad9459168b
Source56: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-pl-3.5.0.tar.bz2
# Source56-md5:	dd1a8db5e7ac7fb7fbf88fc89c6248d6
Source57: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-pt-3.5.0.tar.bz2
# Source57-md5:	14e6a97e5f03902449ef7f79a8c6ca3f
Source58: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-pt_BR-3.5.0.tar.bz2
# Source58-md5:	94bf46c3b6b3f2f3d315c17b7b0df496
Source59: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ro-3.5.0.tar.bz2
# Source59-md5:	5dcaf0e47bc367bbc8a93b8325e95007
Source60: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ru-3.5.0.tar.bz2
# Source60-md5:	8f6c9961e3df806d1bb2ecab073436fe
Source61: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-se-3.5.0.tar.bz2
# Source61-md5:	12eda3a6000f45624dba73a43e0151db
Source62: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-sk-3.5.0.tar.bz2
# Source62-md5:	64289a8a8d2ffd4de136faca3b901453
Source63: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-sl-3.5.0.tar.bz2
# Source63-md5:	29618443a77a8b657f6003ce28db8471
Source64: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-sr-3.5.0.tar.bz2
# Source64-md5:	305e7594a705c1ffaf566f0adb543dc8
Source65: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-sr@Latn-3.5.0.tar.bz2
# Source65-md5:	f3a2dfb04cfa1d41ec55d2e5112654a7
Source66: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-sv-3.5.0.tar.bz2
# Source66-md5:	1eb351f2332fa6c51fecba7eecb1ca61
Source67: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-ta-3.5.0.tar.bz2
# Source67-md5:	4776430c0e6d5aa4455ebc8406e8a373
Source68: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-tg-3.5.0.tar.bz2
# Source68-md5:	33331fd43fa6f7026ca40dd95184dfa2
Source69: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-tr-3.5.0.tar.bz2
# Source69-md5:	0fd7a1e932ec5bf1bfe494ee00b3cd09
Source70: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-uk-3.5.0.tar.bz2
# Source70-md5:	039bf39e0b7df0906358667f2bbefe46
Source71: http://ep09.pld-linux.org/~arekm/kde/kde-i18n/kde-i18n-zh_CN-3.5.0.tar.bz2
# Source71-md5:	aba75e252510e999a17650994934065c
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
