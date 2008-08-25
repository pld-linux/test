# - easy way to update all sources with new/old locales:
#   lynx -dump http://carme.pld-linux.org/~arekm/kde/kde-i18n | awk -vi=19 '/3.5.9.tar.bz2$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   sed -i -e 's,http://carme.pld-linux.org/~arekm/kde/kde-i18n/,%{_urlprefix}/kde-i18n/,' out
#   sed -i -e 's,3.5.9,%{version},' out
#   and then :r out in vim and ./builder -a5 the spec
%bcond_with	i18n
%define		_urlprefix	http://carme.pld-linux.org/~arekm/kde/
%define		artsver	1.5.10
%define		kdevelopver 3.5.3
Summary:	Fetch KDE packages to distfiles
Name:		kdefetch
Version:	3.5.10
Release:	1
License:	GPL
Group:		Networking/Hacking
Source0:	%{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source0-md5:	feb1582b9acc573cef8cd357d8a7bc1d
Source1:	%{_urlprefix}/kdeaddons-%{version}.tar.bz2
# Source1-md5:	c69d082407b2c1bb46d078f8ac5d2bea
Source2:	%{_urlprefix}/arts-%{artsver}.tar.bz2
# Source2-md5:	6da172aab2a4a44929b5fdfc30fa3efc
Source3:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source3-md5:	eb23c52c945f31a48f2c9df4330a1262
Source4:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source4-md5:	6e6f089dc0f1dabb0f138641600d0b59
Source5:	%{_urlprefix}/kdebase-%{version}.tar.bz2
# Source5-md5:	88237188271fbf1e6bcd40180a75d953
Source6:	%{_urlprefix}/kdebindings-%{version}.tar.bz2
# Source6-md5:	7d5119160ac3688ac1a63954d03ab4a8
Source7:	%{_urlprefix}/kdeedu-%{version}.tar.bz2
# Source7-md5:	1b1466bf4cb0a59b1abd8613a2588142
Source8:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source8-md5:	5533b3886cbb74180933fe3f3d209031
Source9:	%{_urlprefix}/kdegraphics-%{version}.tar.bz2
# Source9-md5:	a09094b5357d8cd5c49d45b5d291dcfe
Source10:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source10-md5:	43cd55ed15f63b5738d620ef9f9fd568
Source11:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source11-md5:	8e8cd7f41d37f7da8bd239048abf3516
Source12:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source12-md5:	634b2e914661faebae79d95dcc6c5bfa
Source13:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source13-md5:	fc93e458a8eec8131ede56cff30c28b2
Source14:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source14-md5:	ad711d1ce09242bd13b73a9a005f3143
Source15:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source15-md5:	1da4383e2d520dfd572edb33b708822d
Source16:	%{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source16-md5:	038f94275f42df3cae89735506ffbc0b
Source17:	%{_urlprefix}/kdevelop-%{kdevelopver}.tar.bz2
# Source17-md5:	a2cdb5f71952386798175f8ce5a3e196
Source18:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source18-md5:	7188f351158ca5a7613c3de4a6854b37
%if %{with i18n}
Source19:	%{_urlprefix}/kde-i18n/kde-i18n-af-%{version}.tar.bz2
# Source19-md5:	08d05d7ff9f866fce127382d1e73a27d
Source20:	%{_urlprefix}/kde-i18n/kde-i18n-ar-%{version}.tar.bz2
# Source20-md5:	ff3f9b816be41df76dfdfa7dbefadb2f
Source21:	%{_urlprefix}/kde-i18n/kde-i18n-az-%{version}.tar.bz2
# Source21-md5:	72b6743124db7d046f6136cf219022d3
Source22:	%{_urlprefix}/kde-i18n/kde-i18n-be-%{version}.tar.bz2
# Source22-md5:	8b61229e1193f03fe7d54e4cfa909191
Source23:	%{_urlprefix}/kde-i18n/kde-i18n-bg-%{version}.tar.bz2
# Source23-md5:	c3efc49aef6bb21f8fa604e4f300fc73
Source24:	%{_urlprefix}/kde-i18n/kde-i18n-bn-%{version}.tar.bz2
# Source24-md5:	6d49f20c81ffae866559c09976f6b733
Source25:	%{_urlprefix}/kde-i18n/kde-i18n-br-%{version}.tar.bz2
# Source25-md5:	d777f77c14922eaf17e911bbb2bb7b40
Source26:	%{_urlprefix}/kde-i18n/kde-i18n-bs-%{version}.tar.bz2
# Source26-md5:	3605c85c1788230368d19b1a09140cd0
Source27:	%{_urlprefix}/kde-i18n/kde-i18n-ca-%{version}.tar.bz2
# Source27-md5:	7587f2accb4231e0cb68e750e2496f55
Source28:	%{_urlprefix}/kde-i18n/kde-i18n-cs-%{version}.tar.bz2
# Source28-md5:	cc83561a25a53dea5452f0261d94e2cc
Source29:	%{_urlprefix}/kde-i18n/kde-i18n-csb-%{version}.tar.bz2
# Source29-md5:	f0c9154fd0695a22fcc6dd9a6692afc9
Source30:	%{_urlprefix}/kde-i18n/kde-i18n-cy-%{version}.tar.bz2
# Source30-md5:	67eab91e0a0a72681ea684876003a286
Source31:	%{_urlprefix}/kde-i18n/kde-i18n-da-%{version}.tar.bz2
# Source31-md5:	de37394373fef218ffd19f2efbb139b4
Source32:	%{_urlprefix}/kde-i18n/kde-i18n-de-%{version}.tar.bz2
# Source32-md5:	9d24448a403242c64253fcde28d94321
Source33:	%{_urlprefix}/kde-i18n/kde-i18n-el-%{version}.tar.bz2
# Source33-md5:	b46f636e5e89a6a22d65b8ab40c99aa0
Source34:	%{_urlprefix}/kde-i18n/kde-i18n-en_GB-%{version}.tar.bz2
# Source34-md5:	3ac6784dd0b7f24e88de85f0196fc138
Source35:	%{_urlprefix}/kde-i18n/kde-i18n-eo-%{version}.tar.bz2
# Source35-md5:	4c4256af2b07f4ef89ceb8f8fd087a0d
Source36:	%{_urlprefix}/kde-i18n/kde-i18n-es-%{version}.tar.bz2
# Source36-md5:	37b1d4f181dbfab4a2f235657e672eea
Source37:	%{_urlprefix}/kde-i18n/kde-i18n-et-%{version}.tar.bz2
# Source37-md5:	58862bbec128c29db0df33a824813c15
Source38:	%{_urlprefix}/kde-i18n/kde-i18n-eu-%{version}.tar.bz2
# Source38-md5:	222a5f1dd0d5ab6c334468fe5440dc66
Source39:	%{_urlprefix}/kde-i18n/kde-i18n-fa-%{version}.tar.bz2
# Source39-md5:	790b34649838b87444926cb32188a6d5
Source40:	%{_urlprefix}/kde-i18n/kde-i18n-fi-%{version}.tar.bz2
# Source40-md5:	195580d7f80330bf703db2d32c6973ec
Source41:	%{_urlprefix}/kde-i18n/kde-i18n-fr-%{version}.tar.bz2
# Source41-md5:	b92590c756aedd16ee863f307ec20c58
Source42:	%{_urlprefix}/kde-i18n/kde-i18n-fy-%{version}.tar.bz2
# Source42-md5:	abeabb8786293786743c4f513a907bc7
Source43:	%{_urlprefix}/kde-i18n/kde-i18n-ga-%{version}.tar.bz2
# Source43-md5:	b48a11cff0f37de75cf82676e9c63503
Source44:	%{_urlprefix}/kde-i18n/kde-i18n-gl-%{version}.tar.bz2
# Source44-md5:	254953a780dc5f74c1e7107624ce9b3f
Source45:	%{_urlprefix}/kde-i18n/kde-i18n-he-%{version}.tar.bz2
# Source45-md5:	4ba23539fa791d7a9e9b93c6992031a5
Source46:	%{_urlprefix}/kde-i18n/kde-i18n-hi-%{version}.tar.bz2
# Source46-md5:	0d5b52ef04c80034e4148db916a5b8d8
Source47:	%{_urlprefix}/kde-i18n/kde-i18n-hr-%{version}.tar.bz2
# Source47-md5:	50948306543eb3ce4d27e6577955c9d8
Source48:	%{_urlprefix}/kde-i18n/kde-i18n-hu-%{version}.tar.bz2
# Source48-md5:	998409be294212345806483033485c0f
Source49:	%{_urlprefix}/kde-i18n/kde-i18n-is-%{version}.tar.bz2
# Source49-md5:	92cf1c508c3c719d6899e1f56d91cd31
Source50:	%{_urlprefix}/kde-i18n/kde-i18n-it-%{version}.tar.bz2
# Source50-md5:	aa850328a980fbcb4253ff97bd7d0305
Source51:	%{_urlprefix}/kde-i18n/kde-i18n-ja-%{version}.tar.bz2
# Source51-md5:	3417f460b7da4b3538439c3fd91defa5
Source52:	%{_urlprefix}/kde-i18n/kde-i18n-kk-%{version}.tar.bz2
# Source52-md5:	f66034d61514b919f5d27014843b88c9
Source53:	%{_urlprefix}/kde-i18n/kde-i18n-km-%{version}.tar.bz2
# Source53-md5:	f340a35320368600f9c6527166cd11bb
Source54:	%{_urlprefix}/kde-i18n/kde-i18n-ko-%{version}.tar.bz2
# Source54-md5:	910573d994b6236d64f3f13be7211112
Source55:	%{_urlprefix}/kde-i18n/kde-i18n-lt-%{version}.tar.bz2
# Source55-md5:	c12d47a5a9f29a9e2b51d40296d4c8c3
Source56:	%{_urlprefix}/kde-i18n/kde-i18n-lv-%{version}.tar.bz2
# Source56-md5:	2c7f33fa01658d65d824bd14d7b034ce
Source57:	%{_urlprefix}/kde-i18n/kde-i18n-mk-%{version}.tar.bz2
# Source57-md5:	576d665415b25ccf0744755845e80c7a
Source58:	%{_urlprefix}/kde-i18n/kde-i18n-mn-%{version}.tar.bz2
# Source58-md5:	e8e5b3d93bc88332995c8a36b89a82f7
Source59:	%{_urlprefix}/kde-i18n/kde-i18n-ms-%{version}.tar.bz2
# Source59-md5:	0c4009229fe716e66cd1bb0b6b051477
Source60:	%{_urlprefix}/kde-i18n/kde-i18n-nb-%{version}.tar.bz2
# Source60-md5:	d990123fe61f6f15a215c5b189f7f141
Source61:	%{_urlprefix}/kde-i18n/kde-i18n-nds-%{version}.tar.bz2
# Source61-md5:	b30f44fd4f3220ca3ae5165486979891
Source62:	%{_urlprefix}/kde-i18n/kde-i18n-nl-%{version}.tar.bz2
# Source62-md5:	a934c97f18dbb1fcb6d2ad72e3247dd1
Source63:	%{_urlprefix}/kde-i18n/kde-i18n-nn-%{version}.tar.bz2
# Source63-md5:	6e6a432ffc3b8242c29fb3806a61c1d1
Source64:	%{_urlprefix}/kde-i18n/kde-i18n-pa-%{version}.tar.bz2
# Source64-md5:	f87435d069e4adc9c211775359c336ea
Source65:	%{_urlprefix}/kde-i18n/kde-i18n-pl-%{version}.tar.bz2
# Source65-md5:	f32e46ce95dc3c7e150d57ae08de1a55
Source66:	%{_urlprefix}/kde-i18n/kde-i18n-pt-%{version}.tar.bz2
# Source66-md5:	da33de5028e91be24115304b9ec95bb4
Source67:	%{_urlprefix}/kde-i18n/kde-i18n-pt_BR-%{version}.tar.bz2
# Source67-md5:	8f1344d86383337a930d4c69cfcc1c91
Source68:	%{_urlprefix}/kde-i18n/kde-i18n-ro-%{version}.tar.bz2
# Source68-md5:	864955c215254a4cb2675c7c1631a8c8
Source69:	%{_urlprefix}/kde-i18n/kde-i18n-ru-%{version}.tar.bz2
# Source69-md5:	0e76918a045a4792c86216bdc6dccaf4
Source70:	%{_urlprefix}/kde-i18n/kde-i18n-rw-%{version}.tar.bz2
# Source70-md5:	c3569c1115edf40e0b51b2670b441000
Source71:	%{_urlprefix}/kde-i18n/kde-i18n-se-%{version}.tar.bz2
# Source71-md5:	05f86c78e91e777b707bcae123e2a2b8
Source72:	%{_urlprefix}/kde-i18n/kde-i18n-sk-%{version}.tar.bz2
# Source72-md5:	0b012bc94d7a374e6fad26b66815eb16
Source73:	%{_urlprefix}/kde-i18n/kde-i18n-sl-%{version}.tar.bz2
# Source73-md5:	dc1a128d27c5cf76de1a98ea80928884
Source74:	%{_urlprefix}/kde-i18n/kde-i18n-sr-%{version}.tar.bz2
# Source74-md5:	5df0699edb6e7ab7243648838fca3e13
Source75:	%{_urlprefix}/kde-i18n/kde-i18n-sr@Latn-%{version}.tar.bz2
# Source75-md5:	b2d9d83c77fd32c3f321515e840770d6
Source76:	%{_urlprefix}/kde-i18n/kde-i18n-ss-%{version}.tar.bz2
# Source76-md5:	d3d95a17a66f8414c16d3095aa7f7829
Source77:	%{_urlprefix}/kde-i18n/kde-i18n-sv-%{version}.tar.bz2
# Source77-md5:	0769547c21b2b82e01e430826002abdd
Source78:	%{_urlprefix}/kde-i18n/kde-i18n-ta-%{version}.tar.bz2
# Source78-md5:	040cecbcc246733cbb692099138a278b
Source79:	%{_urlprefix}/kde-i18n/kde-i18n-te-%{version}.tar.bz2
# Source79-md5:	726acc373482e8fa97e468f23e4f5619
Source80:	%{_urlprefix}/kde-i18n/kde-i18n-tg-%{version}.tar.bz2
# Source80-md5:	7999d00f85d0a9bf2991ab8600ce23c1
Source81:	%{_urlprefix}/kde-i18n/kde-i18n-th-%{version}.tar.bz2
# Source81-md5:	9a2b03bc371ec00e62a92a30bec2abf9
Source82:	%{_urlprefix}/kde-i18n/kde-i18n-tr-%{version}.tar.bz2
# Source82-md5:	a043c8e13c699be9b60f0d56833162a8
Source83:	%{_urlprefix}/kde-i18n/kde-i18n-uk-%{version}.tar.bz2
# Source83-md5:	c4bb322541cbba9dad22da3c588ba639
Source84:	%{_urlprefix}/kde-i18n/kde-i18n-uz-%{version}.tar.bz2
# Source84-md5:	9c4aca3db425032d85016aa23e9a3b92
Source85:	%{_urlprefix}/kde-i18n/kde-i18n-vi-%{version}.tar.bz2
# Source85-md5:	78c9313e33f5122cdd576d70be360c3c
Source86:	%{_urlprefix}/kde-i18n/kde-i18n-wa-%{version}.tar.bz2
# Source86-md5:	b7bc216e665e1612e47874aea6628af3
Source87:	%{_urlprefix}/kde-i18n/kde-i18n-zh_CN-%{version}.tar.bz2
# Source87-md5:	65ac47c0c1d2424158e416dfa878cc26
Source88:	%{_urlprefix}/kde-i18n/kde-i18n-zh_TW-%{version}.tar.bz2
# Source88-md5:	c9b7fc28f62fc43f57c0d75535860be6
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
