# - easy way to update all sources with new/old locales:
#   lynx -dump http://carme.pld-linux.org/~arekm/kde/kde-l10n | awk -vi=19 '/4.1.0.tar.bz2$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   sed -i -e 's,http://carme.pld-linux.org/~arekm/kde/kde-l10n/,%{_urlprefix}/kde-l10n/,' out
#   sed -i -e 's,4.1.0,%{version},' out
#   and then :r out in vim and ./builder -a5 the spec
%bcond_with	l10n
%bcond_with	koffice
#%%define		_urlprefix	http://carme.pld-linux.org/~arekm/kde/
%define		_urlprefix	http://shadzik.nomeno.pl/kde4/
%define		kofficever	2.3.1
#%%define		_urlprefix	ftp://ftp.pbone.net/mirror/ftp.kde.org/pub/kde/unstable/%{version}/src
Summary:	Fetch KDE packages to distfiles
Name:		kdefetch
Version:	4.5.5
Release:	3
License:	GPL
Group:		Networking/Hacking
Source100:	kde4diff.sh
Source0:	%{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source0-md5:	3be1c8f3291205e350006734600767e4
Source1:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source1-md5:	3737cfdc02e87ce236ea836dbb76c711
Source2:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source2-md5:	5a2dd4c94356ed3d92bed9f5bae6ae58
Source3:	%{_urlprefix}/kdebase-%{version}.tar.bz2
# Source3-md5:	f0eb111e0ce6570a6c3ccf2365543c37
Source4:	%{_urlprefix}/kdebase-runtime-%{version}.tar.bz2
# Source4-md5:	a26619cea3708fe0bef2bca5afee3733
Source5:	%{_urlprefix}/kdebase-workspace-%{version}.tar.bz2
# Source5-md5:	71aa7927acc526b2b7c1588d3697a75b
Source6:	%{_urlprefix}/kdebindings-%{version}.tar.bz2
# Source6-md5:	a1b3ed7fd4bf473e0e3e79c926bd6be2
Source7:	%{_urlprefix}/kdeedu-%{version}.tar.bz2
# Source7-md5:	42859a1c8568dfeeb164fdce01720a7e
Source8:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source8-md5:	bda063329f33c72fd8dc2a8412e8ff85
Source9:	%{_urlprefix}/kdegraphics-%{version}.tar.bz2
# Source9-md5:	62a773576beba66f522323d872c86129
Source10:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source10-md5:	a6037c53d34fe28f8a135181fe7c923b
#Source11:	%{_urlprefix}/kdepim-runtime-%{version}.tar.bz2
# Source11-md5:	63dff808a6a6d4b4467fddd3bfbfc0da
Source12:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source12-md5:	968947d44a1bfdbce9732008ee63ebca
Source13:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source13-md5:	9afe9295fd200323cb8171c2ad32e8fd
#Source14:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source14-md5:	aae69bbf54ffac3563f19a72b06f60b3
Source15:	%{_urlprefix}/kdepimlibs-%{version}.tar.bz2
# Source15-md5:	4ad7d01c3231e418cda80ec81d31846e
Source16:	%{_urlprefix}/kdeplasma-addons-%{version}.tar.bz2
# Source16-md5:	1ad0fbe68940a3f2c38c071cc5a58e95
Source17:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source17-md5:	bf9f9e6a14f5cf80b1d01d0d610d24e1
Source18:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source18-md5:	00f5fb6d5c01b55ad63c270a0db150ec
Source19:	%{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source19-md5:	81bdf5d3987ade47ca284458c842d60e
Source20:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source20-md5:	ab0a2fe13949bfe4df0f1eee0dbbc5f6
Source21:	%{_urlprefix}/oxygen-icons-%{version}.tar.bz2
# Source21-md5:	da56bf2e8f8c329fc86fbcd93bc09bfe
%if %{with l10n}
Source22:	%{_urlprefix}/kde-l10n/kde-l10n-bg-%{version}.tar.bz2
# Source22-md5:	289f4ad35af16e1295febbc81ee0d1cc
Source23:	%{_urlprefix}/kde-l10n/kde-l10n-ca-%{version}.tar.bz2
# Source23-md5:	f43ef56ace9333c4b4eed913b7adaae3
Source24:	%{_urlprefix}/kde-l10n/kde-l10n-cs-%{version}.tar.bz2
# Source24-md5:	26dc7d4009af594a66343dd4f107afb8
Source25:	%{_urlprefix}/kde-l10n/kde-l10n-csb-%{version}.tar.bz2
# Source25-md5:	aaca61dfd1f6aa5ddf620dad9d2dc409
Source26:	%{_urlprefix}/kde-l10n/kde-l10n-da-%{version}.tar.bz2
# Source26-md5:	18f3ea7134efe91761c2b0d4233a777f
Source27:	%{_urlprefix}/kde-l10n/kde-l10n-de-%{version}.tar.bz2
# Source27-md5:	58c73228397ca61e7e6b6b2b9e3a8eb7
Source28:	%{_urlprefix}/kde-l10n/kde-l10n-el-%{version}.tar.bz2
# Source28-md5:	2d524dfbfd92f6353357382747bbc8a7
Source29:	%{_urlprefix}/kde-l10n/kde-l10n-en_GB-%{version}.tar.bz2
# Source29-md5:	9571890944f6919cda6437de36b9d0e0
Source30:	%{_urlprefix}/kde-l10n/kde-l10n-es-%{version}.tar.bz2
# Source30-md5:	04e5c3bf2fc5db0d575f1160058f6b9e
Source31:	%{_urlprefix}/kde-l10n/kde-l10n-et-%{version}.tar.bz2
# Source31-md5:	be2804a5d37778accad44d7ff137116e
Source32:	%{_urlprefix}/kde-l10n/kde-l10n-fi-%{version}.tar.bz2
# Source32-md5:	008d74aa566a7d7ad24b899e05971156
Source33:	%{_urlprefix}/kde-l10n/kde-l10n-fr-%{version}.tar.bz2
# Source33-md5:	14a2b8dda0b92e61df5079562fc90631
#Source34:	%{_urlprefix}/kde-l10n/kde-l10n-fy-%{version}.tar.bz2
# Source34-md5:	e5046259747f18c9d017f3606eda444c
Source35:	%{_urlprefix}/kde-l10n/kde-l10n-ga-%{version}.tar.bz2
# Source35-md5:	313f09572ff3fc12d6e0948bbe9323a8
Source36:	%{_urlprefix}/kde-l10n/kde-l10n-gl-%{version}.tar.bz2
# Source36-md5:	b29696a293bf5d101fcc2c65ad766d6b
Source37:	%{_urlprefix}/kde-l10n/kde-l10n-hi-%{version}.tar.bz2
# Source37-md5:	ba6a612ffbf033dc39196fedeee12156
Source38:	%{_urlprefix}/kde-l10n/kde-l10n-hu-%{version}.tar.bz2
# Source38-md5:	cff446c8fec814d3c955b512afbd0bbb
Source39:	%{_urlprefix}/kde-l10n/kde-l10n-it-%{version}.tar.bz2
# Source39-md5:	25e59f06e9e81f9f04b0daa9b619445d
Source40:	%{_urlprefix}/kde-l10n/kde-l10n-ja-%{version}.tar.bz2
# Source40-md5:	4d43fda933fae49e3857ea3cae3a246e
Source41:	%{_urlprefix}/kde-l10n/kde-l10n-kk-%{version}.tar.bz2
# Source41-md5:	e27a39970fd7cbd8a7a77aa4646d78b9
Source42:	%{_urlprefix}/kde-l10n/kde-l10n-km-%{version}.tar.bz2
# Source42-md5:	98c9a0b0dea83b2166a555d251346334
Source43:	%{_urlprefix}/kde-l10n/kde-l10n-ko-%{version}.tar.bz2
# Source43-md5:	9193c57505c0a97c33e4f05a16dfac84
#Source44:	%{_urlprefix}/kde-l10n/kde-l10n-ku-%{version}.tar.bz2
## Source44-md5:	80dbde92c9cc2a3b18ddc8f8e6bf6228
Source45:	%{_urlprefix}/kde-l10n/kde-l10n-lt-%{version}.tar.bz2
# Source45-md5:	023d6c62be4b14af600efdc41d217615
Source46:	%{_urlprefix}/kde-l10n/kde-l10n-lv-%{version}.tar.bz2
# Source46-md5:	132d395b1a9298402d8c70f0b000a46c
Source47:	%{_urlprefix}/kde-l10n/kde-l10n-mk-%{version}.tar.bz2
# Source47-md5:	e391f33ac404ac3d0700137d1f8f9522
Source48:	%{_urlprefix}/kde-l10n/kde-l10n-ml-%{version}.tar.bz2
# Source48-md5:	18953920117d90624f329f11b9f49fe3
Source49:	%{_urlprefix}/kde-l10n/kde-l10n-nb-%{version}.tar.bz2
# Source49-md5:	fcf5593a127fbca1ad34c64619021812
Source50:	%{_urlprefix}/kde-l10n/kde-l10n-nds-%{version}.tar.bz2
# Source50-md5:	7fb584160fd7d23ab4e93fdad3b6f018
Source51:	%{_urlprefix}/kde-l10n/kde-l10n-nl-%{version}.tar.bz2
# Source51-md5:	5e7d69e1c34114e5f291d3ea43822b53
Source52:	%{_urlprefix}/kde-l10n/kde-l10n-nn-%{version}.tar.bz2
# Source52-md5:	f8e08119cd81e871e9cc2dc8293792d7
Source53:	%{_urlprefix}/kde-l10n/kde-l10n-pa-%{version}.tar.bz2
# Source53-md5:	8d74896f4eb98b05f16cc872f10701c7
Source54:	%{_urlprefix}/kde-l10n/kde-l10n-pl-%{version}.tar.bz2
# Source54-md5:	a2d5ebe8fd8e786e14b1cc623f9e846c
Source55:	%{_urlprefix}/kde-l10n/kde-l10n-pt-%{version}.tar.bz2
# Source55-md5:	ff72511e63e0908aef89ad4d27b58af0
Source56:	%{_urlprefix}/kde-l10n/kde-l10n-pt_BR-%{version}.tar.bz2
# Source56-md5:	8f53e213e5845d99d2a3ba9ad8ee0b45
Source57:	%{_urlprefix}/kde-l10n/kde-l10n-ru-%{version}.tar.bz2
# Source57-md5:	54b572b164977293aef7067dc65f49cc
Source58:	%{_urlprefix}/kde-l10n/kde-l10n-sl-%{version}.tar.bz2
# Source58-md5:	8b69e008e4c18c423c53785b489bd1b8
Source59:	%{_urlprefix}/kde-l10n/kde-l10n-sk-%{version}.tar.bz2
# Source59-md5:	a2d84b8a0d335c06d47d0e9554dd89dd
Source60:	%{_urlprefix}/kde-l10n/kde-l10n-sr-%{version}.tar.bz2
# Source60-md5:	4217d7c9eaf4e5e071529c276aa22926
Source61:	%{_urlprefix}/kde-l10n/kde-l10n-sv-%{version}.tar.bz2
# Source61-md5:	ca0112b6b66480a74cee73667db7a001
#Source62:	%{_urlprefix}/kde-l10n/kde-l10n-th-%{version}.tar.bz2
## Source62-md5:	2c5dd52012d3e21eaefde4211bee2d1c
Source63:	%{_urlprefix}/kde-l10n/kde-l10n-tr-%{version}.tar.bz2
# Source63-md5:	cb49ea48c6e1aac59a72ede159660890
Source64:	%{_urlprefix}/kde-l10n/kde-l10n-uk-%{version}.tar.bz2
# Source64-md5:	ef3d4ba05bbb795c0f9db6242a83ab3b
Source65:	%{_urlprefix}/kde-l10n/kde-l10n-wa-%{version}.tar.bz2
# Source65-md5:	d282c0f07ec398d528deff32070d811d
Source66:	%{_urlprefix}/kde-l10n/kde-l10n-zh_CN-%{version}.tar.bz2
# Source66-md5:	eecb1395482c1482b3244402f7d78638
Source67:	%{_urlprefix}/kde-l10n/kde-l10n-zh_TW-%{version}.tar.bz2
# Source67-md5:	ec1edd4964da8e6919b2966f81d35de3
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
