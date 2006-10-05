%bcond_with	i18n
%define		_urlprefix	http://ep09.pld-linux.org/~arekm/kde/
%define		artsver	1.5.5
%define		kdevelopver 3.3.4
Summary:	Fetch KDE packages to distfiles
Name:		kdefetch
Version:	3.5.5
Release:	1
License:	GPL
Group:		Networking/Hacking
Source2:	%{_urlprefix}/arts-%{artsver}.tar.bz2
# Source2-md5:	3b0aa1ee08c6ef2aefd8d2d88d1ec146
Source3:	%{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source3-md5:	a227e65e012b83c8635f6e16c4dc3259
Source4:	%{_urlprefix}/kdeaddons-%{version}.tar.bz2
# Source4-md5:	71c0a690abf8ad0f43135fa887d0b40c
Source5:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source5-md5:	4af595f5d5506521e8b29a1d92ba3409
Source6:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source6-md5:	8d35156b506cf870eb9641f72a304c8c
Source7:	%{_urlprefix}/kdebase-%{version}.tar.bz2
# Source7-md5:	2ad67fde6d979b7441ac15f46afaec01
Source8:	%{_urlprefix}/kdebindings-%{version}.tar.bz2
# Source8-md5:	e0da219943407a786c2ceea1605fadd1
Source9:	%{_urlprefix}/kdeedu-%{version}.tar.bz2
# Source9-md5:	1659863d74a510bee412d0cb404b4542
Source10:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source10-md5:	1db8e3960ffb6af0a8d683756b89efa7
Source11:	%{_urlprefix}/kdegraphics-%{version}.tar.bz2
# Source11-md5:	cdbe15afc01c5da7af9557e803bbb7e6
Source12:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source12-md5:	f6eabff82e1a7d8533a512aed5f09260
Source13:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source13-md5:	fc8f0911050c42aec0636cf3873e22ba
Source14:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source14-md5:	a6e642c070cbd50d4a817f6588bf8e46
Source15:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source15-md5:	3f2127f74cb496899bb3f1f6f702353b
Source16:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source16-md5:	d226bf07bf8106f37b4e9e31a7d451f0
Source17:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source17-md5:	2b03fd068209cf324396b75334f39aba
Source18:	%{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source18-md5:	a20a732284a3dcb735665e45f5be532e
Source19:	%{_urlprefix}/kdevelop-%{kdevelopver}.tar.bz2
# Source19-md5:	e5278e37468bda7fdf6d019f84aeed16
Source20:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source20-md5:	d0655fd0286607f4726a82db96f00da3
%if %{with i18n}
Source21:	%{_urlprefix}/kde-i18n/kde-i18n-af-%{version}.tar.bz2
# Source21-md5:	3de24c2c32aba906b9e2cea304b151be
Source22:	%{_urlprefix}/kde-i18n/kde-i18n-ar-%{version}.tar.bz2
# Source22-md5:	237879698e967ba9384b6800f8517ce2
Source220:	%{_urlprefix}/kde-i18n/kde-i18n-az-%{version}.tar.bz2
# Source220-md5:	c63e0b5e0682571498b168e6f6707caf
Source23:	%{_urlprefix}/kde-i18n/kde-i18n-bg-%{version}.tar.bz2
# Source23-md5:	28871147d247f33072a278f0d16a96be
Source24:	%{_urlprefix}/kde-i18n/kde-i18n-bn-%{version}.tar.bz2
# Source24-md5:	bfd5159743442c47a02ee5af4bd17c68
Source25:	%{_urlprefix}/kde-i18n/kde-i18n-br-%{version}.tar.bz2
# Source25-md5:	f96e07c3b9f4905dc3f37eb829feba89
Source26:	%{_urlprefix}/kde-i18n/kde-i18n-bs-%{version}.tar.bz2
# Source26-md5:	8441891d28b9785504ab1151a603d8f4
Source27:	%{_urlprefix}/kde-i18n/kde-i18n-ca-%{version}.tar.bz2
# Source27-md5:	fec16708dc8c3e9a864d5ad9e45f06b8
Source28:	%{_urlprefix}/kde-i18n/kde-i18n-cs-%{version}.tar.bz2
# Source28-md5:	aaace6da2097b2f98f163a5da7667752
Source29:	%{_urlprefix}/kde-i18n/kde-i18n-cy-%{version}.tar.bz2
# Source29-md5:	fae86d2ffa550c4d831eeb9a5a3ecdb2
Source30:	%{_urlprefix}/kde-i18n/kde-i18n-da-%{version}.tar.bz2
# Source30-md5:	70c041ca96330834c6f988255d7bd6ae
Source31:	%{_urlprefix}/kde-i18n/kde-i18n-de-%{version}.tar.bz2
# Source31-md5:	a99bf0e5d298fce191ad2c938af3afdb
Source32:	%{_urlprefix}/kde-i18n/kde-i18n-el-%{version}.tar.bz2
# Source32-md5:	a2cb7afd4c5883bc2eb5d9c8a96d04c0
Source33:	%{_urlprefix}/kde-i18n/kde-i18n-en_GB-%{version}.tar.bz2
# Source33-md5:	50af460c4b69e5cd91b820ed656f99bd
Source34:	%{_urlprefix}/kde-i18n/kde-i18n-eo-%{version}.tar.bz2
# Source34-md5:	c55c9ae0c001e5214f1ad97f4b6d02a1
Source35:	%{_urlprefix}/kde-i18n/kde-i18n-es-%{version}.tar.bz2
# Source35-md5:	d8dc649138fe136c57a808eac1fdd719
Source36:	%{_urlprefix}/kde-i18n/kde-i18n-et-%{version}.tar.bz2
# Source36-md5:	d3065d66591fa0ea4e304e9bcbb6dc10
Source37:	%{_urlprefix}/kde-i18n/kde-i18n-eu-%{version}.tar.bz2
# Source37-md5:	45a4361f11c14b8cbc0a5bb29ab18edb
Source370:	%{_urlprefix}/kde-i18n/kde-i18n-fa-%{version}.tar.bz2
# Source370-md5:	e55d8c8d06097b3daaa71eb499114e3d
Source38:	%{_urlprefix}/kde-i18n/kde-i18n-fi-%{version}.tar.bz2
# Source38-md5:	5693b184f6d3e2d79c78248a9506ba11
Source39:	%{_urlprefix}/kde-i18n/kde-i18n-fr-%{version}.tar.bz2
# Source39-md5:	0a0e9ba98b33e81a092110563def9ca4
Source40:	%{_urlprefix}/kde-i18n/kde-i18n-fy-%{version}.tar.bz2
# Source40-md5:	98a3bbe04e82b89c8ab2a821741ffc34
Source41:	%{_urlprefix}/kde-i18n/kde-i18n-ga-%{version}.tar.bz2
# Source41-md5:	e82a3ff13cb0f8d73578f1a3770a119c
Source410:	%{_urlprefix}/kde-i18n/kde-i18n-gl-%{version}.tar.bz2
# Source410-md5:	bf3ad88fea56ded7fd451cc83826e4c5
Source42:	%{_urlprefix}/kde-i18n/kde-i18n-he-%{version}.tar.bz2
# Source42-md5:	2099f23192fe79f1e94c0da2184871c0
Source43:	%{_urlprefix}/kde-i18n/kde-i18n-hi-%{version}.tar.bz2
# Source43-md5:	a046a16fd6575ee67a9086702414bac1
Source44:	%{_urlprefix}/kde-i18n/kde-i18n-hr-%{version}.tar.bz2
# Source44-md5:	486262b00bab42965aa0d25c86d65f84
Source45:	%{_urlprefix}/kde-i18n/kde-i18n-hu-%{version}.tar.bz2
# Source45-md5:	9638821a380cf7a8697b03dca2f3513d
Source46:	%{_urlprefix}/kde-i18n/kde-i18n-is-%{version}.tar.bz2
# Source46-md5:	4bdd95af464b36e7d52b4848291c9717
Source47:	%{_urlprefix}/kde-i18n/kde-i18n-it-%{version}.tar.bz2
# Source47-md5:	a69220e5a700a277238924a3675d9dbd
Source48:	%{_urlprefix}/kde-i18n/kde-i18n-ja-%{version}.tar.bz2
# Source48-md5:	3b89aa140388f7b0e3beb80ef2b8b247
Source480:	%{_urlprefix}/kde-i18n/kde-i18n-lv-%{version}.tar.bz2
# Source480-md5:	f541bb2957e1f0469d76711cc86ba851
Source49:	%{_urlprefix}/kde-i18n/kde-i18n-lt-%{version}.tar.bz2
# Source49-md5:	aa799b8fac440c0b70188e0f9df16350
Source490:	%{_urlprefix}/kde-i18n/kde-i18n-km-%{version}.tar.bz2
# Source490-md5:	c11c4653c9e211deb4c16bf346bd03ad
Source491:	%{_urlprefix}/kde-i18n/kde-i18n-ko-%{version}.tar.bz2
# Source491-md5:	7a364e95e894e9c58d56054edab21142
Source50:	%{_urlprefix}/kde-i18n/kde-i18n-mk-%{version}.tar.bz2
# Source50-md5:	014b290f599e808ff3b885c50d150fe5
Source500:	%{_urlprefix}/kde-i18n/kde-i18n-mn-%{version}.tar.bz2
# Source500-md5:	67fb64745786c2ef908b192432e51040
Source501:	%{_urlprefix}/kde-i18n/kde-i18n-ms-%{version}.tar.bz2
# Source501-md5:	2757eb622ace8a2f231dda1bd5cd454d
Source51:	%{_urlprefix}/kde-i18n/kde-i18n-nb-%{version}.tar.bz2
# Source51-md5:	1b3edcfa11bb648e98bab07f93e898a9
Source52:	%{_urlprefix}/kde-i18n/kde-i18n-nds-%{version}.tar.bz2
# Source52-md5:	f159dd39c2385403a0f95c0b102ef67b
Source53:	%{_urlprefix}/kde-i18n/kde-i18n-nl-%{version}.tar.bz2
# Source53-md5:	44b404fc4d0b9d12714fdf2357fa3f56
Source54:	%{_urlprefix}/kde-i18n/kde-i18n-nn-%{version}.tar.bz2
# Source54-md5:	964c91710f2b28cdde7b8cdfef961791
Source55:	%{_urlprefix}/kde-i18n/kde-i18n-pa-%{version}.tar.bz2
# Source55-md5:	1881a7e5b1fc6b75ca74dc4c504ad16d
Source56:	%{_urlprefix}/kde-i18n/kde-i18n-pl-%{version}.tar.bz2
# Source56-md5:	7444560d7d6cb3221e8f0907218157de
Source57:	%{_urlprefix}/kde-i18n/kde-i18n-pt-%{version}.tar.bz2
# Source57-md5:	af8b477236f98e0fa7fcae21db3df5cc
Source58:	%{_urlprefix}/kde-i18n/kde-i18n-pt_BR-%{version}.tar.bz2
# Source58-md5:	d9359ccc0040a5c6ac88d5cad12d4fcf
Source59:	%{_urlprefix}/kde-i18n/kde-i18n-ro-%{version}.tar.bz2
# Source59-md5:	b31d031cbf2deae408c94a665677dfd2
Source60:	%{_urlprefix}/kde-i18n/kde-i18n-ru-%{version}.tar.bz2
# Source60-md5:	4bfa140a22122446fd8ab356d32fee40
Source600:	%{_urlprefix}/kde-i18n/kde-i18n-rw-%{version}.tar.bz2
# Source600-md5:	b94681f15ccb61cd9760e2e7830e7592
Source61:	%{_urlprefix}/kde-i18n/kde-i18n-se-%{version}.tar.bz2
# Source61-md5:	4492ee7304d4539b3dfd4d1349c6a838
Source62:	%{_urlprefix}/kde-i18n/kde-i18n-sk-%{version}.tar.bz2
# Source62-md5:	0a1bccde30cf25cf37974362585b118a
Source63:	%{_urlprefix}/kde-i18n/kde-i18n-sl-%{version}.tar.bz2
# Source63-md5:	3574861dc47aa09ada8cc6c7bca2307e
Source64:	%{_urlprefix}/kde-i18n/kde-i18n-sr-%{version}.tar.bz2
# Source64-md5:	e308f4f37c5509bd5583f7fcd90bcb32
Source65:	%{_urlprefix}/kde-i18n/kde-i18n-sr@Latn-%{version}.tar.bz2
# Source65-md5:	0e3d6ba65882faadc89791c3691b19b6
Source660:	%{_urlprefix}/kde-i18n/kde-i18n-ss-%{version}.tar.bz2
# Source660-md5:	8a08733c9cd4d367a42f0c0a69accc8a
Source66:	%{_urlprefix}/kde-i18n/kde-i18n-sv-%{version}.tar.bz2
# Source66-md5:	0a614fc596f082a1a11d7ee91b1bae2a
Source67:	%{_urlprefix}/kde-i18n/kde-i18n-ta-%{version}.tar.bz2
# Source67-md5:	4ab3c05628fc635609218d17cce6d138
Source68:	%{_urlprefix}/kde-i18n/kde-i18n-tg-%{version}.tar.bz2
# Source68-md5:	135a419bb0d3429dde4bc698d095bf86
Source69:	%{_urlprefix}/kde-i18n/kde-i18n-tr-%{version}.tar.bz2
# Source69-md5:	001d5909b3fd8121b1f4f7970d88215b
Source70:	%{_urlprefix}/kde-i18n/kde-i18n-uk-%{version}.tar.bz2
# Source70-md5:	fc18b699825837e49e3062e5acc0a3f5
Source700:	%{_urlprefix}/kde-i18n/kde-i18n-uz-%{version}.tar.bz2
# Source700-md5:	b66b574eff1fd2349a9a767098e5430e
Source71:	%{_urlprefix}/kde-i18n/kde-i18n-zh_CN-%{version}.tar.bz2
# Source71-md5:	c0df78b39982a1ba117539e86c0dabb8
Source710:	%{_urlprefix}/kde-i18n/kde-i18n-zh_TW-%{version}.tar.bz2
# Source710-md5:	6c1051a985f68563380844dec9080248
%endif
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
