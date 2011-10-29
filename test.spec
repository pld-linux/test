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
Version:	4.7.3
Release:	1
License:	GPL
Group:		Networking/Hacking
Source100:	kde4diff.sh
# Source100-md5:	
Source0: %{_urlprefix}/blinken-%{version}.tar.bz2
# Source0-md5:	dd0201138f84f0dc332f9b8a5bea49e9
Source1: %{_urlprefix}/cantor-%{version}.tar.bz2
# Source1-md5:	910a2e814df1a61d77f0be06c6a9f1ab
Source2: %{_urlprefix}/gwenview-%{version}.tar.bz2
# Source2-md5:	71809b5736992a912aa7032adba2f615
Source3: %{_urlprefix}/kalgebra-%{version}.tar.bz2
# Source3-md5:	0ba1eb9298c4466e232266b81ce58bff
Source4: %{_urlprefix}/kalzium-%{version}.tar.bz2
# Source4-md5:	5713d00f453a4e51965455e10de9063e
Source5: %{_urlprefix}/kamera-%{version}.tar.bz2
# Source5-md5:	a45e5c31432c86179303e88c6cf45e4b
Source6: %{_urlprefix}/kanagram-%{version}.tar.bz2
# Source6-md5:	b17de32ea9e22738c773b3188128609d
Source7: %{_urlprefix}/kate-%{version}.tar.bz2
# Source7-md5:	c7bb74c251db064b81b4e0bee4295745
Source8: %{_urlprefix}/kbruch-%{version}.tar.bz2
# Source8-md5:	6702192b84d15b10d90814601d8478f5
Source9: %{_urlprefix}/kcolorchooser-%{version}.tar.bz2
# Source9-md5:	f4f478fe5ad095e73cb31f2753cc3447
Source10: %{_urlprefix}/kde-baseapps-%{version}.tar.bz2
# Source10-md5:	5e6675a032c767db7e73b816952f9baf
Source11: %{_urlprefix}/kde-runtime-%{version}.tar.bz2
# Source11-md5:	1b80879c37e7ab1d23e224d687e8e630
Source12: %{_urlprefix}/kde-wallpapers-%{version}.tar.bz2
# Source12-md5:	163103fa8a003ad5e692858213391542
Source13: %{_urlprefix}/kde-workspace-%{version}.tar.bz2
# Source13-md5:	0814890a06a90610a4ae41e1fa3beff4
#Source14: %{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
## Source14-md5:	1669d5179e339ebc2d88502c7af050d3
Source15: %{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source15-md5:	4737b705f774ee75835385edfc4a8394
Source16: %{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source16-md5:	35be01dc71508d79148179e9e7e41571
Source17: %{_urlprefix}/kdegames-%{version}.tar.bz2
# Source17-md5:	c2b9a052c7abb342a5d273a26e5dd933
Source18: %{_urlprefix}/kdegraphics-strigi-analyzer-%{version}.tar.bz2
# Source18-md5:	fdf05d436b34c7001a919be4c5049a27
Source19: %{_urlprefix}/kdegraphics-thumbnailers-%{version}.tar.bz2
# Source19-md5:	177ccb5137308ad2a53a2046b4afb910
Source20: %{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source20-md5:	57fdc211995a6846b15dfdbf40a3e2e3
Source21: %{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source21-md5:	75764dfaab78c75ec5d40534ae20aa15
Source22: %{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source22-md5:	980f1164afd83525c099d1879276359e
Source23: %{_urlprefix}/kdepim-%{version}.tar.bz2
# Source23-md5:	ab886795c66c94fd0374d1e791ceae87
Source24: %{_urlprefix}/kdepim-runtime-%{version}.tar.bz2
# Source24-md5:	5cfa432c541722d28fe6a00375cf43dd
Source25: %{_urlprefix}/kdepimlibs-%{version}.tar.bz2
# Source25-md5:	fc29a8a6d82721b55c9322b153e1ac74
Source26: %{_urlprefix}/kdeplasma-addons-%{version}.tar.bz2
# Source26-md5:	fff6b4f068b04801c96120c5a51fa48f
Source27: %{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source27-md5:	730fbf307793efb8dd7db2d54ae8080c
Source28: %{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source28-md5:	e614644e50bac5d5b05fa94914e01f00
#Source29: %{_urlprefix}/kdeutils-%{version}.tar.bz2
## Source29-md5:	ea7888ad0752009b427065ceedc9e265
Source30: %{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source30-md5:	7f6ff53b88442ead45068db0a86ddced
Source31: %{_urlprefix}/kgamma-%{version}.tar.bz2
# Source31-md5:	9952df0e9a686eee7851d5bbe81a3d54
Source32: %{_urlprefix}/kgeography-%{version}.tar.bz2
# Source32-md5:	4b74752f6bd3dc00d123ba8f0dc46f27
Source33: %{_urlprefix}/khangman-%{version}.tar.bz2
# Source33-md5:	0b981832cb8b38fa914af52b4a9a0757
Source34: %{_urlprefix}/kig-%{version}.tar.bz2
# Source34-md5:	d470977abb051c738bd2cf7d54b50553
Source35: %{_urlprefix}/kimono-%{version}.tar.bz2
# Source35-md5:	0e425454290e12b76a26aaf49a108197
Source36: %{_urlprefix}/kiten-%{version}.tar.bz2
# Source36-md5:	43c52322c8a9ed2e6b6cd1fc57fd0c59
Source37: %{_urlprefix}/klettres-%{version}.tar.bz2
# Source37-md5:	11c29f1bda6c53906d968e5ed77178ac
Source38: %{_urlprefix}/kmplot-%{version}.tar.bz2
# Source38-md5:	5eec907bdce49c2b738283d017cea3dc
Source39: %{_urlprefix}/kolourpaint-%{version}.tar.bz2
# Source39-md5:	a66e3da8f3f85a5c8b2f4de23b106a6b
Source40: %{_urlprefix}/konsole-%{version}.tar.bz2
# Source40-md5:	fdb73cc1e4b0add724f4f177f8129bf8
Source41: %{_urlprefix}/korundum-%{version}.tar.bz2
# Source41-md5:	856a60498e89f6697772ef6de4d2b8ca
Source42: %{_urlprefix}/kross-interpreters-%{version}.tar.bz2
# Source42-md5:	c50322c0a8c046619225037727bd8cc2
Source43: %{_urlprefix}/kruler-%{version}.tar.bz2
# Source43-md5:	1cddcdc8ffa04f51c7f6b23df283a783
Source44: %{_urlprefix}/ksaneplugin-%{version}.tar.bz2
# Source44-md5:	38753e033757c7190985494db290c09f
Source45: %{_urlprefix}/ksnapshot-%{version}.tar.bz2
# Source45-md5:	cfd8fd595a77ad1753fe9e05607e1d7b
Source46: %{_urlprefix}/kstars-%{version}.tar.bz2
# Source46-md5:	791211270c3565e214e874d8852dfa11
Source47: %{_urlprefix}/ktouch-%{version}.tar.bz2
# Source47-md5:	1010d6f87ddaac47f106e22d3e694077
Source48: %{_urlprefix}/kturtle-%{version}.tar.bz2
# Source48-md5:	e7f4c8f2c94c1fc9547b3eb4e30e2c4d
Source49: %{_urlprefix}/kwordquiz-%{version}.tar.bz2
# Source49-md5:	ee548c2d08c7d4de329a20234e70cb41
Source50: %{_urlprefix}/libkdcraw-%{version}.tar.bz2
# Source50-md5:	ea57e7b64c235e5d5dd070cb7dca312e
Source51: %{_urlprefix}/libkdeedu-%{version}.tar.bz2
# Source51-md5:	7af222698e8181b28052852bfe82af22
Source52: %{_urlprefix}/libkexiv2-%{version}.tar.bz2
# Source52-md5:	4d0fcae0d7570b922eeffecfec6d9ca5
Source53: %{_urlprefix}/libkipi-%{version}.tar.bz2
# Source53-md5:	c918a3772d2e65c4da0afb28a53e186a
Source54: %{_urlprefix}/libksane-%{version}.tar.bz2
# Source54-md5:	dd01f8366d18f3f128ba76568ab142fd
Source55: %{_urlprefix}/marble-%{version}.tar.bz2
# Source55-md5:	0447caaded93c89144f1a446f226c262
Source56: %{_urlprefix}/mobipocket-%{version}.tar.bz2
# Source56-md5:	9e0aa8e2b030243e9398cbaafdab30ed
Source57: %{_urlprefix}/okular-%{version}.tar.bz2
# Source57-md5:	68d4f59a5c7e8bfd77413e7e412e2dae
Source58: %{_urlprefix}/oxygen-icons-%{version}.tar.bz2
# Source58-md5:	a211817dd168a6def9e9d3e983b3da8d
Source59: %{_urlprefix}/parley-%{version}.tar.bz2
# Source59-md5:	896b88f3f0bdab177a6beabfc9b0b380
Source60: %{_urlprefix}/perlkde-%{version}.tar.bz2
# Source60-md5:	90876c99b8a07fc2c31bce2348491803
Source61: %{_urlprefix}/perlqt-%{version}.tar.bz2
# Source61-md5:	cd13db20c7d3c93d837430a0370b30f1
Source62: %{_urlprefix}/pykde4-%{version}.tar.bz2
# Source62-md5:	cda980dba1ccb8e9afa269269cfe2b40
Source63: %{_urlprefix}/qtruby-%{version}.tar.bz2
# Source63-md5:	e1f3f6af281095ac0b24650715882c25
Source64: %{_urlprefix}/qyoto-%{version}.tar.bz2
# Source64-md5:	4dd915a5a012d33860dc520e570be15e
Source65: %{_urlprefix}/rocs-%{version}.tar.bz2
# Source65-md5:	7cf9729478082903ef8dc148ecf4ba79
Source66: %{_urlprefix}/smokegen-%{version}.tar.bz2
# Source66-md5:	3927fd6a73a3c95bdb35c4d31024dc59
Source67: %{_urlprefix}/smokekde-%{version}.tar.bz2
# Source67-md5:	570b404211229d753f893a8f381e32c9
Source68: %{_urlprefix}/smokeqt-%{version}.tar.bz2
# Source68-md5:	24331c3cf0a733ba7bbef3d9eab92d80
Source69: %{_urlprefix}/step-%{version}.tar.bz2
# Source69-md5:	273da8e98289a218d7d76e762e4ae341
Source70: %{_urlprefix}/svgpart-%{version}.tar.bz2
# Source70-md5:	d144c9ad6807ce3b4d17682a0ab5d00a
%if %{with l10n}
Source100: %{_urlprefix}/kde-l10n/kde-l10n-ar-%{version}.tar.bz2
# Source100-md5:	
Source101: %{_urlprefix}/kde-l10n/kde-l10n-bg-%{version}.tar.bz2
# Source101-md5:	5fc99c767ea3a82f247c2b00438068bb
Source102: %{_urlprefix}/kde-l10n/kde-l10n-bs-%{version}.tar.bz2
# Source102-md5:	6cc917e0e12a7512b8dc28c285e616b8
Source103: %{_urlprefix}/kde-l10n/kde-l10n-ca-%{version}.tar.bz2
# Source103-md5:	8895748164d4ac41340a105839ea36d8
Source104: %{_urlprefix}/kde-l10n/kde-l10n-ca@valencia-%{version}.tar.bz2
# Source104-md5:	a1aced26157d74af0dc18278d7a87bae
Source105: %{_urlprefix}/kde-l10n/kde-l10n-cs-%{version}.tar.bz2
# Source105-md5:	40f06d829e921b50935cffa88993c5c2
Source106: %{_urlprefix}/kde-l10n/kde-l10n-da-%{version}.tar.bz2
# Source106-md5:	f1639adb05b2ccb5827ba3a3100a1d2f
Source107: %{_urlprefix}/kde-l10n/kde-l10n-de-%{version}.tar.bz2
# Source107-md5:	6b7a4d709535a1f2f9a4101d7828486d
Source108: %{_urlprefix}/kde-l10n/kde-l10n-el-%{version}.tar.bz2
# Source108-md5:	e485781767e331d24d5a6748cf0deb07
Source109: %{_urlprefix}/kde-l10n/kde-l10n-en_GB-%{version}.tar.bz2
# Source109-md5:	e50a4f5667cdb4d7c2933c69ed32c46f
Source110: %{_urlprefix}/kde-l10n/kde-l10n-es-%{version}.tar.bz2
# Source110-md5:	5802b54b948a98d2dad9d83496115a0b
Source111: %{_urlprefix}/kde-l10n/kde-l10n-et-%{version}.tar.bz2
# Source111-md5:	99590fd262f5dd50748570848b45ab2c
Source112: %{_urlprefix}/kde-l10n/kde-l10n-eu-%{version}.tar.bz2
# Source112-md5:	ca6721a1271c9391541bc91f8f96c59c
Source113: %{_urlprefix}/kde-l10n/kde-l10n-fi-%{version}.tar.bz2
# Source113-md5:	0fd9630e88cfbccda11f5afbf717cbea
Source114: %{_urlprefix}/kde-l10n/kde-l10n-fr-%{version}.tar.bz2
# Source114-md5:	88cb733ca323e249c3b34ccb53bff9f2
Source115: %{_urlprefix}/kde-l10n/kde-l10n-ga-%{version}.tar.bz2
# Source115-md5:	8ea6275a54ed0a08ca915e5edde0e7c7
Source116: %{_urlprefix}/kde-l10n/kde-l10n-gl-%{version}.tar.bz2
# Source116-md5:	7270814fbf30533bc0c33a17e1fe94e5
Source117: %{_urlprefix}/kde-l10n/kde-l10n-he-%{version}.tar.bz2
# Source117-md5:	31bcf07e789a4b69264af0f5a7857f3c
Source118: %{_urlprefix}/kde-l10n/kde-l10n-hr-%{version}.tar.bz2
# Source118-md5:	4c9ce97ca3ee55eb3855e89a7f70ab80
Source119: %{_urlprefix}/kde-l10n/kde-l10n-hu-%{version}.tar.bz2
# Source119-md5:	4d869523e9b68dee00e9d7887ad53407
Source120: %{_urlprefix}/kde-l10n/kde-l10n-ia-%{version}.tar.bz2
# Source120-md5:	24fb09f0a9139ec1fa59c518ac20051a
Source121: %{_urlprefix}/kde-l10n/kde-l10n-id-%{version}.tar.bz2
# Source121-md5:	27b473acdc014ecbf1419c78dc68b5b5
Source122: %{_urlprefix}/kde-l10n/kde-l10n-is-%{version}.tar.bz2
# Source122-md5:	910715c07bb4dcdf0d932fe35d8c04e8
Source123: %{_urlprefix}/kde-l10n/kde-l10n-it-%{version}.tar.bz2
# Source123-md5:	2dad86f3f664b0b4e70620be16e92e9a
Source124: %{_urlprefix}/kde-l10n/kde-l10n-ja-%{version}.tar.bz2
# Source124-md5:	f964a12a83156500fa9deca862c33c5a
Source125: %{_urlprefix}/kde-l10n/kde-l10n-kk-%{version}.tar.bz2
# Source125-md5:	3c2ec10fd3a43833ec0ee07a097ee902
Source126: %{_urlprefix}/kde-l10n/kde-l10n-km-%{version}.tar.bz2
# Source126-md5:	6bcc864466676669ff4d0f630cc95f52
Source127: %{_urlprefix}/kde-l10n/kde-l10n-kn-%{version}.tar.bz2
# Source127-md5:	c7b1ed17376dcca8df1355a7f237a18c
Source128: %{_urlprefix}/kde-l10n/kde-l10n-ko-%{version}.tar.bz2
# Source128-md5:	3785f6c99a1a5f8921f1bf0e1f95ebd4
Source129: %{_urlprefix}/kde-l10n/kde-l10n-lt-%{version}.tar.bz2
# Source129-md5:	8024639bcfa6b8518aabba5441c2da94
Source130: %{_urlprefix}/kde-l10n/kde-l10n-lv-%{version}.tar.bz2
# Source130-md5:	34567ac2be7db047ab14617a59fb7ba6
Source131: %{_urlprefix}/kde-l10n/kde-l10n-nb-%{version}.tar.bz2
# Source131-md5:	ebd2d7cda4028ea63947fe8423eaa7ca
Source132: %{_urlprefix}/kde-l10n/kde-l10n-nds-%{version}.tar.bz2
# Source132-md5:	b9ba68900b0b1b87a388aefac769b77f
Source133: %{_urlprefix}/kde-l10n/kde-l10n-nl-%{version}.tar.bz2
# Source133-md5:	bfd62b4b1d4d943b989c5daf73412b2e
Source134: %{_urlprefix}/kde-l10n/kde-l10n-nn-%{version}.tar.bz2
# Source134-md5:	4bf2aab74f59a69b6651462022294d46
Source135: %{_urlprefix}/kde-l10n/kde-l10n-pa-%{version}.tar.bz2
# Source135-md5:	07c83920095b8eb2cc7efe7b0d1e983a
Source136: %{_urlprefix}/kde-l10n/kde-l10n-pl-%{version}.tar.bz2
# Source136-md5:	bd7604f6da9234b853d80570d5180ecb
Source137: %{_urlprefix}/kde-l10n/kde-l10n-pt-%{version}.tar.bz2
# Source137-md5:	0ac92f7e05710d9506d104b33251fd0e
Source138: %{_urlprefix}/kde-l10n/kde-l10n-pt_BR-%{version}.tar.bz2
# Source138-md5:	787a321c5f3d6fc1436419976dd8b7d3
Source139: %{_urlprefix}/kde-l10n/kde-l10n-ro-%{version}.tar.bz2
# Source139-md5:	e7df86710cb0606b2c3a85387d5ffeb0
Source140: %{_urlprefix}/kde-l10n/kde-l10n-ru-%{version}.tar.bz2
# Source140-md5:	25e8ae00b670bf21458bca80db8b72cd
Source141: %{_urlprefix}/kde-l10n/kde-l10n-sk-%{version}.tar.bz2
# Source141-md5:	fb8c8f710b0eb209318252accf5cf84b
Source142: %{_urlprefix}/kde-l10n/kde-l10n-sl-%{version}.tar.bz2
# Source142-md5:	85183b944d22b07a02d221c81f2df30a
Source143: %{_urlprefix}/kde-l10n/kde-l10n-sr-%{version}.tar.bz2
# Source143-md5:	53bbca44ec05ed24a0f352b05cd08ff3
Source144: %{_urlprefix}/kde-l10n/kde-l10n-sv-%{version}.tar.bz2
# Source144-md5:	f410e40782d072b760184c6f9ba29c22
Source145: %{_urlprefix}/kde-l10n/kde-l10n-th-%{version}.tar.bz2
# Source145-md5:	a03ecde05b081c495c225cb9fb733d14
Source146: %{_urlprefix}/kde-l10n/kde-l10n-tr-%{version}.tar.bz2
# Source146-md5:	32b980da8f31a736770bfdf2b4ecc61c
Source147: %{_urlprefix}/kde-l10n/kde-l10n-ug-%{version}.tar.bz2
# Source147-md5:	e470c05f788c412a68edf61e3bd41d22
Source148: %{_urlprefix}/kde-l10n/kde-l10n-uk-%{version}.tar.bz2
# Source148-md5:	b529656cc1b28cf1beec47ecab4799ff
Source149: %{_urlprefix}/kde-l10n/kde-l10n-wa-%{version}.tar.bz2
# Source149-md5:	883bf31279b2a406c54f99f6c681f67f
Source150: %{_urlprefix}/kde-l10n/kde-l10n-zh_CN-%{version}.tar.bz2
# Source150-md5:	3958339f7f8eb7f9ed888dfe8fafa0a6
Source151: %{_urlprefix}/kde-l10n/kde-l10n-zh_TW-%{version}.tar.bz2
# Source151-md5:	5d57f811033176f76cab815c50461838
%endif
%if %{with koffice}
Source68:	%{_urlprefix}/koffice-%{kofficever}/koffice-%{kofficever}.tar.bz2
# Source68-md5:	24331c3cf0a733ba7bbef3d9eab92d80
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
