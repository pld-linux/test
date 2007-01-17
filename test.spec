%bcond_with	i18n
%define		_urlprefix	http://ep09.pld-linux.org/~arekm/kde/
%define		artsver	1.5.6
%define		kdevelopver 3.3.6
Summary:	Fetch KDE packages to distfiles
Name:		kdefetch
Version:	3.5.6
Release:	1
License:	GPL
Group:		Networking/Hacking
Source2:	%{_urlprefix}/arts-%{artsver}.tar.bz2
# Source2-md5:	e986393a5827499bbad04a00b797add0
Source3:	%{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source3-md5:	03d3c9f4d8c2fd12b7d0e020e11cd88e
Source4:	%{_urlprefix}/kdeaddons-%{version}.tar.bz2
# Source4-md5:	96d6d2a76da2a5232b3b46318456a5bc
Source5:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source5-md5:	13654a93e83b7c8fd2ccce3aceb2d535
Source6:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source6-md5:	4c817eab517fba30fce8f3b40a6f019d
Source7:	%{_urlprefix}/kdebase-%{version}.tar.bz2
# Source7-md5:	a53f589f58012e655a52220a6a151019
Source8:	%{_urlprefix}/kdebindings-%{version}.tar.bz2
# Source8-md5:	d26b5f54f062b765a949d66657c2ab3c
Source9:	%{_urlprefix}/kdeedu-%{version}.tar.bz2
# Source9-md5:	6017317b133d973e7fc8a279a81f37a1
Source10:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source10-md5:	d6cdf7d9235896670d5299e9e91665e2
Source11:	%{_urlprefix}/kdegraphics-%{version}.tar.bz2
# Source11-md5:	79a1ffb7ae89bede1410411a30be3210
Source12:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source12-md5:	f2da82c44b8a4e177018732e64a83a36
Source13:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source13-md5:	57c50bfcb0147324a1af02ebcc103376
Source14:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source14-md5:	0f428cccc4ea16aa53c427530874c591
Source15:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source15-md5:	e37e6173fe9fd7f242c9502a4ae1d7de
Source16:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source16-md5:	1462e1a884fdaa070ed493c10a336728
Source17:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source17-md5:	7d4f1a33e5379f789fcbf17b9e503bfd
Source18:	%{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source18-md5:	e0ea2c15ccf2bd3d8be5f2bf57cfe14a
Source19:	%{_urlprefix}/kdevelop-%{kdevelopver}.tar.bz2
# Source19-md5:	0de7c7d82c176456f2adff48981f5d40
Source20:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source20-md5:	fa1fc2d7c81465c7e1762014a892ced3
%if %{with i18n}
Source21:	%{_urlprefix}/kde-i18n/kde-i18n-af-%{version}.tar.bz2
# Source21-md5:	7771bdb76b76323a68da4700bd5eaf26
Source22:	%{_urlprefix}/kde-i18n/kde-i18n-ar-%{version}.tar.bz2
# Source22-md5:	e79ef203dfc9196ea75089dfcd99339d
Source220:	%{_urlprefix}/kde-i18n/kde-i18n-az-%{version}.tar.bz2
# Source220-md5:	416e628f6c3d27a334d26f1c5bd83406
Source23:	%{_urlprefix}/kde-i18n/kde-i18n-bg-%{version}.tar.bz2
# Source23-md5:	a34d5e307d418fc87bcbb6ab150bc046
Source24:	%{_urlprefix}/kde-i18n/kde-i18n-bn-%{version}.tar.bz2
# Source24-md5:	f5153ad329e8d7305aefa12f7ddfdfa3
Source25:	%{_urlprefix}/kde-i18n/kde-i18n-br-%{version}.tar.bz2
# Source25-md5:	5c4ae705596f83ac2ee5df83a7900e5b
Source26:	%{_urlprefix}/kde-i18n/kde-i18n-bs-%{version}.tar.bz2
# Source26-md5:	df40c6f49ebbc00155eea55f913d1600
Source27:	%{_urlprefix}/kde-i18n/kde-i18n-ca-%{version}.tar.bz2
# Source27-md5:	84b3a011b9d594ce26fdee77cccdfb52
Source28:	%{_urlprefix}/kde-i18n/kde-i18n-cs-%{version}.tar.bz2
# Source28-md5:	b2dab45ea572efbb2569781211c2a7fc
Source29:	%{_urlprefix}/kde-i18n/kde-i18n-cy-%{version}.tar.bz2
# Source29-md5:	3d3ddcd729b5ade752b498a42aeac39c
Source30:	%{_urlprefix}/kde-i18n/kde-i18n-da-%{version}.tar.bz2
# Source30-md5:	913550e6604b9423cea605d95a8a664f
Source31:	%{_urlprefix}/kde-i18n/kde-i18n-de-%{version}.tar.bz2
# Source31-md5:	c8a52e825c610ae5779ef84d1bf7e3c5
Source32:	%{_urlprefix}/kde-i18n/kde-i18n-el-%{version}.tar.bz2
# Source32-md5:	f395db170010c2a4ee9a7e27b1c8772e
Source33:	%{_urlprefix}/kde-i18n/kde-i18n-en_GB-%{version}.tar.bz2
# Source33-md5:	6b81bfa733c5e1c8ae4d16208093f648
Source34:	%{_urlprefix}/kde-i18n/kde-i18n-eo-%{version}.tar.bz2
# Source34-md5:	7f17faa2bda08f31e1f33a3242f0b960
Source35:	%{_urlprefix}/kde-i18n/kde-i18n-es-%{version}.tar.bz2
# Source35-md5:	75f2b236131bcf89b6f2302c1fb8780f
Source36:	%{_urlprefix}/kde-i18n/kde-i18n-et-%{version}.tar.bz2
# Source36-md5:	55647fdaf91b9626618015017be954b4
Source37:	%{_urlprefix}/kde-i18n/kde-i18n-eu-%{version}.tar.bz2
# Source37-md5:	6413e62d868721be5b269e50e979d4b1
Source370:	%{_urlprefix}/kde-i18n/kde-i18n-fa-%{version}.tar.bz2
# Source370-md5:	be881e4b7be80e289b9dcdf00753ce79
Source38:	%{_urlprefix}/kde-i18n/kde-i18n-fi-%{version}.tar.bz2
# Source38-md5:	227d47ad0232daf190653b4f8d9cd508
Source39:	%{_urlprefix}/kde-i18n/kde-i18n-fr-%{version}.tar.bz2
# Source39-md5:	f700524f68cf6d34770784c69f9cc293
Source40:	%{_urlprefix}/kde-i18n/kde-i18n-fy-%{version}.tar.bz2
# Source40-md5:	f69c07af129e084a4166cdfb3e5db173
Source41:	%{_urlprefix}/kde-i18n/kde-i18n-ga-%{version}.tar.bz2
# Source41-md5:	0ffdca99a102c4e1320916de3bf35adb
Source410:	%{_urlprefix}/kde-i18n/kde-i18n-gl-%{version}.tar.bz2
# Source410-md5:	590bd015071b21ba0dcd55fc2955ca55
Source42:	%{_urlprefix}/kde-i18n/kde-i18n-he-%{version}.tar.bz2
# Source42-md5:	b416073a3503a01056e14107fc797dae
Source43:	%{_urlprefix}/kde-i18n/kde-i18n-hi-%{version}.tar.bz2
# Source43-md5:	25f0b08c99c952f443f32a86d5d4d4ad
Source44:	%{_urlprefix}/kde-i18n/kde-i18n-hr-%{version}.tar.bz2
# Source44-md5:	99a94e8fc1fcdf1837f7030760c3deeb
Source45:	%{_urlprefix}/kde-i18n/kde-i18n-hu-%{version}.tar.bz2
# Source45-md5:	575734a98fa2984f47adb49d6c023cc0
Source46:	%{_urlprefix}/kde-i18n/kde-i18n-is-%{version}.tar.bz2
# Source46-md5:	f41752647ef59cb9fd179e2e1f77738c
Source47:	%{_urlprefix}/kde-i18n/kde-i18n-it-%{version}.tar.bz2
# Source47-md5:	3a9bea48fb5ac7d3703abfdaa8a50c3c
Source48:	%{_urlprefix}/kde-i18n/kde-i18n-ja-%{version}.tar.bz2
# Source48-md5:	79b62e00ae4bbcc0d874588ccba177be
Source480:	%{_urlprefix}/kde-i18n/kde-i18n-lv-%{version}.tar.bz2
# Source480-md5:	c3f7cca71708d2894510bdd30b264bff
Source49:	%{_urlprefix}/kde-i18n/kde-i18n-lt-%{version}.tar.bz2
# Source49-md5:	2769c90376add2e49addcaa2f39df577
Source490:	%{_urlprefix}/kde-i18n/kde-i18n-km-%{version}.tar.bz2
# Source490-md5:	2f83f915e5ee4932ce8c7f26abb8b542
Source491:	%{_urlprefix}/kde-i18n/kde-i18n-ko-%{version}.tar.bz2
# Source491-md5:	eb47d4c6f46c161835c5255f399e1ac9
Source50:	%{_urlprefix}/kde-i18n/kde-i18n-mk-%{version}.tar.bz2
# Source50-md5:	2e374c32eb02a6421b2076ac305926a2
Source500:	%{_urlprefix}/kde-i18n/kde-i18n-mn-%{version}.tar.bz2
# Source500-md5:	7158b53fec42b7ed43525bacfa57e0e4
Source501:	%{_urlprefix}/kde-i18n/kde-i18n-ms-%{version}.tar.bz2
# Source501-md5:	edeaa43311fc0935d0a5b79b5db8f39e
Source51:	%{_urlprefix}/kde-i18n/kde-i18n-nb-%{version}.tar.bz2
# Source51-md5:	bf087b3c116770dcffa008da74e767e2
Source52:	%{_urlprefix}/kde-i18n/kde-i18n-nds-%{version}.tar.bz2
# Source52-md5:	a12623e0d68f3737447b663e070e3f61
Source53:	%{_urlprefix}/kde-i18n/kde-i18n-nl-%{version}.tar.bz2
# Source53-md5:	6f4eea25839984463e70d1c635813a11
Source54:	%{_urlprefix}/kde-i18n/kde-i18n-nn-%{version}.tar.bz2
# Source54-md5:	9dc810b75c2cb7c864ec5bf82a2bed2f
Source55:	%{_urlprefix}/kde-i18n/kde-i18n-pa-%{version}.tar.bz2
# Source55-md5:	6a9be2176930ceb07600913cbee525e3
Source56:	%{_urlprefix}/kde-i18n/kde-i18n-pl-%{version}.tar.bz2
# Source56-md5:	71852ce8f2549cfc19ffe71468a82349
Source57:	%{_urlprefix}/kde-i18n/kde-i18n-pt-%{version}.tar.bz2
# Source57-md5:	ee8322ab521d796fbfafef471d845d6d
Source58:	%{_urlprefix}/kde-i18n/kde-i18n-pt_BR-%{version}.tar.bz2
# Source58-md5:	29836d3d914f41a2cab1567d1df6feff
Source59:	%{_urlprefix}/kde-i18n/kde-i18n-ro-%{version}.tar.bz2
# Source59-md5:	af2fc2dbc745614c7286a430a7874a54
Source60:	%{_urlprefix}/kde-i18n/kde-i18n-ru-%{version}.tar.bz2
# Source60-md5:	348d72dfa83d51cbb65f6c7e964d64b3
Source600:	%{_urlprefix}/kde-i18n/kde-i18n-rw-%{version}.tar.bz2
# Source600-md5:	8d07d207bb2e933a7b0130e593313842
Source61:	%{_urlprefix}/kde-i18n/kde-i18n-se-%{version}.tar.bz2
# Source61-md5:	11d5888678814a442589c995d6307cd8
Source62:	%{_urlprefix}/kde-i18n/kde-i18n-sk-%{version}.tar.bz2
# Source62-md5:	3a7b1b8bd44c92713d5e4db52655915b
Source63:	%{_urlprefix}/kde-i18n/kde-i18n-sl-%{version}.tar.bz2
# Source63-md5:	2064f33c3f76ee60ddf1aef010d92399
Source64:	%{_urlprefix}/kde-i18n/kde-i18n-sr-%{version}.tar.bz2
# Source64-md5:	e38ff9abe6f68bc69e0df5891e7bce69
Source65:	%{_urlprefix}/kde-i18n/kde-i18n-sr@Latn-%{version}.tar.bz2
# Source65-md5:	9dcf67d0837f8ad2448d07c3ba3d5015
Source660:	%{_urlprefix}/kde-i18n/kde-i18n-ss-%{version}.tar.bz2
# Source660-md5:	7ecd86abba7c02c73b248ba5452c4bed
Source66:	%{_urlprefix}/kde-i18n/kde-i18n-sv-%{version}.tar.bz2
# Source66-md5:	a826fb26b9378b12dae31b15ac22d995
Source67:	%{_urlprefix}/kde-i18n/kde-i18n-ta-%{version}.tar.bz2
# Source67-md5:	11da7704ec348481c392cfd47af85caa
Source68:	%{_urlprefix}/kde-i18n/kde-i18n-tg-%{version}.tar.bz2
# Source68-md5:	33f3b735e9cbd8a736146dae8a764d06
Source69:	%{_urlprefix}/kde-i18n/kde-i18n-tr-%{version}.tar.bz2
# Source69-md5:	b56062b9908ecb6909bc4a7e4c4bb62a
Source70:	%{_urlprefix}/kde-i18n/kde-i18n-uk-%{version}.tar.bz2
# Source70-md5:	82f0f3f3567d551307c03ebad12f3a1c
Source700:	%{_urlprefix}/kde-i18n/kde-i18n-uz-%{version}.tar.bz2
# Source700-md5:	2208bb14ae419e20f2179d586ba49ff5
Source71:	%{_urlprefix}/kde-i18n/kde-i18n-zh_CN-%{version}.tar.bz2
# Source71-md5:	a74fb6fee6d36a8bd975bb7b1b97fb4c
Source710:	%{_urlprefix}/kde-i18n/kde-i18n-zh_TW-%{version}.tar.bz2
# Source710-md5:	f6211661d09cf7dcc381147d084537a7
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
