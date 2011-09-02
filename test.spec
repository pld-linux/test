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
Version:	4.7.1
Release:	1
License:	GPL
Group:		Networking/Hacking
Source100:	kde4diff.sh
# Source100-md5:	
Source0: %{_urlprefix}/blinken-%{version}.tar.bz2
# Source0-md5:	188ff5ff5ca53a4383c919eec9299fbe
Source1: %{_urlprefix}/cantor-%{version}.tar.bz2
# Source1-md5:	b2f1a3ae4fdc0f04f0cd250a8dbd6d76
Source2: %{_urlprefix}/gwenview-%{version}.tar.bz2
# Source2-md5:	54a419ec211ac09f9cc1a70d5556f2cd
Source3: %{_urlprefix}/kalgebra-%{version}.tar.bz2
# Source3-md5:	5ed2c0a4ba7e2792f33c36d4d82dbbdf
Source4: %{_urlprefix}/kalzium-%{version}.tar.bz2
# Source4-md5:	929ba3e612cbb998aa0b8410d89dcd7e
Source5: %{_urlprefix}/kamera-%{version}.tar.bz2
# Source5-md5:	4f5669536561f1125f9fc3f12c501fd8
Source6: %{_urlprefix}/kanagram-%{version}.tar.bz2
# Source6-md5:	a0643cbf4b8bb6a992f73e85263a8b45
Source7: %{_urlprefix}/kate-%{version}.tar.bz2
# Source7-md5:	68edb488a616cc4bb41475ee129a22c3
Source8: %{_urlprefix}/kbruch-%{version}.tar.bz2
# Source8-md5:	95a186add683373cdae592e259a250ae
Source9: %{_urlprefix}/kcolorchooser-%{version}.tar.bz2
# Source9-md5:	9b8074f7362a6ad4a35fbebb0156a0f1
Source10: %{_urlprefix}/kde-l10n/kde-baseapps-%{version}.tar.bz2
# Source10-md5:	f477884f2c25ea23a69b74a2f675c8f6
Source11: %{_urlprefix}/kde-l10n/kde-runtime-%{version}.tar.bz2
# Source11-md5:	927c47f79000f7af66b845600a21e9f5
Source12: %{_urlprefix}/kde-l10n/kde-wallpapers-%{version}.tar.bz2
# Source12-md5:	643eade621034d84803db793089a9c24
Source13: %{_urlprefix}/kde-l10n/kde-workspace-%{version}.tar.bz2
# Source13-md5:	128738157adc30030aa590f90109dbb9
Source14: %{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source14-md5:	0713f18f7d9ccbfb7d8e045ac9e195cc
Source15: %{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source15-md5:	b50211eb643bb32159e2321ba6b44416
Source16: %{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source16-md5:	ba3037537e8a2184a80e9d384ecc3302
Source17: %{_urlprefix}/kdegames-%{version}.tar.bz2
# Source17-md5:	ca9d63f2034a674e771ca4f9036308ec
Source18: %{_urlprefix}/kdegraphics-strigi-analyzer-%{version}.tar.bz2
# Source18-md5:	d58ea5426f38262543c5b38af0057172
Source19: %{_urlprefix}/kdegraphics-thumbnailers-%{version}.tar.bz2
# Source19-md5:	9d72b5d9179c7eb981dc7dd9b81ed841
Source20: %{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source20-md5:	eaeacc3c94501f343eb7c4ef74c7475b
Source21: %{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source21-md5:	730aabab1869e23715fd56ef6dbaa6be
Source22: %{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source22-md5:	9f6e2d00955a9fcbdf0afa71a91e3aa2
Source23: %{_urlprefix}/kdepim-%{version}.tar.bz2
# Source23-md5:	89b1f72b764bc3df4cf27b9afd36b324
Source24: %{_urlprefix}/kdepim-runtime-%{version}.tar.bz2
# Source24-md5:	c244c997c50ab5239ce2f6f0439cad6e
Source25: %{_urlprefix}/kdepimlibs-%{version}.tar.bz2
# Source25-md5:	14432a983e5e280470d04f7922a43bb1
Source26: %{_urlprefix}/kdeplasma-addons-%{version}.tar.bz2
# Source26-md5:	42e63b0e539dd1a4255b81d1cda770f6
Source27: %{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source27-md5:	9f7ddb6b219e095103cbe2848cc31d79
Source28: %{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source28-md5:	b6d5b199536080c20ab7fa26fdfdb9e7
Source29: %{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source29-md5:	346d3e6a7fbce8f2359bfc3ce28941f3
Source30: %{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source30-md5:	150bb976a06777c2bfe87beac6109956
Source31: %{_urlprefix}/kgamma-%{version}.tar.bz2
# Source31-md5:	524adb1b3c6c4bb9b3e50e1034983216
Source32: %{_urlprefix}/kgeography-%{version}.tar.bz2
# Source32-md5:	9600b1a5d788475fa38ebfdeee6536fc
Source33: %{_urlprefix}/khangman-%{version}.tar.bz2
# Source33-md5:	a7e0223ccb4f9d827e70627f5505588e
Source34: %{_urlprefix}/kig-%{version}.tar.bz2
# Source34-md5:	bf912d2f54e66406e2029b2eb5a45f7a
Source35: %{_urlprefix}/kimono-%{version}.tar.bz2
# Source35-md5:	673e41be49c6277f832450fa2ba5c698
Source36: %{_urlprefix}/kiten-%{version}.tar.bz2
# Source36-md5:	fe1ce1363da8b9aa754a31b843a5f906
Source37: %{_urlprefix}/klettres-%{version}.tar.bz2
# Source37-md5:	e3176f534baf92ba91100499966e17a8
Source38: %{_urlprefix}/kmplot-%{version}.tar.bz2
# Source38-md5:	8052a7295021485fb0a1ca2c7e657e80
Source39: %{_urlprefix}/kolourpaint-%{version}.tar.bz2
# Source39-md5:	adfe49a6bf61a4996a2abb589888f380
Source40: %{_urlprefix}/konsole-%{version}.tar.bz2
# Source40-md5:	009bd5f40ca86e48ef2cec795dd87262
Source41: %{_urlprefix}/korundum-%{version}.tar.bz2
# Source41-md5:	3e175c5dc5f4ab803c111dfd55cebc2d
Source42: %{_urlprefix}/kross-interpreters-%{version}.tar.bz2
# Source42-md5:	6d0cbe5f268fc65e5050833822e8a55c
Source43: %{_urlprefix}/kruler-%{version}.tar.bz2
# Source43-md5:	392304d7e1b2e5fefd2f9fbd8e721767
Source44: %{_urlprefix}/ksaneplugin-%{version}.tar.bz2
# Source44-md5:	2dc4a2fdb1e340b139d84b6d45bac38f
Source45: %{_urlprefix}/ksnapshot-%{version}.tar.bz2
# Source45-md5:	2f080edabaef56718121fe2f9abaa3ea
Source46: %{_urlprefix}/kstars-%{version}.tar.bz2
# Source46-md5:	fe243613d628e28371ea4986f2312d70
Source47: %{_urlprefix}/ktouch-%{version}.tar.bz2
# Source47-md5:	f6b657df0b46190122148e9c418ae060
Source48: %{_urlprefix}/kturtle-%{version}.tar.bz2
# Source48-md5:	1918f53d284bfe12da45c5dad9651445
Source49: %{_urlprefix}/kwordquiz-%{version}.tar.bz2
# Source49-md5:	399949f9e32ba74512b7af47243a30ad
Source50: %{_urlprefix}/libkdcraw-%{version}.tar.bz2
# Source50-md5:	9501a948515d024a12f7ba6cf551bea2
Source51: %{_urlprefix}/libkdeedu-%{version}.tar.bz2
# Source51-md5:	d4ae1f0d640c9f8fb8db6b0f4a3def10
Source52: %{_urlprefix}/libkexiv2-%{version}.tar.bz2
# Source52-md5:	78940384d4d194cc82f26f73187234d1
Source53: %{_urlprefix}/libkipi-%{version}.tar.bz2
# Source53-md5:	08ed8a97c28abc766aed1a337bd8087b
Source54: %{_urlprefix}/libksane-%{version}.tar.bz2
# Source54-md5:	cd85b7423e90ed2e9a9d53c1d3cad94c
Source55: %{_urlprefix}/marble-%{version}.tar.bz2
# Source55-md5:	c51019621e91c53b1ded13eb2cfc76c0
Source56: %{_urlprefix}/mobipocket-%{version}.tar.bz2
# Source56-md5:	01aff9d17d452379d471bc22ed6a9902
Source57: %{_urlprefix}/okular-%{version}.tar.bz2
# Source57-md5:	da745b0d3ee2e796894fbb56caae7461
Source58: %{_urlprefix}/oxygen-icons-%{version}.tar.bz2
# Source58-md5:	76472c5e3f92840fcf19ab0223a21b66
Source59: %{_urlprefix}/parley-%{version}.tar.bz2
# Source59-md5:	e707e690bdf4b766914391a517f6c698
Source60: %{_urlprefix}/perlkde-%{version}.tar.bz2
# Source60-md5:	ba81c4a305cf86aa3eea4117f6633c04
Source61: %{_urlprefix}/perlqt-%{version}.tar.bz2
# Source61-md5:	2f21df2a106d33c4ec626568e9c1d506
Source62: %{_urlprefix}/pykde4-%{version}.tar.bz2
# Source62-md5:	53fc1c1e1bacb1600a82c94352348fdd
Source63: %{_urlprefix}/qtruby-%{version}.tar.bz2
# Source63-md5:	c498021117270962db9b9afae0d24adb
Source64: %{_urlprefix}/qyoto-%{version}.tar.bz2
# Source64-md5:	7c81786e0f80353d8fd7e11ce4471272
Source65: %{_urlprefix}/rocs-%{version}.tar.bz2
# Source65-md5:	35e2f6d4cf74884a74afdaab3a80a276
Source66: %{_urlprefix}/smokegen-%{version}.tar.bz2
# Source66-md5:	b346f945d559e47dd6fcef8c7e8dcc71
Source67: %{_urlprefix}/smokekde-%{version}.tar.bz2
# Source67-md5:	959ecaf7d268072a93477f309d763ff5
Source68: %{_urlprefix}/smokeqt-%{version}.tar.bz2
# Source68-md5:	147d73b6f05105ebacd4d8c2f316254c
Source69: %{_urlprefix}/step-%{version}.tar.bz2
# Source69-md5:	070fac7e16f5c5d3f471f0204dfb3052
Source70: %{_urlprefix}/svgpart-%{version}.tar.bz2
# Source70-md5:	1bffaac4d9c6c9f1d04377621dff224d
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
# Source68-md5:	147d73b6f05105ebacd4d8c2f316254c
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
