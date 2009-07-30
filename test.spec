# - easy way to update all sources with new/old locales:
#   lynx -dump http://carme.pld-linux.org/~arekm/kde/kde-l10n | awk -vi=19 '/4.1.0.tar.bz2$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   sed -i -e 's,http://carme.pld-linux.org/~arekm/kde/kde-l10n/,%{_urlprefix}/kde-l10n/,' out
#   sed -i -e 's,4.1.0,%{version},' out
#   and then :r out in vim and ./builder -a5 the spec
%bcond_with	l10n
%bcond_with	koffice
%define		_urlprefix	http://carme.pld-linux.org/~arekm/kde/
#%%define		_urlprefix	http://shadzik.nomeno.pl/kde4/unstable
%define		kofficever	1.9.99.0
#%%define		_urlprefix	ftp://ftp.pbone.net/mirror/ftp.kde.org/pub/kde/unstable/%{version}/src
Summary:	Fetch KDE packages to distfiles
Name:		kdefetch
Version:	4.3.0
Release:	1
License:	GPL
Group:		Networking/Hacking
Source100:	kde4diff.sh
Source0:	%{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source0-md5:	76435ce1bf787713effe079a3664d3cd
Source1:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source1-md5:	4712ade616d3c3a987281d24326ee9af
Source2:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source2-md5:	3e7872e841e87f716872086571028a37
Source3:	%{_urlprefix}/kdebase-%{version}.tar.bz2
# Source3-md5:	6de0b96b78504d8f5fcdee819d080fb1
Source4:	%{_urlprefix}/kdebase-runtime-%{version}.tar.bz2
# Source4-md5:	9681d074a26e2affe7c0a75db5139846
Source5:	%{_urlprefix}/kdebase-workspace-%{version}.tar.bz2
# Source5-md5:	fa5c39df1559e47b3176703a5b3e1ab4
Source6:	%{_urlprefix}/kdebindings-%{version}.tar.bz2
# Source6-md5:	1b6cd0a20586eea0161e782be9c16326
Source7:	%{_urlprefix}/kdeedu-%{version}.tar.bz2
# Source7-md5:	4c309bcdc47274cea6f61206a42ef638
Source8:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source8-md5:	9997c1fab82519ebc59e661c4324fa0a
Source9:	%{_urlprefix}/kdegraphics-%{version}.tar.bz2
# Source9-md5:	5d3838a2575a82777f00ced90332c41a
Source10:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source10-md5:	ea54f71bcbb0cf96bb6d94c019de8bb5
Source11:	%{_urlprefix}/kdelibs-experimental-%{version}.tar.bz2
# Source11-md5:	9b3ed689f4f357d4fc059cf9dd41e035
Source12:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source12-md5:	75c0c42f22f5ffc98262441751ccb247
Source13:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source13-md5:	f9695ff06d0d67a78a71fb9b3ddbd4f3
Source14:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source14-md5:	ddc887f19ef9cd454f4f3226c955aaaf
Source15:	%{_urlprefix}/kdepimlibs-%{version}.tar.bz2
# Source15-md5:	313f1a9d353f82c2ffee517115404dd5
Source16:	%{_urlprefix}/kdeplasma-addons-%{version}.tar.bz2
# Source16-md5:	abfbe2d32c444689b5bf4e5346b33c9e
Source17:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source17-md5:	eda2376a54d66899bf7beb60cc0843b1
Source18:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source18-md5:	6975e332bdd1cdf60b8509c544cedb06
Source19:	%{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source19-md5:	9d17d3d7bf25be5af1cbd4abf04e4c99
Source20:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source20-md5:	c050af7fed0b5593433650605df651b2
Source21:	%{_urlprefix}/oxygen-icons-%{version}.tar.bz2
# Source21-md5:	26b63e75f9f198f91a022e5f198119bb
%if %{with l10n}
Source22:	%{_urlprefix}/kde-l10n/kde-l10n-bg-%{version}.tar.bz2
# Source22-md5:	fb0a71d21cf32e48a28916d365b4cd96
Source23:	%{_urlprefix}/kde-l10n/kde-l10n-ca-%{version}.tar.bz2
# Source23-md5:	1f9e2f387083be475ec995c0e965b1cf
Source24:	%{_urlprefix}/kde-l10n/kde-l10n-cs-%{version}.tar.bz2
# Source24-md5:	8d8ec27742416e134b2990abbd9af14b
Source25:	%{_urlprefix}/kde-l10n/kde-l10n-csb-%{version}.tar.bz2
# Source25-md5:	f19c3a3bfae24f4caf98a40f6bed7463
Source26:	%{_urlprefix}/kde-l10n/kde-l10n-da-%{version}.tar.bz2
# Source26-md5:	b81c512af946a1e365c2eada3d82e4e0
Source27:	%{_urlprefix}/kde-l10n/kde-l10n-de-%{version}.tar.bz2
# Source27-md5:	c7ca5df8998b4ae0977bc706db86d89f
Source28:	%{_urlprefix}/kde-l10n/kde-l10n-el-%{version}.tar.bz2
# Source28-md5:	24b9e6117c254a7eb42bb7ac3ee5956e
Source29:	%{_urlprefix}/kde-l10n/kde-l10n-en_GB-%{version}.tar.bz2
# Source29-md5:	1596bbb2848517bba0cf50854de47e89
Source30:	%{_urlprefix}/kde-l10n/kde-l10n-es-%{version}.tar.bz2
# Source30-md5:	34dc196b2395e3a3223346cf2dafde5a
Source31:	%{_urlprefix}/kde-l10n/kde-l10n-et-%{version}.tar.bz2
# Source31-md5:	aeb0683e93853f67c50ba2fcd1e4a41c
Source32:	%{_urlprefix}/kde-l10n/kde-l10n-fi-%{version}.tar.bz2
# Source32-md5:	dc151141386e6e1af9dc2b405dd8a9d9
Source33:	%{_urlprefix}/kde-l10n/kde-l10n-fr-%{version}.tar.bz2
# Source33-md5:	faa1b6b4d9640c9a45f0e86a5af64091
#Source34:	%{_urlprefix}/kde-l10n/kde-l10n-fy-%{version}.tar.bz2
# Source34-md5:	e5046259747f18c9d017f3606eda444c
Source35:	%{_urlprefix}/kde-l10n/kde-l10n-ga-%{version}.tar.bz2
# Source35-md5:	145deb5a130537b5abd8c75c316f88a5
Source36:	%{_urlprefix}/kde-l10n/kde-l10n-gl-%{version}.tar.bz2
# Source36-md5:	fde9f9726edf1ba1a32302ea285a1bf5
Source37:	%{_urlprefix}/kde-l10n/kde-l10n-hi-%{version}.tar.bz2
# Source37-md5:	ad1bd358a3bf4a515e95607edfdde4c9
Source38:	%{_urlprefix}/kde-l10n/kde-l10n-hu-%{version}.tar.bz2
# Source38-md5:	ba442f81bc3ed72710e5ea1c44c2949d
Source39:	%{_urlprefix}/kde-l10n/kde-l10n-it-%{version}.tar.bz2
# Source39-md5:	7974d9d51286c0bbe3ce9201cea05372
Source40:	%{_urlprefix}/kde-l10n/kde-l10n-ja-%{version}.tar.bz2
# Source40-md5:	e0bc5aecab2dab8a32a7a379c3bda98c
Source41:	%{_urlprefix}/kde-l10n/kde-l10n-kk-%{version}.tar.bz2
# Source41-md5:	c007430e5839c943c27d2c08a3271c01
Source42:	%{_urlprefix}/kde-l10n/kde-l10n-km-%{version}.tar.bz2
# Source42-md5:	4cde7eb586388fb3268aecc901c2f297
Source43:	%{_urlprefix}/kde-l10n/kde-l10n-ko-%{version}.tar.bz2
# Source43-md5:	9a10bf30852acd34040c6fa8fcf1bc27
Source44:	%{_urlprefix}/kde-l10n/kde-l10n-ku-%{version}.tar.bz2
# Source44-md5:	80dbde92c9cc2a3b18ddc8f8e6bf6228
Source45:	%{_urlprefix}/kde-l10n/kde-l10n-lt-%{version}.tar.bz2
# Source45-md5:	0f7d011ce2e22f92e7e814445cf6ff97
Source46:	%{_urlprefix}/kde-l10n/kde-l10n-lv-%{version}.tar.bz2
# Source46-md5:	e097c2d2be217ae29cb769504356281c
Source47:	%{_urlprefix}/kde-l10n/kde-l10n-mk-%{version}.tar.bz2
# Source47-md5:	853109465d2dc4031f0cd729775cca55
Source48:	%{_urlprefix}/kde-l10n/kde-l10n-ml-%{version}.tar.bz2
# Source48-md5:	953f5f1d4cbb785cc4d8ef4a488c6661
Source49:	%{_urlprefix}/kde-l10n/kde-l10n-nb-%{version}.tar.bz2
# Source49-md5:	cfe753a7bebfda9f5f6f25399d8dad0c
Source50:	%{_urlprefix}/kde-l10n/kde-l10n-nds-%{version}.tar.bz2
# Source50-md5:	b7b453507e58788503835fec4eddd5a9
Source51:	%{_urlprefix}/kde-l10n/kde-l10n-nl-%{version}.tar.bz2
# Source51-md5:	9118bfb78b280b0228f4f299420f98ea
Source52:	%{_urlprefix}/kde-l10n/kde-l10n-nn-%{version}.tar.bz2
# Source52-md5:	f6863912c5d4d326097e1f995299dbc1
Source53:	%{_urlprefix}/kde-l10n/kde-l10n-pa-%{version}.tar.bz2
# Source53-md5:	a533709989a31c15600ddf9a3e3a7301
Source54:	%{_urlprefix}/kde-l10n/kde-l10n-pl-%{version}.tar.bz2
# Source54-md5:	25fb4028a7bb2000b06363e23efec62d
Source55:	%{_urlprefix}/kde-l10n/kde-l10n-pt-%{version}.tar.bz2
# Source55-md5:	257a995ca6c0adaab8024445dbce848f
Source56:	%{_urlprefix}/kde-l10n/kde-l10n-pt_BR-%{version}.tar.bz2
# Source56-md5:	0020f01a730b5511712a89e13a1d4d76
Source57:	%{_urlprefix}/kde-l10n/kde-l10n-ru-%{version}.tar.bz2
# Source57-md5:	5bc404cea173009d5a817685ca61bcad
Source58:	%{_urlprefix}/kde-l10n/kde-l10n-sl-%{version}.tar.bz2
# Source58-md5:	02117baab6317032245d6ae9f958eb45
Source59:	%{_urlprefix}/kde-l10n/kde-l10n-sk-%{version}.tar.bz2
# Source59-md5:	24945e807ad3703f546a7f6787cb0345
Source60:	%{_urlprefix}/kde-l10n/kde-l10n-sr-%{version}.tar.bz2
# Source60-md5:	26338c314a2a3da58f93e8f606b185c2
Source61:	%{_urlprefix}/kde-l10n/kde-l10n-sv-%{version}.tar.bz2
# Source61-md5:	7499b0fb6ddbb10c2f2e0fb0e88cb097
Source62:	%{_urlprefix}/kde-l10n/kde-l10n-th-%{version}.tar.bz2
# Source62-md5:	2c5dd52012d3e21eaefde4211bee2d1c
Source63:	%{_urlprefix}/kde-l10n/kde-l10n-tr-%{version}.tar.bz2
# Source63-md5:	0d163e01436737a8f4b74d99527997a2
Source64:	%{_urlprefix}/kde-l10n/kde-l10n-uk-%{version}.tar.bz2
# Source64-md5:	43be454febc2f9ca48b66fd5ce057898
Source65:	%{_urlprefix}/kde-l10n/kde-l10n-wa-%{version}.tar.bz2
# Source65-md5:	76bc9dbac978806a7cd73a53fdbe8b69
Source66:	%{_urlprefix}/kde-l10n/kde-l10n-zh_CN-%{version}.tar.bz2
# Source66-md5:	7d0ddb25d6f6e21858b7811bfbd61458
Source67:	%{_urlprefix}/kde-l10n/kde-l10n-zh_TW-%{version}.tar.bz2
# Source67-md5:	ce2a8abf6d8a43a4823ba2e19ad05649
%endif
%if %{with koffice}
Source68:	%{_urlprefix}/koffice-%{kofficever}/koffice-%{kofficever}.tar.bz2
# Source68-md5:	46dcbdda79c6a9aa645d1d473c8d2046
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fetch KDE packages to distfiles

%prep
exit 1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
