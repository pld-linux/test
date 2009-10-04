# - easy way to update all sources with new/old locales:
#   lynx -dump http://carme.pld-linux.org/~arekm/kde/kde-l10n | awk -vi=19 '/4.1.0.tar.bz2$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   sed -i -e 's,http://carme.pld-linux.org/~arekm/kde/kde-l10n/,%{_urlprefix}/kde-l10n/,' out
#   sed -i -e 's,4.1.0,%{version},' out
#   and then :r out in vim and ./builder -a5 the spec
%bcond_with	l10n
%bcond_with	koffice
#%define		_urlprefix	http://carme.pld-linux.org/~arekm/kde/
%define		_urlprefix	http://shadzik.nomeno.pl/kde4/
%define		kofficever	1.9.99.0
#%%define		_urlprefix	ftp://ftp.pbone.net/mirror/ftp.kde.org/pub/kde/unstable/%{version}/src
Summary:	Fetch KDE packages to distfiles
Name:		kdefetch
Version:	4.3.2
Release:	1
License:	GPL
Group:		Networking/Hacking
Source100:	kde4diff.sh
Source0:	%{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source0-md5:	52ab06324f1d47ce5d14638e74b206ed
Source1:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source1-md5:	f547b55cf912f1437ebd2fd7e5059fe4
Source2:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source2-md5:	e4e51be6fe0eaf1290604884a64d28a3
Source3:	%{_urlprefix}/kdebase-%{version}.tar.bz2
# Source3-md5:	7d6b968d8d8dd3730522389dabbb23e2
Source4:	%{_urlprefix}/kdebase-runtime-%{version}.tar.bz2
# Source4-md5:	b0dfe65bc6d18c259c236889f92e2817
Source5:	%{_urlprefix}/kdebase-workspace-%{version}.tar.bz2
# Source5-md5:	2966168f421b3093a119a7c7089b87fb
Source6:	%{_urlprefix}/kdebindings-%{version}.tar.bz2
# Source6-md5:	3187ea9d9913edf4c25ba299dab0d117
Source7:	%{_urlprefix}/kdeedu-%{version}.tar.bz2
# Source7-md5:	d96d87627471d5b34ccfbb44a5fa50f8
Source8:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source8-md5:	7ddf38fb2aa84bd14d176d5a9f45ed3f
Source9:	%{_urlprefix}/kdegraphics-%{version}.tar.bz2
# Source9-md5:	a364a8c0f5ab0c0d41088c92890e6adb
Source10:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source10-md5:	0564ed8ba804a0f3f1cee9732a3d2d72
Source11:	%{_urlprefix}/kdelibs-experimental-%{version}.tar.bz2
# Source11-md5:	d473afb133b5b7d3ead9699c17fe6761
Source12:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source12-md5:	c32305e0d17198387a495e75f3d844ac
Source13:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source13-md5:	57b44a9b59c35366a0c287c591bb9bdc
Source14:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source14-md5:	7e6a672bd681b2f19502798d7ed73fe8
Source15:	%{_urlprefix}/kdepim-runtime-%{version}.tar.bz2
# Source15-md5:	a998b2d6e62e79a80fefc2b3c632a3b8
Source16:	%{_urlprefix}/kdepimlibs-%{version}.tar.bz2
# Source16-md5:	5206959536c1a7abd58f6d2b6eb1c952
Source17:	%{_urlprefix}/kdeplasma-addons-%{version}.tar.bz2
# Source17-md5:	ef545d02cc484d226dc6a580be11a370
Source18:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source18-md5:	326da443b4fed01141f7954464678de2
Source19:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source19-md5:	a4496c504940f076997e553f257e4b3d
Source20:	%{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source20-md5:	b5e72292ed1504f8ee5a82a388af3b04
Source21:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source21-md5:	23af90f4d5977531ca8eca5f297d54b9
Source22:	%{_urlprefix}/oxygen-icons-%{version}.tar.bz2
# Source22-md5:	6f5b700a65720f44d895a10049bbc05c
%if %{with l10n}
Source23:	%{_urlprefix}/kde-l10n/kde-l10n-bg-%{version}.tar.bz2
# Source23-md5:	fb0a71d21cf32e48a28916d365b4cd96
Source24:	%{_urlprefix}/kde-l10n/kde-l10n-ca-%{version}.tar.bz2
# Source24-md5:	1f9e2f387083be475ec995c0e965b1cf
Source25:	%{_urlprefix}/kde-l10n/kde-l10n-cs-%{version}.tar.bz2
# Source25-md5:	8d8ec27742416e134b2990abbd9af14b
Source26:	%{_urlprefix}/kde-l10n/kde-l10n-csb-%{version}.tar.bz2
# Source26-md5:	f19c3a3bfae24f4caf98a40f6bed7463
Source27:	%{_urlprefix}/kde-l10n/kde-l10n-da-%{version}.tar.bz2
# Source27-md5:	b81c512af946a1e365c2eada3d82e4e0
Source28:	%{_urlprefix}/kde-l10n/kde-l10n-de-%{version}.tar.bz2
# Source28-md5:	c7ca5df8998b4ae0977bc706db86d89f
Source29:	%{_urlprefix}/kde-l10n/kde-l10n-el-%{version}.tar.bz2
# Source29-md5:	24b9e6117c254a7eb42bb7ac3ee5956e
Source30:	%{_urlprefix}/kde-l10n/kde-l10n-en_GB-%{version}.tar.bz2
# Source30-md5:	1596bbb2848517bba0cf50854de47e89
Source31:	%{_urlprefix}/kde-l10n/kde-l10n-es-%{version}.tar.bz2
# Source31-md5:	34dc196b2395e3a3223346cf2dafde5a
Source32:	%{_urlprefix}/kde-l10n/kde-l10n-et-%{version}.tar.bz2
# Source32-md5:	aeb0683e93853f67c50ba2fcd1e4a41c
Source33:	%{_urlprefix}/kde-l10n/kde-l10n-fi-%{version}.tar.bz2
# Source33-md5:	dc151141386e6e1af9dc2b405dd8a9d9
Source34:	%{_urlprefix}/kde-l10n/kde-l10n-fr-%{version}.tar.bz2
# Source34-md5:	faa1b6b4d9640c9a45f0e86a5af64091
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
