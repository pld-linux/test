# - easy way to update all sources with new/old locales:
#   lynx -dump http://carme.pld-linux.org/~arekm/kde/kde-l10n | awk -vi=19 '/4.1.0.tar.xz$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   sed -i -e 's,http://carme.pld-linux.org/~arekm/kde/kde-l10n/,%{_urlprefix}/kde-l10n/kde-l10n/,' out
#   sed -i -e 's,4.1.0,%{version},' out
#   and then :r out in vim and ./builder -a5 the spec
%bcond_with	l10n
%bcond_with	koffice
%define		_urlprefix	http://ixion.pld-linux.org/~arekm/kde/
#%%define		_urlprefix	http://shadzik.nomeno.pl/kde4/
%define		kofficever	2.3.1
#%%define		_urlprefix	ftp://ftp.pbone.net/mirror/ftp.kde.org/pub/kde/unstable/%{version}/src
Summary:	Fetch KDE packages to distfiles
Name:		kdefetch
Version:	4.8.3
Release:	1
License:	GPL
Group:		Networking/Hacking
Source100:	kde4diff.sh
# Source100-md5:	e335c913f721664dc383542367cdcbf2
Source0:	%{_urlprefix}/analitza-%{version}.tar.xz
# Source0-md5:	c703386e425d86575afda9e2b2ea320a
Source1:	%{_urlprefix}/ark-%{version}.tar.xz
# Source1-md5:	d6f6a3665cac5e9f4ce7999582e3f612
Source2:	%{_urlprefix}/blinken-%{version}.tar.xz
# Source2-md5:	3bd07db4948ae9fef6340eb069c0c4df
Source3:	%{_urlprefix}/cantor-%{version}.tar.xz
# Source3-md5:	00d89ea1a8d6c8660f480e0efd571d7a
Source4:	%{_urlprefix}/filelight-%{version}.tar.xz
# Source4-md5:	f96153da427141e075f744eb66659f3f
Source5:	%{_urlprefix}/gwenview-%{version}.tar.xz
# Source5-md5:	5c1eae6507a9c0e2924caa2180377e42
Source6:	%{_urlprefix}/jovie-%{version}.tar.xz
# Source6-md5:	d1aed227fa690ea8dbd0fe9fdf8f05b2
Source7:	%{_urlprefix}/kaccessible-%{version}.tar.xz
# Source7-md5:	467ba9bb4b2d72de49bb40f68e6e453f
Source8:	%{_urlprefix}/kactivities-%{version}.tar.xz
# Source8-md5:	9d7e66a832770558ad8641a8667e89ed
Source9:	%{_urlprefix}/kalgebra-%{version}.tar.xz
# Source9-md5:	41b6a5bdccee663e55cd5b1aa35714c8
Source10:	%{_urlprefix}/kalzium-%{version}.tar.xz
# Source10-md5:	cbcf683f2ccdca7d829a0d1bff77e92b
Source11:	%{_urlprefix}/kamera-%{version}.tar.xz
# Source11-md5:	4cdb633dad08d770ca1a5fe1b2bdbf20
Source12:	%{_urlprefix}/kanagram-%{version}.tar.xz
# Source12-md5:	6aa9083c843c52cecbbecc24a0b4a9da
Source13:	%{_urlprefix}/kate-%{version}.tar.xz
# Source13-md5:	e109cc4f76dd0128349999e4713f31dc
Source14:	%{_urlprefix}/kbruch-%{version}.tar.xz
# Source14-md5:	dfb4827073214bd5da0d93bb5bec9ab4
Source15:	%{_urlprefix}/kcalc-%{version}.tar.xz
# Source15-md5:	b996f77c1870fc521cd5737c7e6d0d02
Source16:	%{_urlprefix}/kcharselect-%{version}.tar.xz
# Source16-md5:	e2ece085b66f7b4e21e261d3ef17ec62
Source17:	%{_urlprefix}/kcolorchooser-%{version}.tar.xz
# Source17-md5:	22cb3b15b2b5740fec83b505fc29f5a0
Source18:	%{_urlprefix}/kde-baseapps-%{version}.tar.xz
# Source18-md5:	c0a92dd1c23af86e07e2541f4a8bc07e
Source19:	%{_urlprefix}/kde-l10n
# Source19-md5:	40ff7f8eb50b837f871140280f3f5634
Source20:	%{_urlprefix}/kde-runtime-%{version}.tar.xz
# Source20-md5:	aa22e3d4166e8cd0f149ac5dd5989301
Source21:	%{_urlprefix}/kde-wallpapers-%{version}.tar.xz
# Source21-md5:	87e16f37104f13692d7f9c547d82ae9f
Source22:	%{_urlprefix}/kde-workspace-%{version}.tar.xz
# Source22-md5:	615a05d12337a0cba749951891e60513
Source23:	%{_urlprefix}/kdeadmin-%{version}.tar.xz
# Source23-md5:	e91742cf1c77b7c799f2b1d974088a1d
Source24:	%{_urlprefix}/kdeartwork-%{version}.tar.xz
# Source24-md5:	41d4a060f7790bdf38c043a52107896e
Source25:	%{_urlprefix}/kdegames-%{version}.tar.xz
# Source25-md5:	560425f54a2648875a1c48274fafeaeb
Source26:	%{_urlprefix}/kdegraphics-mobipocket-%{version}.tar.xz
# Source26-md5:	c784c6ead5718c87a09e1fde19896c49
Source27:	%{_urlprefix}/kdegraphics-strigi-analyzer-%{version}.tar.xz
# Source27-md5:	e1f68ee8e938b64cdfdca1f294f41f85
Source28:	%{_urlprefix}/kdegraphics-thumbnailers-%{version}.tar.xz
# Source28-md5:	33a89ef997743ad115340ff7aee12612
Source29:	%{_urlprefix}/kdelibs-%{version}.tar.xz
# Source29-md5:	c4987c838164bd9ee2787e77243fe4a9
Source30:	%{_urlprefix}/kdemultimedia-%{version}.tar.xz
# Source30-md5:	d31072ec8fafef89dc469bf6c09ba836
Source31:	%{_urlprefix}/kdenetwork-%{version}.tar.xz
# Source31-md5:	f6749a63de31ed16725bb71bd0eafaca
Source32:	%{_urlprefix}/kdepim-%{version}.tar.xz
# Source32-md5:	31446093aa268efc0e71f0b9b8753fac
Source33:	%{_urlprefix}/kdepim-runtime-%{version}.tar.xz
# Source33-md5:	3aab404f1a51f5f77581ddc93895dd9d
Source34:	%{_urlprefix}/kdepimlibs-%{version}.tar.xz
# Source34-md5:	30c54a75ea9654f13f96174087ab6fc3
Source35:	%{_urlprefix}/kdeplasma-addons-%{version}.tar.xz
# Source35-md5:	6da9a63dd71c39d7650ae3c07b06d969
Source36:	%{_urlprefix}/kdesdk-%{version}.tar.xz
# Source36-md5:	1b8b8f1639fd0153cf75eb80c575df2a
Source37:	%{_urlprefix}/kdetoys-%{version}.tar.xz
# Source37-md5:	625513eb35bd52e27303ded1ff5d4ffd
Source38:	%{_urlprefix}/kdewebdev-%{version}.tar.xz
# Source38-md5:	efe4b85e5df9c9aa09468ea0acb4b9e5
Source39:	%{_urlprefix}/kdf-%{version}.tar.xz
# Source39-md5:	e62f7820593ff087513caf7259567951
Source40:	%{_urlprefix}/kfloppy-%{version}.tar.xz
# Source40-md5:	acc2da0e55e32042411633f8fc071874
Source41:	%{_urlprefix}/kgamma-%{version}.tar.xz
# Source41-md5:	c96049f4bd867dbde72e852994f17a16
Source42:	%{_urlprefix}/kgeography-%{version}.tar.xz
# Source42-md5:	46622d6ede43a5365481822bb9372f37
Source43:	%{_urlprefix}/kgpg-%{version}.tar.xz
# Source43-md5:	ac97a81cfb679b5f496b380655d74805
Source44:	%{_urlprefix}/khangman-%{version}.tar.xz
# Source44-md5:	01d97ddf426e33b27d4e4b351335de14
Source45:	%{_urlprefix}/kig-%{version}.tar.xz
# Source45-md5:	b3b598b14deb78f26de55c7d5d7c74f5
Source46:	%{_urlprefix}/kimono-%{version}.tar.xz
# Source46-md5:	5c886e6703ddd4bdfe7c32027a547fd3
Source47:	%{_urlprefix}/kiten-%{version}.tar.xz
# Source47-md5:	5f486c82dd45cda738566f9a9ff03a83
Source48:	%{_urlprefix}/klettres-%{version}.tar.xz
# Source48-md5:	2413bf4a0b74c219310a64b7c513e9bd
Source49:	%{_urlprefix}/kmag-%{version}.tar.xz
# Source49-md5:	d9c2846883dd42dc9c4da163757e561c
Source50:	%{_urlprefix}/kmousetool-%{version}.tar.xz
# Source50-md5:	239e2a9ef8799ee897ad9a7443f7d1a6
Source51:	%{_urlprefix}/kmouth-%{version}.tar.xz
# Source51-md5:	6e3703c1fc8adfeff478dc3dec035ea2
Source52:	%{_urlprefix}/kmplot-%{version}.tar.xz
# Source52-md5:	ad3d17383e21c72f9a9b940f78843551
Source53:	%{_urlprefix}/kolourpaint-%{version}.tar.xz
# Source53-md5:	cc350f848c8a1fa246293dec956e6144
Source54:	%{_urlprefix}/konsole-%{version}.tar.xz
# Source54-md5:	980afa132c7c1b89a08ecc6c70a98ad5
Source55:	%{_urlprefix}/korundum-%{version}.tar.xz
# Source55-md5:	e2c560bf41412c70be5f3e73a8c196df
Source56:	%{_urlprefix}/kremotecontrol-%{version}.tar.xz
# Source56-md5:	08a2a33c3e52f3d7d8534abb95219691
Source57:	%{_urlprefix}/kross-interpreters-%{version}.tar.xz
# Source57-md5:	afa46a7fc22639affae2de05e26b9264
Source58:	%{_urlprefix}/kruler-%{version}.tar.xz
# Source58-md5:	e91b5afb11a04c304afc6702ec23b0b6
Source59:	%{_urlprefix}/ksaneplugin-%{version}.tar.xz
# Source59-md5:	4de85592417646d46249ce7863685a2a
Source60:	%{_urlprefix}/ksecrets-%{version}.tar.xz
# Source60-md5:	25c494f5f8c6658b526ed1c245f6c903
Source61:	%{_urlprefix}/ksnapshot-%{version}.tar.xz
# Source61-md5:	af66f517179851c4bed3a8eaf99c0b95
Source62:	%{_urlprefix}/kstars-%{version}.tar.xz
# Source62-md5:	41f4a3d414e6f3ef6d1558287e10f48e
Source63:	%{_urlprefix}/ktimer-%{version}.tar.xz
# Source63-md5:	eae5a1ddfb76c1d5e6f12a2308be2165
Source64:	%{_urlprefix}/ktouch-%{version}.tar.xz
# Source64-md5:	414062bc9e2296e5c559c632157dba37
Source65:	%{_urlprefix}/kturtle-%{version}.tar.xz
# Source65-md5:	56642c41b62ab0523288a12ffacd6dbc
Source66:	%{_urlprefix}/kwallet-%{version}.tar.xz
# Source66-md5:	c020ded4c04cb4a44fb698b954c41e68
Source67:	%{_urlprefix}/kwordquiz-%{version}.tar.xz
# Source67-md5:	139756c02b45b1e58ef6e8c6185a7638
Source68:	%{_urlprefix}/libkdcraw-%{version}.tar.xz
# Source68-md5:	4428df0eb23ff4ed1510951a6ee538e2
Source69:	%{_urlprefix}/libkdeedu-%{version}.tar.xz
# Source69-md5:	24f334dd370bc0f5dedf4c0c919c9ea2
Source70:	%{_urlprefix}/libkexiv2-%{version}.tar.xz
# Source70-md5:	974e93e6693fc0367360281f650a91e4
Source71:	%{_urlprefix}/libkipi-%{version}.tar.xz
# Source71-md5:	43890419ff7432df44a69e4ac1399fbf
Source72:	%{_urlprefix}/libksane-%{version}.tar.xz
# Source72-md5:	dd91b30a1f4d7bcf93b2d60ecaf18711
Source73:	%{_urlprefix}/marble-%{version}.tar.xz
# Source73-md5:	4e9b84a0d29dc5734bc7f11e5855e16e
Source74:	%{_urlprefix}/okular-%{version}.tar.xz
# Source74-md5:	4fa7a3edae4197cb93eb80653f184a26
Source75:	%{_urlprefix}/oxygen-icons-%{version}.tar.xz
# Source75-md5:	cb41c615f3419f2560e92dae85e8ee04
Source76:	%{_urlprefix}/parley-%{version}.tar.xz
# Source76-md5:	b4e1ee0f4788ad17d6606f32a818fca2
Source77:	%{_urlprefix}/perlkde-%{version}.tar.xz
# Source77-md5:	944b263e9a9ff03fb6edccf6960e8e38
Source78:	%{_urlprefix}/perlqt-%{version}.tar.xz
# Source78-md5:	90312c9feb38020f1e3d18d9b7ca53f6
Source79:	%{_urlprefix}/printer-applet-%{version}.tar.xz
# Source79-md5:	2ce2743cf2f1499876b2ad536fa6aa4f
Source80:	%{_urlprefix}/pykde4-%{version}.tar.xz
# Source80-md5:	e0e5e5aaa9f218662dfef5cc269acebc
Source81:	%{_urlprefix}/qtruby-%{version}.tar.xz
# Source81-md5:	78208068121837e7b39fa0f383b14b54
Source82:	%{_urlprefix}/qyoto-%{version}.tar.xz
# Source82-md5:	b847fd81fcdf6b3eacbe87e6a24dd7e5
Source83:	%{_urlprefix}/rocs-%{version}.tar.xz
# Source83-md5:	af9213c71f2777fb3954aa872c9eee32
Source84:	%{_urlprefix}/smokegen-%{version}.tar.xz
# Source84-md5:	77e82ab1a7ce2bf934199b5c5f6aaed9
Source85:	%{_urlprefix}/smokekde-%{version}.tar.xz
# Source85-md5:	ba49d79b9ab8b1c7bc6d86882c91dfc5
Source86:	%{_urlprefix}/smokeqt-%{version}.tar.xz
# Source86-md5:	63b8882fe70a375a05a199eacb412e92
Source87:	%{_urlprefix}/step-%{version}.tar.xz
# Source87-md5:	88f2c2ee6c6cd2a8ab739874615563e5
Source88:	%{_urlprefix}/superkaramba-%{version}.tar.xz
# Source88-md5:	33cbadd26e137ec5c1910886fdbd67ff
Source89:	%{_urlprefix}/svgpart-%{version}.tar.xz
# Source89-md5:	b5731be2f089faa608bdf6f678d02a66
Source90:	%{_urlprefix}/sweeper-%{version}.tar.xz
# Source90-md5:	5bbb6f9b1f753cc3ba0209c63eb80b22
%if %{with l10n}
Source101: %{_urlprefix}/kde-l10n/kde-l10n-ar-%{version}.tar.xz
# Source101-md5:	cb72c26d0ff82e4108baca199ccbf352
Source102: %{_urlprefix}/kde-l10n/kde-l10n-bg-%{version}.tar.xz
# Source102-md5:	444cf101b29d67aa5e31b24fc461fa37
Source103: %{_urlprefix}/kde-l10n/kde-l10n-bs-%{version}.tar.xz
# Source103-md5:	4d6ee2d71e4d1a8c376b6fee9001b657
Source104: %{_urlprefix}/kde-l10n/kde-l10n-ca-%{version}.tar.xz
# Source104-md5:	593c8f4ed1711b835cef1ff05bdb96e4
Source105: %{_urlprefix}/kde-l10n/kde-l10n-ca@valencia-%{version}.tar.xz
# Source105-md5:	b2e41f762e5eded4665e5e6b938d3c49
Source106: %{_urlprefix}/kde-l10n/kde-l10n-cs-%{version}.tar.xz
# Source106-md5:	63409a91f972b17395f65ddc56b3975e
Source107: %{_urlprefix}/kde-l10n/kde-l10n-da-%{version}.tar.xz
# Source107-md5:	197e756a5b0adbbe408e6bd6e33b4a65
Source108: %{_urlprefix}/kde-l10n/kde-l10n-de-%{version}.tar.xz
# Source108-md5:	40757d343ba1cd8f970269a2b3e6dbc4
Source109: %{_urlprefix}/kde-l10n/kde-l10n-el-%{version}.tar.xz
# Source109-md5:	9650c82678c42d64227c3d4e334f92bf
Source110: %{_urlprefix}/kde-l10n/kde-l10n-en_GB-%{version}.tar.xz
# Source110-md5:	9fa6a2d89df599a61529c5d546f3ac3e
Source111: %{_urlprefix}/kde-l10n/kde-l10n-es-%{version}.tar.xz
# Source111-md5:	63d6236f1248381efc7aabf760527592
Source112: %{_urlprefix}/kde-l10n/kde-l10n-et-%{version}.tar.xz
# Source112-md5:	91221ea64c5e0179f502d168b49120e5
Source113: %{_urlprefix}/kde-l10n/kde-l10n-eu-%{version}.tar.xz
# Source113-md5:	a2f47fbe6d7124a15eed02f7bf0ca62c
Source114: %{_urlprefix}/kde-l10n/kde-l10n-fa-%{version}.tar.xz
# Source114-md5:	2f47b456abc330500830cd49eeeb19de
Source115: %{_urlprefix}/kde-l10n/kde-l10n-fi-%{version}.tar.xz
# Source115-md5:	040ea7cc043497e40870a671cd89c745
Source116: %{_urlprefix}/kde-l10n/kde-l10n-fr-%{version}.tar.xz
# Source116-md5:	9622f192ed9c5ba2d9a443aa1f8b4e8c
Source117: %{_urlprefix}/kde-l10n/kde-l10n-ga-%{version}.tar.xz
# Source117-md5:	951ba6041c84410e548e42e66090b8e4
Source118: %{_urlprefix}/kde-l10n/kde-l10n-gl-%{version}.tar.xz
# Source118-md5:	d516896405a60eddc5d96d7f0805cbd2
Source119: %{_urlprefix}/kde-l10n/kde-l10n-hr-%{version}.tar.xz
# Source119-md5:	deb45a9c45a676c1db68278abacc693c
Source120: %{_urlprefix}/kde-l10n/kde-l10n-hu-%{version}.tar.xz
# Source120-md5:	114757cb10064ad0c2cbe700846e9dfd
Source121: %{_urlprefix}/kde-l10n/kde-l10n-ia-%{version}.tar.xz
# Source121-md5:	f7bc69c38ab493d658b82c282c4b94da
Source122: %{_urlprefix}/kde-l10n/kde-l10n-is-%{version}.tar.xz
# Source122-md5:	8b66fe8d80da2f88c83b46b2650cabd2
Source123: %{_urlprefix}/kde-l10n/kde-l10n-it-%{version}.tar.xz
# Source123-md5:	361b387a5097ba28d7b953223a5d8bf2
Source124: %{_urlprefix}/kde-l10n/kde-l10n-ja-%{version}.tar.xz
# Source124-md5:	d7a3e8745edaf0ff53840f0e9a675276
Source125: %{_urlprefix}/kde-l10n/kde-l10n-kk-%{version}.tar.xz
# Source125-md5:	4d40e81ebc206e93674ca9f6d1e28a85
Source126: %{_urlprefix}/kde-l10n/kde-l10n-km-%{version}.tar.xz
# Source126-md5:	9aa9d18edaf56e14f1da1a4174af3e94
Source127: %{_urlprefix}/kde-l10n/kde-l10n-ko-%{version}.tar.xz
# Source127-md5:	150d74cf3c362f86bfe71dfbe93c2e5c
Source128: %{_urlprefix}/kde-l10n/kde-l10n-lt-%{version}.tar.xz
# Source128-md5:	0eb4766e7d889a04477923849d70672c
Source129: %{_urlprefix}/kde-l10n/kde-l10n-lv-%{version}.tar.xz
# Source129-md5:	82d2fa38bfd7881c62fc322a356d1ad7
Source130: %{_urlprefix}/kde-l10n/kde-l10n-nb-%{version}.tar.xz
# Source130-md5:	c2604ab7ff5836fac92e5cee32e2bd34
Source131: %{_urlprefix}/kde-l10n/kde-l10n-nds-%{version}.tar.xz
# Source131-md5:	9ad58e93d7cab5143c5b38552761872a
Source132: %{_urlprefix}/kde-l10n/kde-l10n-nl-%{version}.tar.xz
# Source132-md5:	5af091207c22fc2067f8c01ea2e73a83
Source133: %{_urlprefix}/kde-l10n/kde-l10n-nn-%{version}.tar.xz
# Source133-md5:	c10f503268e3af2e45f37a7ec118f2b5
Source134: %{_urlprefix}/kde-l10n/kde-l10n-pa-%{version}.tar.xz
# Source134-md5:	807ef73aa1adfff8a76e1606488ee4c1
Source135: %{_urlprefix}/kde-l10n/kde-l10n-pl-%{version}.tar.xz
# Source135-md5:	a18bace9aba83b6ed7fe5098d58ec432
Source136: %{_urlprefix}/kde-l10n/kde-l10n-pt-%{version}.tar.xz
# Source136-md5:	d1fefca711d9c4a6223ef064e3fe6863
Source137: %{_urlprefix}/kde-l10n/kde-l10n-pt_BR-%{version}.tar.xz
# Source137-md5:	bd8902518cee0bf495eefb639f2ce917
Source138: %{_urlprefix}/kde-l10n/kde-l10n-ro-%{version}.tar.xz
# Source138-md5:	f364f7fb651adbb38074157f8f5b9a29
Source139: %{_urlprefix}/kde-l10n/kde-l10n-ru-%{version}.tar.xz
# Source139-md5:	573b521bff8ecd190dada43896f303fd
Source140: %{_urlprefix}/kde-l10n/kde-l10n-si-%{version}.tar.xz
# Source140-md5:	6c91269a2b1a8a50c1e1b156ff810940
Source141: %{_urlprefix}/kde-l10n/kde-l10n-sk-%{version}.tar.xz
# Source141-md5:	09cbff28ab4cf4e6f372e8beaccedbbc
Source142: %{_urlprefix}/kde-l10n/kde-l10n-sl-%{version}.tar.xz
# Source142-md5:	25c298e08a0ba243d1fe28291b2710da
Source143: %{_urlprefix}/kde-l10n/kde-l10n-sr-%{version}.tar.xz
# Source143-md5:	477a0d3f83236a161599a05fc5e9c3ce
Source144: %{_urlprefix}/kde-l10n/kde-l10n-sv-%{version}.tar.xz
# Source144-md5:	9a6eda1899f8d360ea2c516cdd9064bd
Source145: %{_urlprefix}/kde-l10n/kde-l10n-tg-%{version}.tar.xz
# Source145-md5:	a6bc0c05ce3b43739c101c90c2cc7118
Source146: %{_urlprefix}/kde-l10n/kde-l10n-th-%{version}.tar.xz
# Source146-md5:	239ba62415227672ebe1ab94a9c6131d
Source147: %{_urlprefix}/kde-l10n/kde-l10n-tr-%{version}.tar.xz
# Source147-md5:	79e16f18b663027f07da5dc5169f4b03
Source148: %{_urlprefix}/kde-l10n/kde-l10n-uk-%{version}.tar.xz
# Source148-md5:	c903e464e8f6b3f827bec6a02ba80021
Source149: %{_urlprefix}/kde-l10n/kde-l10n-vi-%{version}.tar.xz
# Source149-md5:	1ccbc1c0a0cd1fa842bbc3c053d30e73
Source150: %{_urlprefix}/kde-l10n/kde-l10n-wa-%{version}.tar.xz
# Source150-md5:	0f14da93048931321a1aeacd986e2532
Source151: %{_urlprefix}/kde-l10n/kde-l10n-zh_CN-%{version}.tar.xz
# Source151-md5:	dcd564a16fe58028ec533de9cad8e7c9
Source152: %{_urlprefix}/kde-l10n/kde-l10n-zh_TW-%{version}.tar.xz
# Source152-md5:	207eeeb69b0042bef9114f42d1628014
%endif
%if %{with koffice}
Source68:	%{_urlprefix}/koffice-%{kofficever}/koffice-%{kofficever}.tar.bz2
# Source68-md5:	4428df0eb23ff4ed1510951a6ee538e2
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
