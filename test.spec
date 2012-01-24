# - easy way to update all sources with new/old locales:
#   lynx -dump http://carme.pld-linux.org/~arekm/kde/kde-l10n | awk -vi=19 '/4.1.0.tar.bz2$/{printf("Source%d: %s\n", i++, $2)}' | tee out
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
Version:	4.8.0
Release:	1
License:	GPL
Group:		Networking/Hacking
Source100:	kde4diff.sh
# Source100-md5:	e335c913f721664dc383542367cdcbf2
Source0:	%{_urlprefix}/analitza-%{version}.tar.bz2
# Source0-md5:	a45981814327beb81ddfef209dbbb076
Source1:	%{_urlprefix}/ark-%{version}.tar.bz2
# Source1-md5:	e705235a81a198564c067bdfcb29ef10
Source2:	%{_urlprefix}/blinken-%{version}.tar.bz2
# Source2-md5:	0dba841a998fec4ada7fbf068d0c38b0
Source3:	%{_urlprefix}/cantor-%{version}.tar.bz2
# Source3-md5:	aa2e06f133615d44143cf6ad6da52aaf
Source4:	%{_urlprefix}/filelight-%{version}.tar.bz2
# Source4-md5:	998178e03e56a6074b5c7d8b78dc28e4
Source5:	%{_urlprefix}/gwenview-%{version}.tar.bz2
# Source5-md5:	d6339e29d9731dace7bb52f86e99a30e
Source6:	%{_urlprefix}/jovie-%{version}.tar.bz2
# Source6-md5:	17104dcbc028b4f36ba6999426168670
Source7:	%{_urlprefix}/kaccessible-%{version}.tar.bz2
# Source7-md5:	942a509f3ccdf292afb75c9d32c7e136
Source8:	%{_urlprefix}/kactivities-%{version}.tar.bz2
# Source8-md5:	ef762f0ecf2cda78212e6aa6946ffd13
Source9:	%{_urlprefix}/kalgebra-%{version}.tar.bz2
# Source9-md5:	8d5ff9c91c0203c3608af10eeb67195c
Source10:	%{_urlprefix}/kalzium-%{version}.tar.bz2
# Source10-md5:	9da1db7aca2bc178c11549598a02a3fb
Source11:	%{_urlprefix}/kamera-%{version}.tar.bz2
# Source11-md5:	2d7340b1215c24d1e98875c5eea4d54d
Source12:	%{_urlprefix}/kanagram-%{version}.tar.bz2
# Source12-md5:	e4768621391911542d2986a3571a0c3f
Source13:	%{_urlprefix}/kate-%{version}.tar.bz2
# Source13-md5:	abe76125a855e91c2c86849cbf1b8350
Source14:	%{_urlprefix}/kbruch-%{version}.tar.bz2
# Source14-md5:	898ee167ac04a5945f4d90191aa1bea9
Source15:	%{_urlprefix}/kcalc-%{version}.tar.bz2
# Source15-md5:	783fa13b557779d6ce661451a71a56c4
Source16:	%{_urlprefix}/kcharselect-%{version}.tar.bz2
# Source16-md5:	4150d41fe47882c9a3f994dba15283eb
Source17:	%{_urlprefix}/kcolorchooser-%{version}.tar.bz2
# Source17-md5:	48ede55e885819143f229c1f6bb2d388
Source18:	%{_urlprefix}/kde-baseapps-%{version}.tar.bz2
# Source18-md5:	6d3f3d4e030aa2aa690b6fc3124b5832
Source19:	%{_urlprefix}/kde-l10n
# Source19-md5:	40ff7f8eb50b837f871140280f3f5634
Source20:	%{_urlprefix}/kde-runtime-%{version}.tar.bz2
# Source20-md5:	571563f6ab330348d3f917abdf9c69e4
Source21:	%{_urlprefix}/kde-wallpapers-%{version}.tar.bz2
# Source21-md5:	396aa669ab31ab32f73f2278e6ca143a
Source22:	%{_urlprefix}/kde-workspace-%{version}.tar.bz2
# Source22-md5:	19f40e351df9db3d434a5a579fe7e529
Source23:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source23-md5:	4ae902b75b009bd7dca5e8d1423c0fc4
Source24:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source24-md5:	19f5f7c2294deae9741a6cd70005cc4a
Source25:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source25-md5:	20d3b5ead912bc8d6d326cdb305f1b90
Source26:	%{_urlprefix}/kdegraphics-mobipocket-%{version}.tar.bz2
# Source26-md5:	a6e9fcc99189802d130d19824521ac42
Source27:	%{_urlprefix}/kdegraphics-strigi-analyzer-%{version}.tar.bz2
# Source27-md5:	f25df7e81603bcb02c4246eef3826381
Source28:	%{_urlprefix}/kdegraphics-thumbnailers-%{version}.tar.bz2
# Source28-md5:	3676f3f233968b12d1bdac40931dde30
Source29:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source29-md5:	c19858c68f9a209ae521d7fb3c34747b
Source30:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source30-md5:	b1217b735e6ac8abce1b6423601e1be3
Source31:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source31-md5:	4fc00a35dc3f0b3b06a2b6be3086563d
Source32:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source32-md5:	502216fe546ee87b7bb66f2da5599417
Source33:	%{_urlprefix}/kdepim-runtime-%{version}.tar.bz2
# Source33-md5:	8f941417152fd2ae9e5130cf0426a95e
Source34:	%{_urlprefix}/kdepimlibs-%{version}.tar.bz2
# Source34-md5:	3e1ea1d5f56eb87c0c305d941ac414c0
Source35:	%{_urlprefix}/kdeplasma-addons-%{version}.tar.bz2
# Source35-md5:	5b2947ef92fc04aecca8af4393336265
Source36:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source36-md5:	a5a1265a74c5a73cf39d65cad0bd4bd4
Source37:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source37-md5:	71856659db5cf9333499e06f24c0135e
Source38:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source38-md5:	d247fd36ece60bd9d6beaf8f5feb7a1f
Source39:	%{_urlprefix}/kdf-%{version}.tar.bz2
# Source39-md5:	11ec8e7098f020574b925c614e9f46f2
Source40:	%{_urlprefix}/kfloppy-%{version}.tar.bz2
# Source40-md5:	0fff088aaf5a9aa8f1ffd5fabd24fd1a
Source41:	%{_urlprefix}/kgamma-%{version}.tar.bz2
# Source41-md5:	34169d11b670944d7e373d61a220c95c
Source42:	%{_urlprefix}/kgeography-%{version}.tar.bz2
# Source42-md5:	72d1154427723353ad76e48bfc753f02
Source43:	%{_urlprefix}/kgpg-%{version}.tar.bz2
# Source43-md5:	7c757f10db719f6e16cc8bb70f67504e
Source44:	%{_urlprefix}/khangman-%{version}.tar.bz2
# Source44-md5:	a738b368d9a8516bb75b0d84f3285258
Source45:	%{_urlprefix}/kig-%{version}.tar.bz2
# Source45-md5:	2798cb1881a1fefbdc0f051db99cd2b5
Source46:	%{_urlprefix}/kimono-%{version}.tar.bz2
# Source46-md5:	ad5d0e7b45a7b1900cfdeb969dc5d290
Source47:	%{_urlprefix}/kiten-%{version}.tar.bz2
# Source47-md5:	cf787e0c3037a38a5e56f1927cee4693
Source48:	%{_urlprefix}/klettres-%{version}.tar.bz2
# Source48-md5:	f60c9d948e03adcf9b87866c3e489b15
Source49:	%{_urlprefix}/kmag-%{version}.tar.bz2
# Source49-md5:	e693f27fc5a4fe234c474fc164cd44fa
Source50:	%{_urlprefix}/kmousetool-%{version}.tar.bz2
# Source50-md5:	80273941c1cd0264a330b156c5412f46
Source51:	%{_urlprefix}/kmouth-%{version}.tar.bz2
# Source51-md5:	7c6d8d90949e5f1145ab95710a200c7c
Source52:	%{_urlprefix}/kmplot-%{version}.tar.bz2
# Source52-md5:	9922acd164d3b152551ad8a501e7e6a6
Source53:	%{_urlprefix}/kolourpaint-%{version}.tar.bz2
# Source53-md5:	04129e9cdef1f964612a77b97c4bd9f3
Source54:	%{_urlprefix}/konsole-%{version}.tar.bz2
# Source54-md5:	630da3df5545457f69e3aa86327b76b4
Source55:	%{_urlprefix}/korundum-%{version}.tar.bz2
# Source55-md5:	5efef73e24ad15bafb894fb765f466d9
Source56:	%{_urlprefix}/kremotecontrol-%{version}.tar.bz2
# Source56-md5:	90c5dfece8cbdec64b9c809303387fb3
Source57:	%{_urlprefix}/kross-interpreters-%{version}.tar.bz2
# Source57-md5:	d588c7afa24bb9fdd619737bdc61607f
Source58:	%{_urlprefix}/kruler-%{version}.tar.bz2
# Source58-md5:	98036f7a77e914aaae3da9ca9d638806
Source59:	%{_urlprefix}/ksaneplugin-%{version}.tar.bz2
# Source59-md5:	457a8a796937c7eda4e118d71f65a0fa
Source60:	%{_urlprefix}/ksecrets-%{version}.tar.bz2
# Source60-md5:	fa126591e8da34e16b65ecfad9f3907a
Source61:	%{_urlprefix}/ksnapshot-%{version}.tar.bz2
# Source61-md5:	dfa82ee16987070b2150b9426dd2ac35
Source62:	%{_urlprefix}/kstars-%{version}.tar.bz2
# Source62-md5:	3f87bdcb332e9e15c158b0fbeb134755
Source63:	%{_urlprefix}/ktimer-%{version}.tar.bz2
# Source63-md5:	a1d854ca4a975f0035bf517fcee95d34
Source64:	%{_urlprefix}/ktouch-%{version}.tar.bz2
# Source64-md5:	9a691e993c46253d2a087c15d0404c76
Source65:	%{_urlprefix}/kturtle-%{version}.tar.bz2
# Source65-md5:	f14b8db9ee9516b7ce0779b6726c38ef
Source66:	%{_urlprefix}/kwallet-%{version}.tar.bz2
# Source66-md5:	346fea9e992b85bf8de285160dfb9705
Source67:	%{_urlprefix}/kwordquiz-%{version}.tar.bz2
# Source67-md5:	dc68a189fb8988f7889f29cc091c3de7
Source68:	%{_urlprefix}/libkdcraw-%{version}.tar.bz2
# Source68-md5:	986fbbe46f0c17d45784593b18e6e31d
Source69:	%{_urlprefix}/libkdeedu-%{version}.tar.bz2
# Source69-md5:	b984c0e5ea4d9101b150773f4d92c71f
Source70:	%{_urlprefix}/libkexiv2-%{version}.tar.bz2
# Source70-md5:	87f69c9e04cb4c14d18c2c3404740f20
Source71:	%{_urlprefix}/libkipi-%{version}.tar.bz2
# Source71-md5:	b0a84b23a17b2b71cf143b896a77936d
Source72:	%{_urlprefix}/libksane-%{version}.tar.bz2
# Source72-md5:	864685ebe7bb7e7efcb1c9122b9b9d23
Source73:	%{_urlprefix}/marble-%{version}.tar.bz2
# Source73-md5:	95c546f33706d8fcbef8a04b4b18a17f
Source74:	%{_urlprefix}/okular-%{version}.tar.bz2
# Source74-md5:	6df57858c0138072b69945072d09978c
Source75:	%{_urlprefix}/oxygen-icons-%{version}.tar.bz2
# Source75-md5:	2ae26ba235f207eb29677637c1d059a7
Source76:	%{_urlprefix}/parley-%{version}.tar.bz2
# Source76-md5:	92608ce548515a53191705c94af46628
Source77:	%{_urlprefix}/perlkde-%{version}.tar.bz2
# Source77-md5:	a85ad9879e3baeffed23d6d4d4bb0e24
Source78:	%{_urlprefix}/perlqt-%{version}.tar.bz2
# Source78-md5:	b9a419ba264d12fa89a3fb0da5e9fa57
Source79:	%{_urlprefix}/printer-applet-%{version}.tar.bz2
# Source79-md5:	7fb821b0052696c9dc7dcc0360265674
Source80:	%{_urlprefix}/pykde4-%{version}.tar.bz2
# Source80-md5:	5f31743bebb879e537426dafb0b6d942
Source81:	%{_urlprefix}/qtruby-%{version}.tar.bz2
# Source81-md5:	c78fdbd02f161025da5a08b83c47ac66
Source82:	%{_urlprefix}/qyoto-%{version}.tar.bz2
# Source82-md5:	24a3727bdde0f54aff05825d0cc64cd4
Source83:	%{_urlprefix}/rocs-%{version}.tar.bz2
# Source83-md5:	0c38086c47408b8470157d596f7ce221
Source84:	%{_urlprefix}/smokegen-%{version}.tar.bz2
# Source84-md5:	8f3b232945720bf7c23239f4a1b2737d
Source85:	%{_urlprefix}/smokekde-%{version}.tar.bz2
# Source85-md5:	c86cce394b795e0be5ebb25f428f3726
Source86:	%{_urlprefix}/smokeqt-%{version}.tar.bz2
# Source86-md5:	7743457909c5e003ab5da3f6fd8d2a0d
Source87:	%{_urlprefix}/step-%{version}.tar.bz2
# Source87-md5:	e476da52857ac1d753d821e4732c0126
Source88:	%{_urlprefix}/superkaramba-%{version}.tar.bz2
# Source88-md5:	554c3e5dd470b2428f5792cd72224fdf
Source89:	%{_urlprefix}/svgpart-%{version}.tar.bz2
# Source89-md5:	17a325765568945ddbb12a391886b433
Source90:	%{_urlprefix}/sweeper-%{version}.tar.bz2
# Source90-md5:	b53b550467f1c545c08553bbfa0af641
%if %{with l10n}
Source101: %{_urlprefix}/kde-l10n/kde-l10n-ar-4.8.0.tar.bz2
# Source101-md5:	a33e5b8b7c5bf7cc3c013cdc5658882e
Source102: %{_urlprefix}/kde-l10n/kde-l10n-bg-4.8.0.tar.bz2
# Source102-md5:	4ed8b7bfe8cede8be04ad36b6ddbaa92
Source103: %{_urlprefix}/kde-l10n/kde-l10n-bs-4.8.0.tar.bz2
# Source103-md5:	1892c4bbbefced04ef661da6a3543547
Source104: %{_urlprefix}/kde-l10n/kde-l10n-ca-4.8.0.tar.bz2
# Source104-md5:	833bf448d24000d0f5501d7a78dfea14
Source105: %{_urlprefix}/kde-l10n/kde-l10n-ca@valencia-4.8.0.tar.bz2
# Source105-md5:	91a34fd517d05c8040b4cdfbd91d866e
Source106: %{_urlprefix}/kde-l10n/kde-l10n-cs-4.8.0.tar.bz2
# Source106-md5:	8c7bd9791a2e2e8b68be2b05aa9c0d46
Source107: %{_urlprefix}/kde-l10n/kde-l10n-da-4.8.0.tar.bz2
# Source107-md5:	dd60e258a84b9b3537deb5dbd6303d38
Source108: %{_urlprefix}/kde-l10n/kde-l10n-de-4.8.0.tar.bz2
# Source108-md5:	dbd87ccfadcd4d7d93408571032c34b5
Source109: %{_urlprefix}/kde-l10n/kde-l10n-el-4.8.0.tar.bz2
# Source109-md5:	84ff38a5886a3e50ddd23d1c2ba12f7a
Source110: %{_urlprefix}/kde-l10n/kde-l10n-en_GB-4.8.0.tar.bz2
# Source110-md5:	05405af187ea219dbdbd5ffd028961af
Source111: %{_urlprefix}/kde-l10n/kde-l10n-es-4.8.0.tar.bz2
# Source111-md5:	b7503acc7750ceb9aa972ed4da8867ae
Source112: %{_urlprefix}/kde-l10n/kde-l10n-et-4.8.0.tar.bz2
# Source112-md5:	3447e1bf8d5e2e095d4b669246f54b9e
Source113: %{_urlprefix}/kde-l10n/kde-l10n-eu-4.8.0.tar.bz2
# Source113-md5:	eab6d0986e15b10bb337c12450b294c5
Source114: %{_urlprefix}/kde-l10n/kde-l10n-fa-4.8.0.tar.bz2
# Source114-md5:	3ec5f26bdee9c08f8e5815081837473a
Source115: %{_urlprefix}/kde-l10n/kde-l10n-fi-4.8.0.tar.bz2
# Source115-md5:	3b32c493fa6c294b3e702a7033922d51
Source116: %{_urlprefix}/kde-l10n/kde-l10n-fr-4.8.0.tar.bz2
# Source116-md5:	a2b81e1e16d3a2012f5530879dab6b64
Source117: %{_urlprefix}/kde-l10n/kde-l10n-ga-4.8.0.tar.bz2
# Source117-md5:	20c7a8632061f75c217ec709571de2c7
Source118: %{_urlprefix}/kde-l10n/kde-l10n-gl-4.8.0.tar.bz2
# Source118-md5:	1a415d4b6483aed24c6d8fd0c8d25fe0
Source119: %{_urlprefix}/kde-l10n/kde-l10n-hr-4.8.0.tar.bz2
# Source119-md5:	14d3c285ca3196e94d969aa29885bc66
Source120: %{_urlprefix}/kde-l10n/kde-l10n-hu-4.8.0.tar.bz2
# Source120-md5:	c0e557026e97f2d0a7cede09b2a553ab
Source121: %{_urlprefix}/kde-l10n/kde-l10n-ia-4.8.0.tar.bz2
# Source121-md5:	5e8d4f87d819c5832edc888139ea6e8e
Source122: %{_urlprefix}/kde-l10n/kde-l10n-is-4.8.0.tar.bz2
# Source122-md5:	608f969f084264fb94181ca03e9cb22a
Source123: %{_urlprefix}/kde-l10n/kde-l10n-it-4.8.0.tar.bz2
# Source123-md5:	43bd69690af7008b2daa40b79f6b1f03
Source124: %{_urlprefix}/kde-l10n/kde-l10n-ja-4.8.0.tar.bz2
# Source124-md5:	04487bb3a7fa2e729827af2d6d7fecf6
Source125: %{_urlprefix}/kde-l10n/kde-l10n-kk-4.8.0.tar.bz2
# Source125-md5:	b7e04bb0269134fc3b8ae281a93e55e3
Source126: %{_urlprefix}/kde-l10n/kde-l10n-km-4.8.0.tar.bz2
# Source126-md5:	cff24c2dcdd3a74f90accfddfacbd190
Source127: %{_urlprefix}/kde-l10n/kde-l10n-ko-4.8.0.tar.bz2
# Source127-md5:	64d46182cfbb1aec4369524aa3839aa1
Source128: %{_urlprefix}/kde-l10n/kde-l10n-lt-4.8.0.tar.bz2
# Source128-md5:	b9c24bc7130fb61647a21a65fcd41e85
Source129: %{_urlprefix}/kde-l10n/kde-l10n-lv-4.8.0.tar.bz2
# Source129-md5:	b5c277e694397e8b4224bd2a2c20d4ff
Source130: %{_urlprefix}/kde-l10n/kde-l10n-nb-4.8.0.tar.bz2
# Source130-md5:	4f99f6c942cd2fe49e8af8509add6173
Source131: %{_urlprefix}/kde-l10n/kde-l10n-nds-4.8.0.tar.bz2
# Source131-md5:	f1820935e32b2fbf18b80a52b96e4e1d
Source132: %{_urlprefix}/kde-l10n/kde-l10n-nl-4.8.0.tar.bz2
# Source132-md5:	4e6ecce49f26eb20d5c1acd9bf652a85
Source133: %{_urlprefix}/kde-l10n/kde-l10n-nn-4.8.0.tar.bz2
# Source133-md5:	f5531c9ea46590acbd7842f67ad6bfc4
Source134: %{_urlprefix}/kde-l10n/kde-l10n-pa-4.8.0.tar.bz2
# Source134-md5:	2aa9d93435ef52b9a8f614bfe6ec2294
Source135: %{_urlprefix}/kde-l10n/kde-l10n-pl-4.8.0.tar.bz2
# Source135-md5:	8c94e428e9e2cc44df77a177385f73eb
Source136: %{_urlprefix}/kde-l10n/kde-l10n-pt-4.8.0.tar.bz2
# Source136-md5:	ac0053850106d66415805181e87b932d
Source137: %{_urlprefix}/kde-l10n/kde-l10n-pt_BR-4.8.0.tar.bz2
# Source137-md5:	ca423cf9ad488a74bbb8fd09feecae2a
Source138: %{_urlprefix}/kde-l10n/kde-l10n-ro-4.8.0.tar.bz2
# Source138-md5:	86fbec2459f4dbe0032eb4b9ded3f7fc
Source139: %{_urlprefix}/kde-l10n/kde-l10n-ru-4.8.0.tar.bz2
# Source139-md5:	7f895820b8e73da6040027ee2049409a
Source140: %{_urlprefix}/kde-l10n/kde-l10n-si-4.8.0.tar.bz2
# Source140-md5:	cf2d3a3c76ffbe9d85715dbf07f360de
Source141: %{_urlprefix}/kde-l10n/kde-l10n-sk-4.8.0.tar.bz2
# Source141-md5:	964184d80b5fd175779c70d357cac568
Source142: %{_urlprefix}/kde-l10n/kde-l10n-sl-4.8.0.tar.bz2
# Source142-md5:	57adcbc99143ecfa58b74eb2281b3f93
Source143: %{_urlprefix}/kde-l10n/kde-l10n-sr-4.8.0.tar.bz2
# Source143-md5:	ce019d325312229619d4a3c199fdab27
Source144: %{_urlprefix}/kde-l10n/kde-l10n-sv-4.8.0.tar.bz2
# Source144-md5:	e97a9c78978acf95cc7f877c5acef04c
Source145: %{_urlprefix}/kde-l10n/kde-l10n-tg-4.8.0.tar.bz2
# Source145-md5:	c6a83783134f3a9d645f2be734cc0a38
Source146: %{_urlprefix}/kde-l10n/kde-l10n-th-4.8.0.tar.bz2
# Source146-md5:	1bda85b0ee0519b512f27a8d61f47f2e
Source147: %{_urlprefix}/kde-l10n/kde-l10n-tr-4.8.0.tar.bz2
# Source147-md5:	154760d2fabee5528b5942a6454ebdcc
Source148: %{_urlprefix}/kde-l10n/kde-l10n-uk-4.8.0.tar.bz2
# Source148-md5:	87f4e8c8fd9d9a0270e25823d0302fb0
Source149: %{_urlprefix}/kde-l10n/kde-l10n-vi-4.8.0.tar.bz2
# Source149-md5:	b9d10d2a53483b21f09a8c3918a43680
Source150: %{_urlprefix}/kde-l10n/kde-l10n-wa-4.8.0.tar.bz2
# Source150-md5:	0f633a5be3a2f9be010e519414983bf4
Source151: %{_urlprefix}/kde-l10n/kde-l10n-zh_CN-4.8.0.tar.bz2
# Source151-md5:	9b0e5a570b03e0652f2674882b079e20
Source152: %{_urlprefix}/kde-l10n/kde-l10n-zh_TW-4.8.0.tar.bz2
# Source152-md5:	162c411c6b532a6e5045a0befb6fd94a
%endif
%if %{with koffice}
Source68:	%{_urlprefix}/koffice-%{kofficever}/koffice-%{kofficever}.tar.bz2
# Source68-md5:	986fbbe46f0c17d45784593b18e6e31d
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
