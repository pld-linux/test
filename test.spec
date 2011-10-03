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
Version:	4.7.2
Release:	1
License:	GPL
Group:		Networking/Hacking
Source100:	kde4diff.sh
# Source100-md5:	
Source0: %{_urlprefix}/blinken-%{version}.tar.bz2
# Source0-md5:	e403f14a7c991fef7436fbf2d69baff7
Source1: %{_urlprefix}/cantor-%{version}.tar.bz2
# Source1-md5:	39b757fdf0557d9f9114442dd4d5488f
Source2: %{_urlprefix}/gwenview-%{version}.tar.bz2
# Source2-md5:	91994e664773c78bb2d8b595b7ed724f
Source3: %{_urlprefix}/kalgebra-%{version}.tar.bz2
# Source3-md5:	3559e22a282b2dc86e95c86c1f198a27
Source4: %{_urlprefix}/kalzium-%{version}.tar.bz2
# Source4-md5:	770dd180516ef4e39c698221c706bd07
Source5: %{_urlprefix}/kamera-%{version}.tar.bz2
# Source5-md5:	aa73158bceaa64a76faef9a0dda74d6a
Source6: %{_urlprefix}/kanagram-%{version}.tar.bz2
# Source6-md5:	955c0223704db39dbea540fc5f59c1c6
Source7: %{_urlprefix}/kate-%{version}.tar.bz2
# Source7-md5:	76fec4bc11a4cbc74051d2ce8e4171b8
Source8: %{_urlprefix}/kbruch-%{version}.tar.bz2
# Source8-md5:	437a7934682f0b687d18a1f8fbdb5d3f
Source9: %{_urlprefix}/kcolorchooser-%{version}.tar.bz2
# Source9-md5:	b812ba74b8c3c452626d00c9308fd41a
Source10: %{_urlprefix}/kde-baseapps-%{version}.tar.bz2
# Source10-md5:	19759a0700bfb0a7e8af6e07bed3a60b
Source11: %{_urlprefix}/kde-runtime-%{version}.tar.bz2
# Source11-md5:	16b11a96a7ad0b3c0a7175beb1fa943f
Source12: %{_urlprefix}/kde-wallpapers-%{version}.tar.bz2
# Source12-md5:	5de1aa547416d704679b154cc8eb3b36
Source13: %{_urlprefix}/kde-workspace-%{version}.tar.bz2
# Source13-md5:	53a2058c17c19d64bd2de6ee798b5402
#Source14: %{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source14-md5:	0713f18f7d9ccbfb7d8e045ac9e195cc
Source15: %{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source15-md5:	a436fafadc302f82d80c5aca115af48b
Source16: %{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source16-md5:	492c30d4227b395d6826d9ccc70a2796
Source17: %{_urlprefix}/kdegames-%{version}.tar.bz2
# Source17-md5:	92b25760dc30c332d1f267f479d9c884
Source18: %{_urlprefix}/kdegraphics-strigi-analyzer-%{version}.tar.bz2
# Source18-md5:	b9573b6b035cd66dfcef452a6815c29e
Source19: %{_urlprefix}/kdegraphics-thumbnailers-%{version}.tar.bz2
# Source19-md5:	cb4e19c485fe6ce8537a47e257ebee81
Source20: %{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source20-md5:	abe4c8f848366bcab16c57bbaeb86f1f
Source21: %{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source21-md5:	f95d23b09d207ef6d04d9e9f5cd6b22f
Source22: %{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source22-md5:	c1c33c100a0f7e64ffba0ae96d799152
Source23: %{_urlprefix}/kdepim-%{version}.tar.bz2
# Source23-md5:	0042ec48bb369d8f75173c32e7cda171
Source24: %{_urlprefix}/kdepim-runtime-%{version}.tar.bz2
# Source24-md5:	b8d8ce16400360989ffb7fe73c903924
Source25: %{_urlprefix}/kdepimlibs-%{version}.tar.bz2
# Source25-md5:	36a6e357b2420c3065ce96af4d82416c
Source26: %{_urlprefix}/kdeplasma-addons-%{version}.tar.bz2
# Source26-md5:	0805d8538efe0861b0590874c1a5f7af
Source27: %{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source27-md5:	228c5d6b7fbdf4112d27c4ee26eadb30
Source28: %{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source28-md5:	feba907d9797f445945e3521624ac184
#Source29: %{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source29-md5:	346d3e6a7fbce8f2359bfc3ce28941f3
Source30: %{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source30-md5:	f25fdacd5118a320a5d01bb8df34debb
Source31: %{_urlprefix}/kgamma-%{version}.tar.bz2
# Source31-md5:	810d933d7e7b637558a5333b52818db9
Source32: %{_urlprefix}/kgeography-%{version}.tar.bz2
# Source32-md5:	62c679f42adcba4f397f23378293b667
Source33: %{_urlprefix}/khangman-%{version}.tar.bz2
# Source33-md5:	5726500440e526e233ca5d42b1c1ca88
Source34: %{_urlprefix}/kig-%{version}.tar.bz2
# Source34-md5:	5df3ecc943157679f6190c130afe1a16
Source35: %{_urlprefix}/kimono-%{version}.tar.bz2
# Source35-md5:	9795128a06cc62a8b3501865fa2a6fa1
Source36: %{_urlprefix}/kiten-%{version}.tar.bz2
# Source36-md5:	3d96ab1ca77ea9ee18873bd042926e7d
Source37: %{_urlprefix}/klettres-%{version}.tar.bz2
# Source37-md5:	457dda788d5d773304aa439a5659a083
Source38: %{_urlprefix}/kmplot-%{version}.tar.bz2
# Source38-md5:	8ae5fe99cc12ee4affc68776a2431b80
Source39: %{_urlprefix}/kolourpaint-%{version}.tar.bz2
# Source39-md5:	89b2668496dab43f7971228b9c2e616e
Source40: %{_urlprefix}/konsole-%{version}.tar.bz2
# Source40-md5:	21c2c5715f04fed122cd2c22142e3624
Source41: %{_urlprefix}/korundum-%{version}.tar.bz2
# Source41-md5:	8d743627fe038edfde967535b4033ee9
Source42: %{_urlprefix}/kross-interpreters-%{version}.tar.bz2
# Source42-md5:	cc3b01fa53e6508c8db60a8699a39aee
Source43: %{_urlprefix}/kruler-%{version}.tar.bz2
# Source43-md5:	e2ca2f76b8a403fa0bebad2e10dbc0c0
Source44: %{_urlprefix}/ksaneplugin-%{version}.tar.bz2
# Source44-md5:	a8281e772efd66ce4fb01e7a3a09af94
Source45: %{_urlprefix}/ksnapshot-%{version}.tar.bz2
# Source45-md5:	3dc87fa57e770ca1a6e2a7a61fa4d228
Source46: %{_urlprefix}/kstars-%{version}.tar.bz2
# Source46-md5:	f2f682de2e03a4e56ffd9f6cc8e144c1
Source47: %{_urlprefix}/ktouch-%{version}.tar.bz2
# Source47-md5:	a86b76b1be866fcdbd7f8aebbfceff0e
Source48: %{_urlprefix}/kturtle-%{version}.tar.bz2
# Source48-md5:	45682da6474b8f93245e0dfaca106ab1
Source49: %{_urlprefix}/kwordquiz-%{version}.tar.bz2
# Source49-md5:	b56c39c0590db9af05fc6b3efe2e8bc8
Source50: %{_urlprefix}/libkdcraw-%{version}.tar.bz2
# Source50-md5:	b12b98af3cfebe8fb4087472a2f29177
Source51: %{_urlprefix}/libkdeedu-%{version}.tar.bz2
# Source51-md5:	c746d2e0b0b745c668ad165b8dd15fa0
Source52: %{_urlprefix}/libkexiv2-%{version}.tar.bz2
# Source52-md5:	ad22b866be0d35d8d1f2e6bd4be9f18e
Source53: %{_urlprefix}/libkipi-%{version}.tar.bz2
# Source53-md5:	7c0b1475af23d05bdff7bc9a65f98863
Source54: %{_urlprefix}/libksane-%{version}.tar.bz2
# Source54-md5:	1b238a2bdf5b804726983542e5fb0ec3
Source55: %{_urlprefix}/marble-%{version}.tar.bz2
# Source55-md5:	a7512fdd4571a57d36afafc13fa61f17
Source56: %{_urlprefix}/mobipocket-%{version}.tar.bz2
# Source56-md5:	e10217ccb05eceaa1bc97c10e09f4072
Source57: %{_urlprefix}/okular-%{version}.tar.bz2
# Source57-md5:	6d61d0306243f917d8b29e9183a67d39
Source58: %{_urlprefix}/oxygen-icons-%{version}.tar.bz2
# Source58-md5:	d0edab3fd9b37e6ca19f07e3f74ae790
Source59: %{_urlprefix}/parley-%{version}.tar.bz2
# Source59-md5:	56be5e0e3efc8432c12ec0ebe5385de1
Source60: %{_urlprefix}/perlkde-%{version}.tar.bz2
# Source60-md5:	685e62e0038a1efa180ac88592d683e1
Source61: %{_urlprefix}/perlqt-%{version}.tar.bz2
# Source61-md5:	e66a2766dab309f47df9210ac992787d
Source62: %{_urlprefix}/pykde4-%{version}.tar.bz2
# Source62-md5:	ef6d6ed6fad649a20de780e8d145a66f
Source63: %{_urlprefix}/qtruby-%{version}.tar.bz2
# Source63-md5:	bbc3de55ec7bfc215779ac76969f5cce
Source64: %{_urlprefix}/qyoto-%{version}.tar.bz2
# Source64-md5:	0519e56ab8c1a3287b1726ceffa891e0
Source65: %{_urlprefix}/rocs-%{version}.tar.bz2
# Source65-md5:	5aa9f184211536e6466c55074c08307e
Source66: %{_urlprefix}/smokegen-%{version}.tar.bz2
# Source66-md5:	74f9a61c7b9745dc7cf215447b0c6619
Source67: %{_urlprefix}/smokekde-%{version}.tar.bz2
# Source67-md5:	d4982270a8107749fc0057ad77892350
Source68: %{_urlprefix}/smokeqt-%{version}.tar.bz2
# Source68-md5:	3f13460b3ea5b553212b79bf425ec4b1
Source69: %{_urlprefix}/step-%{version}.tar.bz2
# Source69-md5:	b052c83dd8e1387095434a27e59494e5
Source70: %{_urlprefix}/svgpart-%{version}.tar.bz2
# Source70-md5:	b80b68892fd2082b18296cf1a286c945
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
# Source68-md5:	3f13460b3ea5b553212b79bf425ec4b1
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
