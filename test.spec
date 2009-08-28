# - easy way to update all sources with new/old locales:
#   lynx -dump http://carme.pld-linux.org/~arekm/kde/kde-l10n | awk -vi=19 '/4.1.0.tar.bz2$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   sed -i -e 's,http://carme.pld-linux.org/~arekm/kde/kde-l10n/,%{_urlprefix}/kde-l10n/,' out
#   sed -i -e 's,4.1.0,%{version},' out
#   and then :r out in vim and ./builder -a5 the spec
%bcond_with	l10n
%bcond_with	koffice
#%%define		_urlprefix	http://carme.pld-linux.org/~arekm/kde/
%define		_urlprefix	http://shadzik.nomeno.pl/kde4/
%define		kofficever	1.9.99.0
#%%define		_urlprefix	ftp://ftp.pbone.net/mirror/ftp.kde.org/pub/kde/unstable/%{version}/src
Summary:	Fetch KDE packages to distfiles
Name:		kdefetch
Version:	4.3.1
Release:	1
License:	GPL
Group:		Networking/Hacking
Source100:	kde4diff.sh
Source0:	%{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source0-md5:	82f2175329c87b84a25be586b69d6b25
Source1:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source1-md5:	e946d243d0e6e1fdbb24c732acca9c1e
Source2:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source2-md5:	9dbb00b76968658a7337e839fa342230
Source3:	%{_urlprefix}/kdebase-%{version}.tar.bz2
# Source3-md5:	10dae53739f1e8bd6f5f615443649e4f
Source4:	%{_urlprefix}/kdebase-runtime-%{version}.tar.bz2
# Source4-md5:	e51384cef307280f41fa8f39e2ecab8a
Source5:	%{_urlprefix}/kdebase-workspace-%{version}.tar.bz2
# Source5-md5:	48e3674ddd75e63a9a2f405160d02d06
Source6:	%{_urlprefix}/kdebindings-%{version}.tar.bz2
# Source6-md5:	6cc71c3f6136d3b69f7a109d03ddfe40
Source7:	%{_urlprefix}/kdeedu-%{version}.tar.bz2
# Source7-md5:	f283c3727e3507e548e43b84a28def7d
Source8:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source8-md5:	dd0819543978033d4701d65109bf3926
Source9:	%{_urlprefix}/kdegraphics-%{version}.tar.bz2
# Source9-md5:	1657ac3a8773db36b2d89e0bdb332d8b
Source10:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source10-md5:	df6b6d261d46508c7b0abcdd983ffae2
Source11:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source11-md5:	e9a74626bc7eec8496ff9157e65025da
Source12:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source12-md5:	496000ae85856da0c6fb0e014d03d0d7
Source13:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source13-md5:	1029bc586f29c262f5f60eb079623e62
Source14:	%{_urlprefix}/kdepimlibs-%{version}.tar.bz2
# Source14-md5:	8f8ffad4475a98f864470da888ef0931
Source15:	%{_urlprefix}/kdeplasma-addons-%{version}.tar.bz2
# Source15-md5:	282473836da35a48a6c6bee0b6fa6666
Source16:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source16-md5:	e1fda958d1f0a2ac39c0cc04814d1fd7
Source17:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source17-md5:	0cd0bba2f6265751537bf7bdaeacb518
Source18:	%{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source18-md5:	69491ba185ba8ecb2dd4860d7048a88a
Source19:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source19-md5:	22b8e5055f93ef07dc8233f003109d3f
#Source20:	%{_urlprefix}/oxygen-icons-%{version}.tar.bz2
# Source20-md5:	584cff3a47ac7eda4bec61ae5f6417aa
%if %{with l10n}
Source21:	%{_urlprefix}/kde-l10n/kde-l10n-bg-%{version}.tar.bz2
# Source21-md5:	04352d8c1e6820505adf230ef582326a
Source22:	%{_urlprefix}/kde-l10n/kde-l10n-ca-%{version}.tar.bz2
# Source22-md5:	6d90c8a58ef21cc84fbde5034abcdfd2
Source23:	%{_urlprefix}/kde-l10n/kde-l10n-cs-%{version}.tar.bz2
# Source23-md5:	c528e407bc177d8cc8f07900942ed98a
Source24:	%{_urlprefix}/kde-l10n/kde-l10n-csb-%{version}.tar.bz2
# Source24-md5:	b63dfbfa73b7fd0cb6b86652ec0a115d
Source25:	%{_urlprefix}/kde-l10n/kde-l10n-da-%{version}.tar.bz2
# Source25-md5:	39cdd4d26781d2af6528316f924dd2f9
Source26:	%{_urlprefix}/kde-l10n/kde-l10n-de-%{version}.tar.bz2
# Source26-md5:	2f1185db36349a14a600ec58656c82ec
Source27:	%{_urlprefix}/kde-l10n/kde-l10n-el-%{version}.tar.bz2
# Source27-md5:	8cec4b527e64f11698217029413730ab
Source28:	%{_urlprefix}/kde-l10n/kde-l10n-en_GB-%{version}.tar.bz2
# Source28-md5:	7598465393f948243f9da0252620ba93
Source29:	%{_urlprefix}/kde-l10n/kde-l10n-es-%{version}.tar.bz2
# Source29-md5:	dbe304dbadf6d03dfb73bc8577c603d6
Source30:	%{_urlprefix}/kde-l10n/kde-l10n-et-%{version}.tar.bz2
# Source30-md5:	313999a61733d722324b4e899d8fecdd
Source31:	%{_urlprefix}/kde-l10n/kde-l10n-fi-%{version}.tar.bz2
# Source31-md5:	7d9d0e64d741c7c74917161336ccd982
Source32:	%{_urlprefix}/kde-l10n/kde-l10n-fr-%{version}.tar.bz2
# Source32-md5:	0da9b56a0bc2a0cbb113974a365f0350
#Source33:	%{_urlprefix}/kde-l10n/kde-l10n-fy-%{version}.tar.bz2
# Source33-md5:	e5046259747f18c9d017f3606eda444c
Source34:	%{_urlprefix}/kde-l10n/kde-l10n-ga-%{version}.tar.bz2
# Source34-md5:	4c5f9d3c1f5c4514af509b9989186548
Source35:	%{_urlprefix}/kde-l10n/kde-l10n-gl-%{version}.tar.bz2
# Source35-md5:	e1e3031948ff689b83f7e7f192ccda3c
Source36:	%{_urlprefix}/kde-l10n/kde-l10n-hi-%{version}.tar.bz2
# Source36-md5:	65854d31de0eadd32680a2c03c0644f9
Source37:	%{_urlprefix}/kde-l10n/kde-l10n-hu-%{version}.tar.bz2
# Source37-md5:	9c0e191bc9d1d6e53d400611f3b7817c
Source38:	%{_urlprefix}/kde-l10n/kde-l10n-it-%{version}.tar.bz2
# Source38-md5:	b32ebadc4ec0c02202db7a6b7431b78d
Source39:	%{_urlprefix}/kde-l10n/kde-l10n-ja-%{version}.tar.bz2
# Source39-md5:	756f92c06b8cb013e4fc0ee6a8388465
Source40:	%{_urlprefix}/kde-l10n/kde-l10n-kk-%{version}.tar.bz2
# Source40-md5:	3d8f1c7f64a950b2370bfc695a8dca3d
Source41:	%{_urlprefix}/kde-l10n/kde-l10n-km-%{version}.tar.bz2
# Source41-md5:	81559bf93f7fc0e7a776dc5021393846
Source42:	%{_urlprefix}/kde-l10n/kde-l10n-ko-%{version}.tar.bz2
# Source42-md5:	0604120363f244fb9f6a9f52b28e9cd3
Source43:	%{_urlprefix}/kde-l10n/kde-l10n-ku-%{version}.tar.bz2
# Source43-md5:	3861b5ed7bc1281f8e7dc7b3898b3cfb
Source44:	%{_urlprefix}/kde-l10n/kde-l10n-lt-%{version}.tar.bz2
# Source44-md5:	18a4848bb2e191995219bcb43d05692d
Source45:	%{_urlprefix}/kde-l10n/kde-l10n-lv-%{version}.tar.bz2
# Source45-md5:	2d387abb28a3309d09060c18217b6eac
Source46:	%{_urlprefix}/kde-l10n/kde-l10n-mk-%{version}.tar.bz2
# Source46-md5:	feebd0b5db522c87d9206583db7c737d
Source47:	%{_urlprefix}/kde-l10n/kde-l10n-ml-%{version}.tar.bz2
# Source47-md5:	e9d4bc43113e74040e59a7fbc4e751a9
Source48:	%{_urlprefix}/kde-l10n/kde-l10n-nb-%{version}.tar.bz2
# Source48-md5:	d01bca94aa6eef4add56af21b8a7c1d9
Source49:	%{_urlprefix}/kde-l10n/kde-l10n-nds-%{version}.tar.bz2
# Source49-md5:	ded46915af415c47b8c449ab36261298
Source50:	%{_urlprefix}/kde-l10n/kde-l10n-nl-%{version}.tar.bz2
# Source50-md5:	77aef34bf6e2993e95fa043a6e4d884d
Source51:	%{_urlprefix}/kde-l10n/kde-l10n-nn-%{version}.tar.bz2
# Source51-md5:	8efa6f0754c7c03751bdb64a00702955
Source52:	%{_urlprefix}/kde-l10n/kde-l10n-pa-%{version}.tar.bz2
# Source52-md5:	d2eac659c14a3feeba3021f4268ac7ca
Source53:	%{_urlprefix}/kde-l10n/kde-l10n-pl-%{version}.tar.bz2
# Source53-md5:	6749341a81d7807e326ce954b197b3e5
Source54:	%{_urlprefix}/kde-l10n/kde-l10n-pt-%{version}.tar.bz2
# Source54-md5:	c364a53f7409ebc1f9fde2e9eeecd8b5
Source55:	%{_urlprefix}/kde-l10n/kde-l10n-pt_BR-%{version}.tar.bz2
# Source55-md5:	a1b1f1dc212ca772977488cc89ef9932
Source56:	%{_urlprefix}/kde-l10n/kde-l10n-ru-%{version}.tar.bz2
# Source56-md5:	d18ed35c1ff28ba2ee493fde9750210d
Source57:	%{_urlprefix}/kde-l10n/kde-l10n-sl-%{version}.tar.bz2
# Source57-md5:	89042687ac864b2edbfc88de0250940f
Source58:	%{_urlprefix}/kde-l10n/kde-l10n-sk-%{version}.tar.bz2
# Source58-md5:	59fbfc7bf835dfbd04458e5ddc5629a1
Source59:	%{_urlprefix}/kde-l10n/kde-l10n-sr-%{version}.tar.bz2
# Source59-md5:	9d50b526065a2d98e9614260673f99c2
Source60:	%{_urlprefix}/kde-l10n/kde-l10n-sv-%{version}.tar.bz2
# Source60-md5:	b70552996f20bf629531420fbf9bf9d1
Source61:	%{_urlprefix}/kde-l10n/kde-l10n-th-%{version}.tar.bz2
# Source61-md5:	5164f4a21632fa1a065a9cc68409e1b1
Source62:	%{_urlprefix}/kde-l10n/kde-l10n-tr-%{version}.tar.bz2
# Source62-md5:	73996436690460bb7cbd77862bcb7350
Source63:	%{_urlprefix}/kde-l10n/kde-l10n-uk-%{version}.tar.bz2
# Source63-md5:	f69f121a0abc6129ec8e2f5bca171623
Source64:	%{_urlprefix}/kde-l10n/kde-l10n-wa-%{version}.tar.bz2
# Source64-md5:	402f19e737e56855bb3dfbbb240b891c
Source65:	%{_urlprefix}/kde-l10n/kde-l10n-zh_CN-%{version}.tar.bz2
# Source65-md5:	373ef1ab6e56d063982c0e53b575ad3e
Source66:	%{_urlprefix}/kde-l10n/kde-l10n-zh_TW-%{version}.tar.bz2
# Source66-md5:	b1e8f50ea643b4ed8115d5c3257792cd
%endif
%if %{with koffice}
Source67:	%{_urlprefix}/koffice-%{kofficever}/koffice-%{kofficever}.tar.bz2
# Source67-md5:	46dcbdda79c6a9aa645d1d473c8d2046
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
