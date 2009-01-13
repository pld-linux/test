# - easy way to update all sources with new/old locales:
#   lynx -dump http://carme.pld-linux.org/~arekm/kde/kde-l10n | awk -vi=19 '/4.1.0.tar.bz2$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   sed -i -e 's,http://carme.pld-linux.org/~arekm/kde/kde-l10n/,%{_urlprefix}/kde-l10n/,' out
#   sed -i -e 's,4.1.0,%{version},' out
#   and then :r out in vim and ./builder -a5 the spec
%bcond_with	l10n
#%%define		_urlprefix	http://carme.pld-linux.org/~arekm/kde/
%define		_urlprefix	http://nomeno.pl/~shadzik/kde4/
#%%define		_urlprefix	ftp://ftp.pbone.net/mirror/ftp.kde.org/pub/kde/unstable/%{version}/src
Summary:	Fetch KDE packages to distfiles
Name:		kdefetch
Version:	4.1.96
Release:	0.3
License:	GPL
Group:		Networking/Hacking
Source0:	%{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source0-md5:	13d430b62f0b345b7e53b54e9236550d
Source1:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source1-md5:	6c7af1887587a5f864344550fa6c9af0
Source2:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source2-md5:	2c4f0cd7bf767551df395645248d5cb8
Source3:	%{_urlprefix}/kdebase-%{version}.tar.bz2
# Source3-md5:	d9010a13848e17d6f1cef3003a035b13
Source4:	%{_urlprefix}/kdebase-runtime-%{version}.tar.bz2
# Source4-md5:	2c34b66f9d1e7dfc1e0fa78087ddd773
Source5:	%{_urlprefix}/kdebase-workspace-%{version}.tar.bz2
# Source5-md5:	e4fd6e11f45e5099de521867797bf86b
Source6:	%{_urlprefix}/kdebindings-%{version}.tar.bz2
# Source6-md5:	7669193f0ce227bd7e113aaedc131225
Source7:	%{_urlprefix}/kdeedu-%{version}.tar.bz2
# Source7-md5:	b8c1cc06d06dff0852ca16daabeec51b
Source8:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source8-md5:	7d9be8e33e9626774cb6893259564620
Source9:	%{_urlprefix}/kdegraphics-%{version}.tar.bz2
# Source9-md5:	7c8d131404c8e464f553fa1515cebc40
Source10:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source10-md5:	b9254b5afda5bf1855b8d381b6d4509b
Source11:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source11-md5:	98d66627f6ae4376b6415ed1ad23ded4
Source12:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source12-md5:	01c69a5982758b4939627a6c4aa8fd55
Source13:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source13-md5:	4dceae1e430dfef40551f94495cb1f53
Source14:	%{_urlprefix}/kdepimlibs-%{version}.tar.bz2
# Source14-md5:	1ce1fd2ad92e765678c3f858c2a89fd0
Source15:	%{_urlprefix}/kdeplasma-addons-%{version}.tar.bz2
# Source15-md5:	323cc2d3da230e1916ad2fda0784da38
Source16:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source16-md5:	19ed9d019b0dd81dcb442bffb0561457
Source17:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source17-md5:	9a822c9986bc29eab0d92a0598b12dd5
Source18:	%{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source18-md5:	3e154bdb5d84501b372e2305150c4b47
Source19:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source19-md5:	3e10d388f932ce19351541bd2ae16fd6
%if %{with l10n}
Source20:	%{_urlprefix}/kde-l10n/kde-l10n-bg-%{version}.tar.bz2
# Source20-md5:	62095495040db4df27ba910e4baf1654
Source21:	%{_urlprefix}/kde-l10n/kde-l10n-ca-%{version}.tar.bz2
# Source21-md5:	23e9a8fc183373884bac7f723ee0fac2
Source22:	%{_urlprefix}/kde-l10n/kde-l10n-cs-%{version}.tar.bz2
# Source22-md5:	b12eb1339de5ee9a8a4306d4f78263de
Source23:	%{_urlprefix}/kde-l10n/kde-l10n-csb-%{version}.tar.bz2
# Source23-md5:	af896b1c81041b40a5b192f6f8843bd0
Source24:	%{_urlprefix}/kde-l10n/kde-l10n-da-%{version}.tar.bz2
# Source24-md5:	32dc82514e6583d97541cb43d6cb1e20
Source25:	%{_urlprefix}/kde-l10n/kde-l10n-de-%{version}.tar.bz2
# Source25-md5:	69928e97897eb9cea1f8304484075b77
Source26:	%{_urlprefix}/kde-l10n/kde-l10n-el-%{version}.tar.bz2
# Source26-md5:	7d3d8e145046aa433f418a81b6e7095d
Source27:	%{_urlprefix}/kde-l10n/kde-l10n-en_GB-%{version}.tar.bz2
# Source27-md5:	d29e0ebd2b94044db2572f55efc14c56
Source28:	%{_urlprefix}/kde-l10n/kde-l10n-eo-%{version}.tar.bz2
# Source28-md5:	59f6247d771d39abc48ec803cc0a1cfa
Source29:	%{_urlprefix}/kde-l10n/kde-l10n-es-%{version}.tar.bz2
# Source29-md5:	8c6e2507c6853809cac9aa66d3eb087f
Source30:	%{_urlprefix}/kde-l10n/kde-l10n-et-%{version}.tar.bz2
# Source30-md5:	8fc95ce4d7b80927062557479d6abc24
Source31:	%{_urlprefix}/kde-l10n/kde-l10n-fi-%{version}.tar.bz2
# Source31-md5:	e3ef31668dd60dbd39646d55c4a34614
Source32:	%{_urlprefix}/kde-l10n/kde-l10n-fr-%{version}.tar.bz2
# Source32-md5:	e48e82644ebbfe56becbd35ed21e7777
Source33:	%{_urlprefix}/kde-l10n/kde-l10n-fy-%{version}.tar.bz2
# Source33-md5:	e5046259747f18c9d017f3606eda444c
Source34:	%{_urlprefix}/kde-l10n/kde-l10n-ga-%{version}.tar.bz2
# Source34-md5:	f875d7f5f1d3efa984cd56eff0235784
Source35:	%{_urlprefix}/kde-l10n/kde-l10n-gl-%{version}.tar.bz2
# Source35-md5:	c122bebcd1bd5ed799e3856f3a4f0cdd
Source36:	%{_urlprefix}/kde-l10n/kde-l10n-hi-%{version}.tar.bz2
# Source36-md5:	4e143bc481106e01d38b396e5df44416
Source37:	%{_urlprefix}/kde-l10n/kde-l10n-hu-%{version}.tar.bz2
# Source37-md5:	b153b9ba4bcfd29f55fb648acbb9e759
Source38:	%{_urlprefix}/kde-l10n/kde-l10n-it-%{version}.tar.bz2
# Source38-md5:	a26a6e3ecdbbde48aecbcffba1399cf5
Source39:	%{_urlprefix}/kde-l10n/kde-l10n-ja-%{version}.tar.bz2
# Source39-md5:	386aecfdbf000a507a5c0430d8906c33
Source40:	%{_urlprefix}/kde-l10n/kde-l10n-kk-%{version}.tar.bz2
# Source40-md5:	c14fcfe7b1874160e8c526305a5f55d6
Source41:	%{_urlprefix}/kde-l10n/kde-l10n-km-%{version}.tar.bz2
# Source41-md5:	f8dc5ce78e5c2d1a44e60bce84279f38
Source42:	%{_urlprefix}/kde-l10n/kde-l10n-ko-%{version}.tar.bz2
# Source42-md5:	50d5d0c2fb064a8787f285eb7ba279b0
Source43:	%{_urlprefix}/kde-l10n/kde-l10n-ku-%{version}.tar.bz2
# Source43-md5:	2ede6e6fa858bf12266244f3cdfbed0c
Source44:	%{_urlprefix}/kde-l10n/kde-l10n-lt-%{version}.tar.bz2
# Source44-md5:	1b179c6f33c3ae5c18382f131d9608f9
Source45:	%{_urlprefix}/kde-l10n/kde-l10n-lv-%{version}.tar.bz2
# Source45-md5:	a206b118c13b57818a76b1a3b5714916
Source46:	%{_urlprefix}/kde-l10n/kde-l10n-mk-%{version}.tar.bz2
# Source46-md5:	79d31732e541070392c169c249780efd
Source47:	%{_urlprefix}/kde-l10n/kde-l10n-ml-%{version}.tar.bz2
# Source47-md5:	d14930ca1f29cc9a8d60f848d32b2e5b
Source48:	%{_urlprefix}/kde-l10n/kde-l10n-nb-%{version}.tar.bz2
# Source48-md5:	fb6d8dd2e74e9e0862fe2b693d522a57
Source49:	%{_urlprefix}/kde-l10n/kde-l10n-nds-%{version}.tar.bz2
# Source49-md5:	39d9ac7aa022b0df2cecd9eea76cdfe4
Source50:	%{_urlprefix}/kde-l10n/kde-l10n-nl-%{version}.tar.bz2
# Source50-md5:	40fa9ae5d2989291b2d1460b1598d6da
Source51:	%{_urlprefix}/kde-l10n/kde-l10n-nn-%{version}.tar.bz2
# Source51-md5:	f182724525952817b5f11152d9085c94
Source52:	%{_urlprefix}/kde-l10n/kde-l10n-pa-%{version}.tar.bz2
# Source52-md5:	bf879ef593a49729d8e743f2791d5df4
Source53:	%{_urlprefix}/kde-l10n/kde-l10n-pl-%{version}.tar.bz2
# Source53-md5:	3fd8eb6aa9fdef775ea435e64bd9d310
Source54:	%{_urlprefix}/kde-l10n/kde-l10n-pt-%{version}.tar.bz2
# Source54-md5:	81a45e66e12b5b3aaacae7c21498f834
Source55:	%{_urlprefix}/kde-l10n/kde-l10n-pt_BR-%{version}.tar.bz2
# Source55-md5:	bec1cf6f3d8870c16fe495c52a83587f
Source56:	%{_urlprefix}/kde-l10n/kde-l10n-ru-%{version}.tar.bz2
# Source56-md5:	b677e7bc523aa6fd75ed39dff1bcae9a
Source57:	%{_urlprefix}/kde-l10n/kde-l10n-sl-%{version}.tar.bz2
# Source57-md5:	bbfb5135bf89a52765294414b51ce772
Source58:	%{_urlprefix}/kde-l10n/kde-l10n-sr-%{version}.tar.bz2
# Source58-md5:	59aa3d00f5b26c2067a6f82e48f0fc78
Source59:	%{_urlprefix}/kde-l10n/kde-l10n-sv-%{version}.tar.bz2
# Source59-md5:	46d4d350e862184b2ac8dd5b0ad8d815
Source60:	%{_urlprefix}/kde-l10n/kde-l10n-ta-%{version}.tar.bz2
# Source60-md5:	586ccb6fa1f2ef63aa1823c57201feb1
Source61:	%{_urlprefix}/kde-l10n/kde-l10n-th-%{version}.tar.bz2
# Source61-md5:	fdf666417ed2c529cb0e3a4eb495b524
Source62:	%{_urlprefix}/kde-l10n/kde-l10n-tr-%{version}.tar.bz2
# Source62-md5:	0a5a3c13a01635e9060b238036f5a851
Source63:	%{_urlprefix}/kde-l10n/kde-l10n-uk-%{version}.tar.bz2
# Source63-md5:	d3f1d1090c98eba59367451ee8fec601
Source64:	%{_urlprefix}/kde-l10n/kde-l10n-wa-%{version}.tar.bz2
# Source64-md5:	ec57fe2c312e23c7226094ead62a24b8
Source65:	%{_urlprefix}/kde-l10n/kde-l10n-zh_CN-%{version}.tar.bz2
# Source65-md5:	33579ad111bd05d5eb4620c7eae22462
Source66:	%{_urlprefix}/kde-l10n/kde-l10n-zh_TW-%{version}.tar.bz2
# Source66-md5:	61a0356a4dc25f9d388bc6696ac787c8
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
