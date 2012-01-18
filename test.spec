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
Source0: %{_urlprefix}/blinken-%{version}.tar.bz2
# Source0-md5:	0dba841a998fec4ada7fbf068d0c38b0
Source1: %{_urlprefix}/cantor-%{version}.tar.bz2
# Source1-md5:	aa2e06f133615d44143cf6ad6da52aaf
Source2: %{_urlprefix}/gwenview-%{version}.tar.bz2
# Source2-md5:	d6339e29d9731dace7bb52f86e99a30e
Source3: %{_urlprefix}/kalgebra-%{version}.tar.bz2
# Source3-md5:	8d5ff9c91c0203c3608af10eeb67195c
Source4: %{_urlprefix}/kalzium-%{version}.tar.bz2
# Source4-md5:	9da1db7aca2bc178c11549598a02a3fb
Source5: %{_urlprefix}/kamera-%{version}.tar.bz2
# Source5-md5:	2d7340b1215c24d1e98875c5eea4d54d
Source6: %{_urlprefix}/kanagram-%{version}.tar.bz2
# Source6-md5:	e4768621391911542d2986a3571a0c3f
Source7: %{_urlprefix}/kate-%{version}.tar.bz2
# Source7-md5:	abe76125a855e91c2c86849cbf1b8350
Source8: %{_urlprefix}/kbruch-%{version}.tar.bz2
# Source8-md5:	898ee167ac04a5945f4d90191aa1bea9
Source9: %{_urlprefix}/kcolorchooser-%{version}.tar.bz2
# Source9-md5:	48ede55e885819143f229c1f6bb2d388
Source10: %{_urlprefix}/kde-baseapps-%{version}.tar.bz2
# Source10-md5:	6d3f3d4e030aa2aa690b6fc3124b5832
Source11: %{_urlprefix}/kde-runtime-%{version}.tar.bz2
# Source11-md5:	571563f6ab330348d3f917abdf9c69e4
Source12: %{_urlprefix}/kde-wallpapers-%{version}.tar.bz2
# Source12-md5:	396aa669ab31ab32f73f2278e6ca143a
Source13: %{_urlprefix}/kde-workspace-%{version}.tar.bz2
# Source13-md5:	4a80d477c659bc1fed4c1829065db01b
#Source14: %{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
## Source14-md5:	8cad28a2e76f020f7aaca2709447f5f9
Source15: %{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source15-md5:	4ae902b75b009bd7dca5e8d1423c0fc4
Source16: %{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source16-md5:	19f5f7c2294deae9741a6cd70005cc4a
Source17: %{_urlprefix}/kdegames-%{version}.tar.bz2
# Source17-md5:	20d3b5ead912bc8d6d326cdb305f1b90
Source18: %{_urlprefix}/kdegraphics-strigi-analyzer-%{version}.tar.bz2
# Source18-md5:	f25df7e81603bcb02c4246eef3826381
Source19: %{_urlprefix}/kdegraphics-thumbnailers-%{version}.tar.bz2
# Source19-md5:	3676f3f233968b12d1bdac40931dde30
Source20: %{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source20-md5:	c19858c68f9a209ae521d7fb3c34747b
Source21: %{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source21-md5:	b1217b735e6ac8abce1b6423601e1be3
Source22: %{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source22-md5:	4fc00a35dc3f0b3b06a2b6be3086563d
Source23: %{_urlprefix}/kdepim-%{version}.tar.bz2
# Source23-md5:	9e74dce1f43382bfc33aa1c6bfc3519c
Source24: %{_urlprefix}/kdepim-runtime-%{version}.tar.bz2
# Source24-md5:	3a45035530a440652ecf69548334efbc
Source25: %{_urlprefix}/kdepimlibs-%{version}.tar.bz2
# Source25-md5:	9ebb57b689a874c7853b7dfa83af4c9d
Source26: %{_urlprefix}/kdeplasma-addons-%{version}.tar.bz2
# Source26-md5:	5b2947ef92fc04aecca8af4393336265
Source27: %{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source27-md5:	a5a1265a74c5a73cf39d65cad0bd4bd4
Source28: %{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source28-md5:	71856659db5cf9333499e06f24c0135e
#Source29: %{_urlprefix}/kdeutils-%{version}.tar.bz2
## Source29-md5:	7df8a48c48851cb0438acbbf727be396
Source30: %{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source30-md5:	d247fd36ece60bd9d6beaf8f5feb7a1f
Source31: %{_urlprefix}/kgamma-%{version}.tar.bz2
# Source31-md5:	34169d11b670944d7e373d61a220c95c
Source32: %{_urlprefix}/kgeography-%{version}.tar.bz2
# Source32-md5:	72d1154427723353ad76e48bfc753f02
Source33: %{_urlprefix}/khangman-%{version}.tar.bz2
# Source33-md5:	a738b368d9a8516bb75b0d84f3285258
Source34: %{_urlprefix}/kig-%{version}.tar.bz2
# Source34-md5:	2798cb1881a1fefbdc0f051db99cd2b5
Source35: %{_urlprefix}/kimono-%{version}.tar.bz2
# Source35-md5:	ad5d0e7b45a7b1900cfdeb969dc5d290
Source36: %{_urlprefix}/kiten-%{version}.tar.bz2
# Source36-md5:	cf787e0c3037a38a5e56f1927cee4693
Source37: %{_urlprefix}/klettres-%{version}.tar.bz2
# Source37-md5:	f60c9d948e03adcf9b87866c3e489b15
Source38: %{_urlprefix}/kmplot-%{version}.tar.bz2
# Source38-md5:	9922acd164d3b152551ad8a501e7e6a6
Source39: %{_urlprefix}/kolourpaint-%{version}.tar.bz2
# Source39-md5:	04129e9cdef1f964612a77b97c4bd9f3
Source40: %{_urlprefix}/konsole-%{version}.tar.bz2
# Source40-md5:	630da3df5545457f69e3aa86327b76b4
Source41: %{_urlprefix}/korundum-%{version}.tar.bz2
# Source41-md5:	5efef73e24ad15bafb894fb765f466d9
Source42: %{_urlprefix}/kross-interpreters-%{version}.tar.bz2
# Source42-md5:	d588c7afa24bb9fdd619737bdc61607f
Source43: %{_urlprefix}/kruler-%{version}.tar.bz2
# Source43-md5:	98036f7a77e914aaae3da9ca9d638806
Source44: %{_urlprefix}/ksaneplugin-%{version}.tar.bz2
# Source44-md5:	457a8a796937c7eda4e118d71f65a0fa
Source45: %{_urlprefix}/ksnapshot-%{version}.tar.bz2
# Source45-md5:	dfa82ee16987070b2150b9426dd2ac35
Source46: %{_urlprefix}/kstars-%{version}.tar.bz2
# Source46-md5:	3f87bdcb332e9e15c158b0fbeb134755
Source47: %{_urlprefix}/ktouch-%{version}.tar.bz2
# Source47-md5:	9a691e993c46253d2a087c15d0404c76
Source48: %{_urlprefix}/kturtle-%{version}.tar.bz2
# Source48-md5:	f14b8db9ee9516b7ce0779b6726c38ef
Source49: %{_urlprefix}/kwordquiz-%{version}.tar.bz2
# Source49-md5:	dc68a189fb8988f7889f29cc091c3de7
Source50: %{_urlprefix}/libkdcraw-%{version}.tar.bz2
# Source50-md5:	986fbbe46f0c17d45784593b18e6e31d
Source51: %{_urlprefix}/libkdeedu-%{version}.tar.bz2
# Source51-md5:	b984c0e5ea4d9101b150773f4d92c71f
Source52: %{_urlprefix}/libkexiv2-%{version}.tar.bz2
# Source52-md5:	87f69c9e04cb4c14d18c2c3404740f20
Source53: %{_urlprefix}/libkipi-%{version}.tar.bz2
# Source53-md5:	b0a84b23a17b2b71cf143b896a77936d
Source54: %{_urlprefix}/libksane-%{version}.tar.bz2
# Source54-md5:	864685ebe7bb7e7efcb1c9122b9b9d23
Source55: %{_urlprefix}/marble-%{version}.tar.bz2
# Source55-md5:	95c546f33706d8fcbef8a04b4b18a17f
Source56: %{_urlprefix}/kdegraphics-mobipocket-%{version}.tar.bz2
# Source56-md5:	a6e9fcc99189802d130d19824521ac42
Source57: %{_urlprefix}/okular-%{version}.tar.bz2
# Source57-md5:	6df57858c0138072b69945072d09978c
Source58: %{_urlprefix}/oxygen-icons-%{version}.tar.bz2
# Source58-md5:	2ae26ba235f207eb29677637c1d059a7
Source59: %{_urlprefix}/parley-%{version}.tar.bz2
# Source59-md5:	92608ce548515a53191705c94af46628
Source60: %{_urlprefix}/perlkde-%{version}.tar.bz2
# Source60-md5:	a85ad9879e3baeffed23d6d4d4bb0e24
Source61: %{_urlprefix}/perlqt-%{version}.tar.bz2
# Source61-md5:	b9a419ba264d12fa89a3fb0da5e9fa57
Source62: %{_urlprefix}/pykde4-%{version}.tar.bz2
# Source62-md5:	5f31743bebb879e537426dafb0b6d942
Source63: %{_urlprefix}/qtruby-%{version}.tar.bz2
# Source63-md5:	c78fdbd02f161025da5a08b83c47ac66
Source64: %{_urlprefix}/qyoto-%{version}.tar.bz2
# Source64-md5:	24a3727bdde0f54aff05825d0cc64cd4
Source65: %{_urlprefix}/rocs-%{version}.tar.bz2
# Source65-md5:	0c38086c47408b8470157d596f7ce221
Source66: %{_urlprefix}/smokegen-%{version}.tar.bz2
# Source66-md5:	8f3b232945720bf7c23239f4a1b2737d
Source67: %{_urlprefix}/smokekde-%{version}.tar.bz2
# Source67-md5:	c86cce394b795e0be5ebb25f428f3726
Source68: %{_urlprefix}/smokeqt-%{version}.tar.bz2
# Source68-md5:	7743457909c5e003ab5da3f6fd8d2a0d
Source69: %{_urlprefix}/step-%{version}.tar.bz2
# Source69-md5:	e476da52857ac1d753d821e4732c0126
Source70: %{_urlprefix}/svgpart-%{version}.tar.bz2
# Source70-md5:	17a325765568945ddbb12a391886b433
%if %{with l10n}
Source100: %{_urlprefix}/kde-l10n/kde-l10n-ar-%{version}.tar.bz2
# Source100-md5:	e335c913f721664dc383542367cdcbf2
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
# Source68-md5:	7743457909c5e003ab5da3f6fd8d2a0d
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
