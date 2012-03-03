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
Version:	4.8.1
Release:	1
License:	GPL
Group:		Networking/Hacking
Source100:	kde4diff.sh
# Source100-md5:	e335c913f721664dc383542367cdcbf2
Source0:	%{_urlprefix}/analitza-%{version}.tar.xz
# Source0-md5:	d7271f7bf8e379aff579aed24bb4a956
Source1:	%{_urlprefix}/ark-%{version}.tar.xz
# Source1-md5:	0617846872e4390f998711a74b5a7805
Source2:	%{_urlprefix}/blinken-%{version}.tar.xz
# Source2-md5:	2fe2cf873683e3c583152d1986bbee90
Source3:	%{_urlprefix}/cantor-%{version}.tar.xz
# Source3-md5:	41ee1a7408324a690cca543832105ad3
Source4:	%{_urlprefix}/filelight-%{version}.tar.xz
# Source4-md5:	57d6d1d4c78ab74243b412804259a804
Source5:	%{_urlprefix}/gwenview-%{version}.tar.xz
# Source5-md5:	2b9124dd481aa26132de54349be2ef57
Source6:	%{_urlprefix}/jovie-%{version}.tar.xz
# Source6-md5:	e1185281ea0e2c221dc25bd5644da022
Source7:	%{_urlprefix}/kaccessible-%{version}.tar.xz
# Source7-md5:	4c44447f831d804d8cd12c59315f9ff8
Source8:	%{_urlprefix}/kactivities-%{version}.tar.xz
# Source8-md5:	ed51cc5d594d88712afa5a556dbc53e8
Source9:	%{_urlprefix}/kalgebra-%{version}.tar.xz
# Source9-md5:	fdee9c8b80a3872492e3648db8f54026
Source10:	%{_urlprefix}/kalzium-%{version}.tar.xz
# Source10-md5:	fe3c9ea4257ca146af9cbacf103507f8
Source11:	%{_urlprefix}/kamera-%{version}.tar.xz
# Source11-md5:	2b5875c55f2a658eec603131d1c5cdad
Source12:	%{_urlprefix}/kanagram-%{version}.tar.xz
# Source12-md5:	dc461aaf6cc4b2b0937abf506f96b654
Source13:	%{_urlprefix}/kate-%{version}.tar.xz
# Source13-md5:	cf2e11bd3a25080694cd8498ce3f49ba
Source14:	%{_urlprefix}/kbruch-%{version}.tar.xz
# Source14-md5:	bfaf6bc67bb7fda475c5a1f4760f5ddf
Source15:	%{_urlprefix}/kcalc-%{version}.tar.xz
# Source15-md5:	b5fb8194d7dee8d933cb48c4fe04bb89
Source16:	%{_urlprefix}/kcharselect-%{version}.tar.xz
# Source16-md5:	41d89a446e49f3d2c2dff1a8bdb60f89
Source17:	%{_urlprefix}/kcolorchooser-%{version}.tar.xz
# Source17-md5:	9ae91d18499cc185b385bf0c508bb08d
Source18:	%{_urlprefix}/kde-baseapps-%{version}.tar.xz
# Source18-md5:	f9421df243f935ab7076fe7be7572cec
Source19:	%{_urlprefix}/kde-l10n
# Source19-md5:	40ff7f8eb50b837f871140280f3f5634
Source20:	%{_urlprefix}/kde-runtime-%{version}.tar.xz
# Source20-md5:	9fa9c4015f158d1b434a5b8653e65dcf
Source21:	%{_urlprefix}/kde-wallpapers-%{version}.tar.xz
# Source21-md5:	803b5e91d415ab3519a872c70b0c770a
Source22:	%{_urlprefix}/kde-workspace-%{version}.tar.xz
# Source22-md5:	e4549dab07507e602a868bededb740ec
Source23:	%{_urlprefix}/kdeadmin-%{version}.tar.xz
# Source23-md5:	816e678301670c8e7fe859f99951c7d4
Source24:	%{_urlprefix}/kdeartwork-%{version}.tar.xz
# Source24-md5:	be817818f3e1971a31a8606e49f522a1
Source25:	%{_urlprefix}/kdegames-%{version}.tar.xz
# Source25-md5:	450d31446cbf978d8f104a63ebeafdec
Source26:	%{_urlprefix}/kdegraphics-mobipocket-%{version}.tar.xz
# Source26-md5:	f97480d37f7f4f09de1b5cc263204927
Source27:	%{_urlprefix}/kdegraphics-strigi-analyzer-%{version}.tar.xz
# Source27-md5:	43c6db223db10a71fa7a0285b8d2146f
Source28:	%{_urlprefix}/kdegraphics-thumbnailers-%{version}.tar.xz
# Source28-md5:	85b3887e7dff902d9f6b247f5e23719f
Source29:	%{_urlprefix}/kdelibs-%{version}.tar.xz
# Source29-md5:	0488ec7d753c3455876d9e3f76406292
Source30:	%{_urlprefix}/kdemultimedia-%{version}.tar.xz
# Source30-md5:	5feaa2f12f46b60c9b23a1a7011cbdef
Source31:	%{_urlprefix}/kdenetwork-%{version}.tar.xz
# Source31-md5:	cec7c15d1b21b085216be772b5bee9e5
Source32:	%{_urlprefix}/kdepim-%{version}.tar.xz
# Source32-md5:	46a6dd45874b4a5d9cf18785ab4c774e
Source33:	%{_urlprefix}/kdepim-runtime-%{version}.tar.xz
# Source33-md5:	9c26ea08d3c937313e931070c902bfb6
Source34:	%{_urlprefix}/kdepimlibs-%{version}.tar.xz
# Source34-md5:	b5d77e68e6daa93cae3364c825142b4e
Source35:	%{_urlprefix}/kdeplasma-addons-%{version}.tar.xz
# Source35-md5:	9844b096e637f51e4640816cd8b4de42
Source36:	%{_urlprefix}/kdesdk-%{version}.tar.xz
# Source36-md5:	7870565f51d4a8ce847dda42ca9ffe30
Source37:	%{_urlprefix}/kdetoys-%{version}.tar.xz
# Source37-md5:	21a3010705eb4506c3b072a14d62784d
Source38:	%{_urlprefix}/kdewebdev-%{version}.tar.xz
# Source38-md5:	0a3a936f207d09af4ea986988d1fc122
Source39:	%{_urlprefix}/kdf-%{version}.tar.xz
# Source39-md5:	054678f0d81a2a1e908bdf6b7a236ceb
Source40:	%{_urlprefix}/kfloppy-%{version}.tar.xz
# Source40-md5:	b80fc397db04078a7e3787dc92ae30db
Source41:	%{_urlprefix}/kgamma-%{version}.tar.xz
# Source41-md5:	87153d955b0926491df4caec5310f984
Source42:	%{_urlprefix}/kgeography-%{version}.tar.xz
# Source42-md5:	5d26aee81678ab952ee21444be86f93a
Source43:	%{_urlprefix}/kgpg-%{version}.tar.xz
# Source43-md5:	1b54569da5989e248c1f41ed0399fe4b
Source44:	%{_urlprefix}/khangman-%{version}.tar.xz
# Source44-md5:	823eb9d1a9b4f9b2f64a1a5e1305b056
Source45:	%{_urlprefix}/kig-%{version}.tar.xz
# Source45-md5:	8d7c57183c7abce16c2741bb058fb7de
Source46:	%{_urlprefix}/kimono-%{version}.tar.xz
# Source46-md5:	7d3f9c80db9b7cd800a5d1a039b4a641
Source47:	%{_urlprefix}/kiten-%{version}.tar.xz
# Source47-md5:	d6051ab675a5028bd7ece0d8fc9ee0fe
Source48:	%{_urlprefix}/klettres-%{version}.tar.xz
# Source48-md5:	2da84fdc0a2f03cb2cccb2e7c624d9ce
Source49:	%{_urlprefix}/kmag-%{version}.tar.xz
# Source49-md5:	194504ff8c7969d46ba275b2183cf2c3
Source50:	%{_urlprefix}/kmousetool-%{version}.tar.xz
# Source50-md5:	52d106e0929ecec91234c1408288cd7b
Source51:	%{_urlprefix}/kmouth-%{version}.tar.xz
# Source51-md5:	bda199b8b3f2ed961f5b34821ac8f705
Source52:	%{_urlprefix}/kmplot-%{version}.tar.xz
# Source52-md5:	281abbdc71a72930e5bb6c02fd4e10f5
Source53:	%{_urlprefix}/kolourpaint-%{version}.tar.xz
# Source53-md5:	194a6349f4d851e24f3299db6891e338
Source54:	%{_urlprefix}/konsole-%{version}.tar.xz
# Source54-md5:	913c682bbc857c76392d7e8df8c463b1
Source55:	%{_urlprefix}/korundum-%{version}.tar.xz
# Source55-md5:	8cc3ba4d1a916b646529707cbe95c49c
Source56:	%{_urlprefix}/kremotecontrol-%{version}.tar.xz
# Source56-md5:	4d8edb8b57908c3039a15e0a7c7238f1
Source57:	%{_urlprefix}/kross-interpreters-%{version}.tar.xz
# Source57-md5:	b4405799a3e1408f88242f9f2fbec8ef
Source58:	%{_urlprefix}/kruler-%{version}.tar.xz
# Source58-md5:	22da4492b7e33b38d0a60dbad21efcb6
Source59:	%{_urlprefix}/ksaneplugin-%{version}.tar.xz
# Source59-md5:	4eb7ee80b6dceb108cbe69fba99ee50d
Source60:	%{_urlprefix}/ksecrets-%{version}.tar.xz
# Source60-md5:	61533859da11b808214b4bc0478e31ad
Source61:	%{_urlprefix}/ksnapshot-%{version}.tar.xz
# Source61-md5:	f1d61b6865c2cf7e002860303fa7b052
Source62:	%{_urlprefix}/kstars-%{version}.tar.xz
# Source62-md5:	17dd8579901a6fb500bda620a8706376
Source63:	%{_urlprefix}/ktimer-%{version}.tar.xz
# Source63-md5:	1cd04e2529ab2dd041ac8c4eaa4e3338
Source64:	%{_urlprefix}/ktouch-%{version}.tar.xz
# Source64-md5:	1da0a972c66b7e6bc8c7aa6f50e6dbfa
Source65:	%{_urlprefix}/kturtle-%{version}.tar.xz
# Source65-md5:	5ed342e2ac44fb74be8e07a2ef643423
Source66:	%{_urlprefix}/kwallet-%{version}.tar.xz
# Source66-md5:	90103ae4a19ea4a212a9bd6521d214de
Source67:	%{_urlprefix}/kwordquiz-%{version}.tar.xz
# Source67-md5:	09c8bca9a691f562610f832f8fb7f904
Source68:	%{_urlprefix}/libkdcraw-%{version}.tar.xz
# Source68-md5:	83e20af3ae9da617aa95f868000a2cd4
Source69:	%{_urlprefix}/libkdeedu-%{version}.tar.xz
# Source69-md5:	db4fc897ca2e84f527eadabc5b49bce1
Source70:	%{_urlprefix}/libkexiv2-%{version}.tar.xz
# Source70-md5:	05491210248c18b69272f45fddab2f30
Source71:	%{_urlprefix}/libkipi-%{version}.tar.xz
# Source71-md5:	9f28791d6a2b11157d421b5ce1af3b20
Source72:	%{_urlprefix}/libksane-%{version}.tar.xz
# Source72-md5:	c84a768f953576db8030017c2709ea37
Source73:	%{_urlprefix}/marble-%{version}.tar.xz
# Source73-md5:	e1b73990d92d6e4d7f1799e72f885946
Source74:	%{_urlprefix}/okular-%{version}.tar.xz
# Source74-md5:	7e21d10d1631e9c72c25b3ac58c31edb
Source75:	%{_urlprefix}/oxygen-icons-%{version}.tar.xz
# Source75-md5:	947d07c4f993e7cf070078358de13298
Source76:	%{_urlprefix}/parley-%{version}.tar.xz
# Source76-md5:	6194571f3ef9b66a93bb90a3842539ce
Source77:	%{_urlprefix}/perlkde-%{version}.tar.xz
# Source77-md5:	53e8cfc061fe699c7ff12a64b22b33a4
Source78:	%{_urlprefix}/perlqt-%{version}.tar.xz
# Source78-md5:	a644f1ca39d9140f12069e7065fa4bd5
Source79:	%{_urlprefix}/printer-applet-%{version}.tar.xz
# Source79-md5:	395dfbd48c087f519618d2edfd10580c
Source80:	%{_urlprefix}/pykde4-%{version}.tar.xz
# Source80-md5:	ef9da17db70c6ce532dc59c56020c333
Source81:	%{_urlprefix}/qtruby-%{version}.tar.xz
# Source81-md5:	0a9abf4fa07408d4dcab8bb8a0f9f344
Source82:	%{_urlprefix}/qyoto-%{version}.tar.xz
# Source82-md5:	c4fcc2b0e27ea70101620988d9e6898c
Source83:	%{_urlprefix}/rocs-%{version}.tar.xz
# Source83-md5:	d19ee2dab11e346158b578599c0f145d
Source84:	%{_urlprefix}/smokegen-%{version}.tar.xz
# Source84-md5:	ed67926d7fb44080a167ce1cbcac5acd
Source85:	%{_urlprefix}/smokekde-%{version}.tar.xz
# Source85-md5:	dc1d046f79613b9f0dd41194a4ece687
Source86:	%{_urlprefix}/smokeqt-%{version}.tar.xz
# Source86-md5:	f10807832cbfa4c08ebecfc8dec6a0f8
Source87:	%{_urlprefix}/step-%{version}.tar.xz
# Source87-md5:	b734335e134d40801f5d3230665c0a0c
Source88:	%{_urlprefix}/superkaramba-%{version}.tar.xz
# Source88-md5:	babb2b3c03bc50dc8c4aece9f8a0223a
Source89:	%{_urlprefix}/svgpart-%{version}.tar.xz
# Source89-md5:	c63eb95b457314b7d2e4f1cfb66a344d
Source90:	%{_urlprefix}/sweeper-%{version}.tar.xz
# Source90-md5:	63e5ec115d68135164ee5f87f4e6fada
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
# Source68-md5:	83e20af3ae9da617aa95f868000a2cd4
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
