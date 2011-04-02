# - easy way to update all sources with new/old locales:
#   lynx -dump http://carme.pld-linux.org/~arekm/kde/kde-l10n | awk -vi=19 '/4.1.0.tar.bz2$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   sed -i -e 's,http://carme.pld-linux.org/~arekm/kde/kde-l10n/,%{_urlprefix}/kde-l10n/,' out
#   sed -i -e 's,4.1.0,%{version},' out
#   and then :r out in vim and ./builder -a5 the spec
%bcond_with	l10n
%bcond_with	koffice
%define		_urlprefix	http://carme.pld-linux.org/~arekm/kde/
#%%define		_urlprefix	http://shadzik.nomeno.pl/kde4/
%define		kofficever	2.3.1
#%%define		_urlprefix	ftp://ftp.pbone.net/mirror/ftp.kde.org/pub/kde/unstable/%{version}/src
Summary:	Fetch KDE packages to distfiles
Name:		kdefetch
Version:	4.6.2
Release:	1
License:	GPL
Group:		Networking/Hacking
Source100:	kde4diff.sh
Source0:	%{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source0-md5:	c5eea7caa763bdd2a4c695eed2413006
Source1:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source1-md5:	f7011751bf9e8b33f6c2f7ed0de01a88
Source2:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source2-md5:	43ddb06238120efc29614d8268dc4dff
Source3:	%{_urlprefix}/kdebase-%{version}.tar.bz2
# Source3-md5:	80b02b96deb1057a7eff5ec691765110
Source4:	%{_urlprefix}/kdebase-runtime-%{version}.tar.bz2
# Source4-md5:	541029e6a62a8cecade97fb8106d17a8
Source5:	%{_urlprefix}/kdebase-workspace-%{version}.tar.bz2
# Source5-md5:	0cc795bb58aa4841b90717ee4436ce96
Source6:	%{_urlprefix}/kdebindings-%{version}.tar.bz2
# Source6-md5:	358272911af2bf1ff76aca8a43358047
Source7:	%{_urlprefix}/kdeedu-%{version}.tar.bz2
# Source7-md5:	282a7fdd582718575e376e033ec8a049
Source8:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source8-md5:	56f676e7bdb4475ea9ff9b08c443e919
Source9:	%{_urlprefix}/kdegraphics-%{version}.tar.bz2
# Source9-md5:	db3519433c9a91dbc4f1ba68d824d328
Source10:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source10-md5:	7439251b812dc520d4e6ed874036412c
#Source11:	%{_urlprefix}/kdepim-runtime-%{version}.tar.bz2
# Source11-md5:	63dff808a6a6d4b4467fddd3bfbfc0da
Source12:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source12-md5:	a6e067136af5a18dc69dc4b591eabe10
Source13:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source13-md5:	72952749d055f5323df06a6c2a3d3d8b
#Source14:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source14-md5:	aae69bbf54ffac3563f19a72b06f60b3
Source15:	%{_urlprefix}/kdepimlibs-%{version}.tar.bz2
# Source15-md5:	605ed6ca85da2d83605ab500b4b9441a
Source16:	%{_urlprefix}/kdeplasma-addons-%{version}.tar.bz2
# Source16-md5:	98f6e080bf0cee39856408de9e531205
Source17:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source17-md5:	2ff1c0b951ea42295343de0c4ebea965
Source18:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source18-md5:	c22b64fd89ebb0a0fc53245cf1dad91e
Source19:	%{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source19-md5:	c3eb6cf124355eb79c68ce403dd740ec
Source20:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source20-md5:	97ada60c70a73e511a89f83c2287de79
Source21:	%{_urlprefix}/oxygen-icons-%{version}.tar.bz2
# Source21-md5:	c46e7e51c5dde641f1e4c6bba0f2852f
%if %{with l10n}
Source22:	%{_urlprefix}/kde-l10n/kde-l10n-bg-%{version}.tar.bz2
# Source22-md5:	0743f1164a5f86aff2ce5882fac3f513
Source23:	%{_urlprefix}/kde-l10n/kde-l10n-ca-%{version}.tar.bz2
# Source23-md5:	b77aa5f347038ec6a0bf22d9ce35a884
Source24:	%{_urlprefix}/kde-l10n/kde-l10n-cs-%{version}.tar.bz2
# Source24-md5:	e23a88175c0fbf8bd7c9c728907ded5a
#Source25:	%{_urlprefix}/kde-l10n/kde-l10n-csb-%{version}.tar.bz2
## Source25-md5:	aaca61dfd1f6aa5ddf620dad9d2dc409
Source26:	%{_urlprefix}/kde-l10n/kde-l10n-da-%{version}.tar.bz2
# Source26-md5:	665c1952c767b882cb102133312d0f60
Source27:	%{_urlprefix}/kde-l10n/kde-l10n-de-%{version}.tar.bz2
# Source27-md5:	5d45b827275d9bd9588213c9092c9ae0
Source28:	%{_urlprefix}/kde-l10n/kde-l10n-el-%{version}.tar.bz2
# Source28-md5:	e66b4a7e4fc952bc93c820fee3e9fc5b
Source29:	%{_urlprefix}/kde-l10n/kde-l10n-en_GB-%{version}.tar.bz2
# Source29-md5:	0abb46c540f0392f99325d4d14bb1314
Source30:	%{_urlprefix}/kde-l10n/kde-l10n-es-%{version}.tar.bz2
# Source30-md5:	36751b8b89b720d914805633b38dd1d8
Source31:	%{_urlprefix}/kde-l10n/kde-l10n-et-%{version}.tar.bz2
# Source31-md5:	d2d24d1f88d1d93886fcfa508276d5d1
Source32:	%{_urlprefix}/kde-l10n/kde-l10n-fi-%{version}.tar.bz2
# Source32-md5:	5dcd941588632b07aaf566e0788a1884
Source33:	%{_urlprefix}/kde-l10n/kde-l10n-fr-%{version}.tar.bz2
# Source33-md5:	0fca80598686ba7e0aaeed3f2c1d8680
#Source34:	%{_urlprefix}/kde-l10n/kde-l10n-fy-%{version}.tar.bz2
# Source34-md5:	e5046259747f18c9d017f3606eda444c
Source35:	%{_urlprefix}/kde-l10n/kde-l10n-ga-%{version}.tar.bz2
# Source35-md5:	b569a769bd3f23c6008606175bae85d3
Source36:	%{_urlprefix}/kde-l10n/kde-l10n-gl-%{version}.tar.bz2
# Source36-md5:	136724fcb34e8f671085f2def9cbba89
Source37:	%{_urlprefix}/kde-l10n/kde-l10n-hi-%{version}.tar.bz2
# Source37-md5:	87ef3687e72b2773a9fe60c0602f2484
Source38:	%{_urlprefix}/kde-l10n/kde-l10n-hu-%{version}.tar.bz2
# Source38-md5:	f16403e270d06132472c8edf5f9a6a12
Source39:	%{_urlprefix}/kde-l10n/kde-l10n-it-%{version}.tar.bz2
# Source39-md5:	f5b2770a63cd179f0ebacf459a0fc87a
Source40:	%{_urlprefix}/kde-l10n/kde-l10n-ja-%{version}.tar.bz2
# Source40-md5:	fe555c88234be91171db2a02d351872f
Source41:	%{_urlprefix}/kde-l10n/kde-l10n-kk-%{version}.tar.bz2
# Source41-md5:	ee42ed12ec851f27f28fc96051aa9eea
Source42:	%{_urlprefix}/kde-l10n/kde-l10n-km-%{version}.tar.bz2
# Source42-md5:	4f09440092467b9c1fea14e4b26e92e1
Source43:	%{_urlprefix}/kde-l10n/kde-l10n-ko-%{version}.tar.bz2
# Source43-md5:	aee8f51f1e4ae356b133d1aa226fa32a
#Source44:	%{_urlprefix}/kde-l10n/kde-l10n-ku-%{version}.tar.bz2
## Source44-md5:	80dbde92c9cc2a3b18ddc8f8e6bf6228
Source45:	%{_urlprefix}/kde-l10n/kde-l10n-lt-%{version}.tar.bz2
# Source45-md5:	b1ef49c5cfe8a2133626c2064ab1f32b
Source46:	%{_urlprefix}/kde-l10n/kde-l10n-lv-%{version}.tar.bz2
# Source46-md5:	3f7fb135a725e47e69e666ad368f09fa
#Source47:	%{_urlprefix}/kde-l10n/kde-l10n-mk-%{version}.tar.bz2
## Source47-md5:	e391f33ac404ac3d0700137d1f8f9522
#Source48:	%{_urlprefix}/kde-l10n/kde-l10n-ml-%{version}.tar.bz2
## Source48-md5:	18953920117d90624f329f11b9f49fe3
Source49:	%{_urlprefix}/kde-l10n/kde-l10n-nb-%{version}.tar.bz2
# Source49-md5:	c666d6125f088ed53fe13d063258a5a1
Source50:	%{_urlprefix}/kde-l10n/kde-l10n-nds-%{version}.tar.bz2
# Source50-md5:	4e5cdc89446c9cf51522ad46b21d0ca7
Source51:	%{_urlprefix}/kde-l10n/kde-l10n-nl-%{version}.tar.bz2
# Source51-md5:	d3d1439168d8f68024cb7fcaa383f19e
Source52:	%{_urlprefix}/kde-l10n/kde-l10n-nn-%{version}.tar.bz2
# Source52-md5:	6ab2e60938c1dcafe8043af08ddd4a30
Source53:	%{_urlprefix}/kde-l10n/kde-l10n-pa-%{version}.tar.bz2
# Source53-md5:	9fdae265f15d0a1b901fe25f460a0221
Source54:	%{_urlprefix}/kde-l10n/kde-l10n-pl-%{version}.tar.bz2
# Source54-md5:	b648b9b77cfece552ac1116d17eef4fc
Source55:	%{_urlprefix}/kde-l10n/kde-l10n-pt-%{version}.tar.bz2
# Source55-md5:	eb666993b9b4f63c7987c9629ff99eb1
Source56:	%{_urlprefix}/kde-l10n/kde-l10n-pt_BR-%{version}.tar.bz2
# Source56-md5:	aeca4af4788f2e7e7521ee8043a80ed6
Source57:	%{_urlprefix}/kde-l10n/kde-l10n-ru-%{version}.tar.bz2
# Source57-md5:	a249e1645f3bcbe5c7bcd68c246bdf4f
Source58:	%{_urlprefix}/kde-l10n/kde-l10n-sl-%{version}.tar.bz2
# Source58-md5:	0fb8dca611325b79c73f74c47bcb8265
Source59:	%{_urlprefix}/kde-l10n/kde-l10n-sk-%{version}.tar.bz2
# Source59-md5:	7bad8e3d8a6c39621e6d8bcc174d8e53
Source60:	%{_urlprefix}/kde-l10n/kde-l10n-sr-%{version}.tar.bz2
# Source60-md5:	61f88e1877ff3cdc2ae7d375f1fe4bcd
Source61:	%{_urlprefix}/kde-l10n/kde-l10n-sv-%{version}.tar.bz2
# Source61-md5:	7a72bc8b320e8d10eb5376f99ce3272c
#Source62:	%{_urlprefix}/kde-l10n/kde-l10n-th-%{version}.tar.bz2
## Source62-md5:	2c5dd52012d3e21eaefde4211bee2d1c
Source63:	%{_urlprefix}/kde-l10n/kde-l10n-tr-%{version}.tar.bz2
# Source63-md5:	77c142098de145940c5bbbada82fc756
Source64:	%{_urlprefix}/kde-l10n/kde-l10n-uk-%{version}.tar.bz2
# Source64-md5:	ff8bddce2f4ad8b57ed281ab78add1c1
Source65:	%{_urlprefix}/kde-l10n/kde-l10n-wa-%{version}.tar.bz2
# Source65-md5:	a800b8e31be14010b690f70add36e02d
Source66:	%{_urlprefix}/kde-l10n/kde-l10n-zh_CN-%{version}.tar.bz2
# Source66-md5:	abc84444c120660f364c95698a67f529
Source67:	%{_urlprefix}/kde-l10n/kde-l10n-zh_TW-%{version}.tar.bz2
# Source67-md5:	43e19e6eb0bc0f6bdf345e52e5df87f5
%endif
%if %{with koffice}
Source68:	%{_urlprefix}/koffice-%{kofficever}/koffice-%{kofficever}.tar.bz2
# Source68-md5:	5ae8fa9d557f192bd6365f9450785228
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
