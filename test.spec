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
Version:	4.7.4
Release:	1
License:	GPL
Group:		Networking/Hacking
Source100:	kde4diff.sh
# Source100-md5:	
Source0: %{_urlprefix}/blinken-%{version}.tar.bz2
# Source0-md5:	059689341598c0a43a9369f47415adaf
Source1: %{_urlprefix}/cantor-%{version}.tar.bz2
# Source1-md5:	041e2703cfb8bab4399306b38af0a84b
Source2: %{_urlprefix}/gwenview-%{version}.tar.bz2
# Source2-md5:	65520b2e83b401c926913f88bde6c9a1
Source3: %{_urlprefix}/kalgebra-%{version}.tar.bz2
# Source3-md5:	6e1e4c24c342630026812e5e2e5f3b6b
Source4: %{_urlprefix}/kalzium-%{version}.tar.bz2
# Source4-md5:	73a38220f4b973f45da6134d8b8dcbb7
Source5: %{_urlprefix}/kamera-%{version}.tar.bz2
# Source5-md5:	5977355fb1dd14197fc78d5b90a6680c
Source6: %{_urlprefix}/kanagram-%{version}.tar.bz2
# Source6-md5:	6459c04804a58111b825c658f4bc5439
Source7: %{_urlprefix}/kate-%{version}.tar.bz2
# Source7-md5:	565ebff0d1e2316097897149eeb4d255
Source8: %{_urlprefix}/kbruch-%{version}.tar.bz2
# Source8-md5:	39f6eaf063e31aef694df30ce998396e
Source9: %{_urlprefix}/kcolorchooser-%{version}.tar.bz2
# Source9-md5:	9a66ae51f42f681344664efb87645e38
Source10: %{_urlprefix}/kde-baseapps-%{version}.tar.bz2
# Source10-md5:	d44310cad99a9afb757ff13f24eeae32
Source11: %{_urlprefix}/kde-runtime-%{version}.tar.bz2
# Source11-md5:	8e6af5f464ae06e3b7cbfd73aa9f7971
Source12: %{_urlprefix}/kde-wallpapers-%{version}.tar.bz2
# Source12-md5:	e3606013a1406ba87293aa5948a6c123
Source13: %{_urlprefix}/kde-workspace-%{version}.tar.bz2
# Source13-md5:	42492b9669b1bb8d549b59223b8732cb
Source14: %{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source14-md5:	8cad28a2e76f020f7aaca2709447f5f9
Source15: %{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source15-md5:	890660c26e177187106144d52741437f
Source16: %{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source16-md5:	5a287460b09252853276ad6644753326
Source17: %{_urlprefix}/kdegames-%{version}.tar.bz2
# Source17-md5:	0446dcecc7723a3df0324d394327b984
Source18: %{_urlprefix}/kdegraphics-strigi-analyzer-%{version}.tar.bz2
# Source18-md5:	5489ad5a410636b994bbd7660814f796
Source19: %{_urlprefix}/kdegraphics-thumbnailers-%{version}.tar.bz2
# Source19-md5:	cf1fb62fa3f9668406a1a27c3cc3b8d2
Source20: %{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source20-md5:	46baa210a6f5a0d6af4b7602a4b00994
Source21: %{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source21-md5:	64dc14f2b964b9e5b412090b046a0268
Source22: %{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source22-md5:	e180222d932c64574ba5b8ef31e6bb86
Source23: %{_urlprefix}/kdepim-%{version}.tar.bz2
# Source23-md5:	fd197859ad0f3c55a175133c2a7b6c47
Source24: %{_urlprefix}/kdepim-runtime-%{version}.tar.bz2
# Source24-md5:	fff04e1be1ffb8047fc8c5a395b79efb
Source25: %{_urlprefix}/kdepimlibs-%{version}.tar.bz2
# Source25-md5:	ccc9d9ec4173e5627623d93207fdf318
Source26: %{_urlprefix}/kdeplasma-addons-%{version}.tar.bz2
# Source26-md5:	57b6c3ee0bed9c0c2190308a4e690e39
Source27: %{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source27-md5:	13e9015de83969b478e1b21ac6a901b2
Source28: %{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source28-md5:	e596142c0d8c8622aa2577c3990b2293
Source29: %{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source29-md5:	7df8a48c48851cb0438acbbf727be396
Source30: %{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source30-md5:	6608ace1b8b35ec12e0a2d3644d66e71
Source31: %{_urlprefix}/kgamma-%{version}.tar.bz2
# Source31-md5:	8d2a5b123b6f07e60bce0064de6b1e1d
Source32: %{_urlprefix}/kgeography-%{version}.tar.bz2
# Source32-md5:	4a468d620e9e4ed8bb1356bed6765842
Source33: %{_urlprefix}/khangman-%{version}.tar.bz2
# Source33-md5:	5988daa03e87648ff200ff4fccdeedf7
Source34: %{_urlprefix}/kig-%{version}.tar.bz2
# Source34-md5:	e56ec698d84035046794897c523f2386
Source35: %{_urlprefix}/kimono-%{version}.tar.bz2
# Source35-md5:	d9eabf628c4f418421fa8e299410f500
Source36: %{_urlprefix}/kiten-%{version}.tar.bz2
# Source36-md5:	8dc39396c5f19873c5fbd86d184ffc32
Source37: %{_urlprefix}/klettres-%{version}.tar.bz2
# Source37-md5:	d818029a2e8751740cd32d7b42e4ae39
Source38: %{_urlprefix}/kmplot-%{version}.tar.bz2
# Source38-md5:	dc71089f2f2bfdc9005d315ab2f39eb8
Source39: %{_urlprefix}/kolourpaint-%{version}.tar.bz2
# Source39-md5:	ab8e29ab4047e3842741d76136a3bfaf
Source40: %{_urlprefix}/konsole-%{version}.tar.bz2
# Source40-md5:	c3828a382cb83b8d3c4e1ffcedb16172
Source41: %{_urlprefix}/korundum-%{version}.tar.bz2
# Source41-md5:	e9c032831d3b0c5fc2f16b1111927276
Source42: %{_urlprefix}/kross-interpreters-%{version}.tar.bz2
# Source42-md5:	e512693d2e183b4c6029233489583031
Source43: %{_urlprefix}/kruler-%{version}.tar.bz2
# Source43-md5:	5a11d5f1ee9aa09273966321e5533d8f
Source44: %{_urlprefix}/ksaneplugin-%{version}.tar.bz2
# Source44-md5:	0b39c9abf4ed2253965e7b9fd11bd5ab
Source45: %{_urlprefix}/ksnapshot-%{version}.tar.bz2
# Source45-md5:	41ab4f1375b59053610fb7f981d14f02
Source46: %{_urlprefix}/kstars-%{version}.tar.bz2
# Source46-md5:	d1b753e798202d2bf9cac76b552608ac
Source47: %{_urlprefix}/ktouch-%{version}.tar.bz2
# Source47-md5:	fa6e1ca2d1f4e6585a766bb75befee84
Source48: %{_urlprefix}/kturtle-%{version}.tar.bz2
# Source48-md5:	15b2eadc2b140b7e487a138bc293c9b2
Source49: %{_urlprefix}/kwordquiz-%{version}.tar.bz2
# Source49-md5:	2c926e6c6715387b9cb5ae4d279e66ef
Source50: %{_urlprefix}/libkdcraw-%{version}.tar.bz2
# Source50-md5:	e7f91cd5280582590908a5bc1e979021
Source51: %{_urlprefix}/libkdeedu-%{version}.tar.bz2
# Source51-md5:	81812b255f159926f4d8a6c14b572bc9
Source52: %{_urlprefix}/libkexiv2-%{version}.tar.bz2
# Source52-md5:	251e7eb95eb5353a821479fc233b4b0f
Source53: %{_urlprefix}/libkipi-%{version}.tar.bz2
# Source53-md5:	570785645994e45a3c7eaa122cd1350e
Source54: %{_urlprefix}/libksane-%{version}.tar.bz2
# Source54-md5:	8d08cea522f9ff4417c3a17e95aa3ef5
Source55: %{_urlprefix}/marble-%{version}.tar.bz2
# Source55-md5:	77d6be4dd6de1a81551c525ba93a409e
Source56: %{_urlprefix}/mobipocket-%{version}.tar.bz2
# Source56-md5:	8b57cc0aac4ce5bf43805b2921c97cd2
Source57: %{_urlprefix}/okular-%{version}.tar.bz2
# Source57-md5:	bc3062761bb427fba5953e2b637589ab
Source58: %{_urlprefix}/oxygen-icons-%{version}.tar.bz2
# Source58-md5:	1ab8d750781249d84becca7f7eb988ed
Source59: %{_urlprefix}/parley-%{version}.tar.bz2
# Source59-md5:	87fa53544eb170b3098e50ec8fa11c0d
Source60: %{_urlprefix}/perlkde-%{version}.tar.bz2
# Source60-md5:	64d4a74c3348f5e6b9c560b1f298de17
Source61: %{_urlprefix}/perlqt-%{version}.tar.bz2
# Source61-md5:	a2ae28a62e28ed9ae21fac8624095f8e
Source62: %{_urlprefix}/pykde4-%{version}.tar.bz2
# Source62-md5:	600ca5b316be23a3b8dc9c74b9e97b2e
Source63: %{_urlprefix}/qtruby-%{version}.tar.bz2
# Source63-md5:	5e618d2450e2507a6e69494b64e404c5
Source64: %{_urlprefix}/qyoto-%{version}.tar.bz2
# Source64-md5:	85a89969a04a97ad55f5645c77f06fb9
Source65: %{_urlprefix}/rocs-%{version}.tar.bz2
# Source65-md5:	a109b02d4ba00f359c274a80ebc34b62
Source66: %{_urlprefix}/smokegen-%{version}.tar.bz2
# Source66-md5:	4829045c88c608de8484ea8386fe77a0
Source67: %{_urlprefix}/smokekde-%{version}.tar.bz2
# Source67-md5:	4aaba02db3cb655fe4627b731b73b06e
Source68: %{_urlprefix}/smokeqt-%{version}.tar.bz2
# Source68-md5:	9ec2838d6943f6fd2101cdaf8768dd36
Source69: %{_urlprefix}/step-%{version}.tar.bz2
# Source69-md5:	f1ad2a2d7e2b616b1c9b3e03c848b189
Source70: %{_urlprefix}/svgpart-%{version}.tar.bz2
# Source70-md5:	da8db422ed3212e693d73fca63c89adf
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
# Source68-md5:	9ec2838d6943f6fd2101cdaf8768dd36
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
