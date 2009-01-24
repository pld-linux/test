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
Version:	4.2.0
Release:	2
License:	GPL
Group:		Networking/Hacking
Source0:	%{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source0-md5:	f32f24c4f07906b7af39ca18d47b5e27
Source1:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source1-md5:	2c5b33477b5679bcd9fdbc1f8017e6fb
Source2:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source2-md5:	d81623b60c7deb314bc2e28a52254ac2
Source3:	%{_urlprefix}/kdebase-%{version}.tar.bz2
# Source3-md5:	da86a8ad624e86eda3a7509f39272060
Source4:	%{_urlprefix}/kdebase-runtime-%{version}.tar.bz2
# Source4-md5:	9e56281e9daa579d56cfda794f1bbc10
Source5:	%{_urlprefix}/kdebase-workspace-%{version}.tar.bz2
# Source5-md5:	193e30b9ed0b55b0196289d9df43a904
Source6:	%{_urlprefix}/kdebindings-%{version}.tar.bz2
# Source6-md5:	6eae8fd968da83fe65e592993e416adc
Source7:	%{_urlprefix}/kdeedu-%{version}.tar.bz2
# Source7-md5:	aaddbdab29e1d284ad8ee67a78b4c597
Source8:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source8-md5:	68cefd627025be99ba136e5a4e35e554
Source9:	%{_urlprefix}/kdegraphics-%{version}.tar.bz2
# Source9-md5:	8beb6fe5d475d0b0245ea6d4cc7e9732
Source10:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source10-md5:	4ea13b88463125026a7f71937075bcec
Source11:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source11-md5:	3e944c87888ac1ac5b11d3722dd31f88
Source12:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source12-md5:	0ea1628e11d398fdf45276a35edd3cae
Source13:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source13-md5:	a80631de21930b2544c86722138aaa6c
Source14:	%{_urlprefix}/kdepimlibs-%{version}.tar.bz2
# Source14-md5:	8a91677e2dca7d4db26b33c78e239e5e
Source15:	%{_urlprefix}/kdeplasma-addons-%{version}.tar.bz2
# Source15-md5:	d98f805f4c9b7af7278067f9e544b2ec
Source16:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source16-md5:	79d01b4f10f1ecc283f7860d2c7973e9
Source17:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source17-md5:	3adf538297e5dca51f15186b4acd02ce
Source18:	%{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source18-md5:	f0ca24c7d3e5bb0ab55bf6b26fc6224e
Source19:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source19-md5:	8b60c68f6cbbe9c5bb48caa576853f9e
%if %{with l10n}
Source20:	%{_urlprefix}/kde-l10n/kde-l10n-bg-%{version}.tar.bz2
# Source20-md5:	fc201d9b7d85b84ed02d049309d50ec7
Source21:	%{_urlprefix}/kde-l10n/kde-l10n-ca-%{version}.tar.bz2
# Source21-md5:	62b468adf048dde92abcea1cc8378ee0
Source22:	%{_urlprefix}/kde-l10n/kde-l10n-cs-%{version}.tar.bz2
# Source22-md5:	3fbbda2cb209e8c773c075ed3d28f831
Source23:	%{_urlprefix}/kde-l10n/kde-l10n-csb-%{version}.tar.bz2
# Source23-md5:	c9e576d85e7c8644a7f363a7dc446a47
Source24:	%{_urlprefix}/kde-l10n/kde-l10n-da-%{version}.tar.bz2
# Source24-md5:	9f6a01336b631223e13df6f82f6247ad
Source25:	%{_urlprefix}/kde-l10n/kde-l10n-de-%{version}.tar.bz2
# Source25-md5:	da8184a7380795790d498c7d5e4a6b62
Source26:	%{_urlprefix}/kde-l10n/kde-l10n-el-%{version}.tar.bz2
# Source26-md5:	2bbfca0b7a1366aee558804105b176cb
Source27:	%{_urlprefix}/kde-l10n/kde-l10n-en_GB-%{version}.tar.bz2
# Source27-md5:	12814406b6d35d8098a6cd16f49f827e
#Source28:	%{_urlprefix}/kde-l10n/kde-l10n-eo-%{version}.tar.bz2
# Source28-md5:	59f6247d771d39abc48ec803cc0a1cfa
Source29:	%{_urlprefix}/kde-l10n/kde-l10n-es-%{version}.tar.bz2
# Source29-md5:	e3b9bc8ef5573f7574e296385eb130a9
Source30:	%{_urlprefix}/kde-l10n/kde-l10n-et-%{version}.tar.bz2
# Source30-md5:	94b1a109b75d7bca66a3f26b0b3b61c1
Source31:	%{_urlprefix}/kde-l10n/kde-l10n-fi-%{version}.tar.bz2
# Source31-md5:	dc5bda4589b9a2042ade700caf8de083
Source32:	%{_urlprefix}/kde-l10n/kde-l10n-fr-%{version}.tar.bz2
# Source32-md5:	ca231f7972a5269a589cad934cd4ab81
#Source33:	%{_urlprefix}/kde-l10n/kde-l10n-fy-%{version}.tar.bz2
# Source33-md5:	e5046259747f18c9d017f3606eda444c
Source34:	%{_urlprefix}/kde-l10n/kde-l10n-ga-%{version}.tar.bz2
# Source34-md5:	d18b399ca99aa54c936bcdb207baac0a
Source35:	%{_urlprefix}/kde-l10n/kde-l10n-gl-%{version}.tar.bz2
# Source35-md5:	104815bc1b20b100509f66132df52cad
Source36:	%{_urlprefix}/kde-l10n/kde-l10n-hi-%{version}.tar.bz2
# Source36-md5:	b828a209e2b370e4b3487be01dc0ea8e
Source37:	%{_urlprefix}/kde-l10n/kde-l10n-hu-%{version}.tar.bz2
# Source37-md5:	b000573be5a3b6cee9ee9aa45b0931bc
Source38:	%{_urlprefix}/kde-l10n/kde-l10n-it-%{version}.tar.bz2
# Source38-md5:	42387c0b473767173ebf65622edb4278
Source39:	%{_urlprefix}/kde-l10n/kde-l10n-ja-%{version}.tar.bz2
# Source39-md5:	84c1dc6f18dd405b217d98312ffec6bf
Source40:	%{_urlprefix}/kde-l10n/kde-l10n-kk-%{version}.tar.bz2
# Source40-md5:	a984ed36132141eb8473ab541187d296
Source41:	%{_urlprefix}/kde-l10n/kde-l10n-km-%{version}.tar.bz2
# Source41-md5:	a8aaca814f556e3e8b3cd99f04eddca6
Source42:	%{_urlprefix}/kde-l10n/kde-l10n-ko-%{version}.tar.bz2
# Source42-md5:	bbd68e1c9eee724c7db051657fdfb50c
Source43:	%{_urlprefix}/kde-l10n/kde-l10n-ku-%{version}.tar.bz2
# Source43-md5:	3ce287f12f044c14608692518018bbef
Source44:	%{_urlprefix}/kde-l10n/kde-l10n-lt-%{version}.tar.bz2
# Source44-md5:	5ffad305fb06d70f7991745b82a427e3
Source45:	%{_urlprefix}/kde-l10n/kde-l10n-lv-%{version}.tar.bz2
# Source45-md5:	9d8fe83cefb273eb065337a0ab8790a5
Source46:	%{_urlprefix}/kde-l10n/kde-l10n-mk-%{version}.tar.bz2
# Source46-md5:	933d60b4c535d9d6d9729bd986906e64
Source47:	%{_urlprefix}/kde-l10n/kde-l10n-ml-%{version}.tar.bz2
# Source47-md5:	462763d9a71c273b7ae6f3ebd2c798e1
Source48:	%{_urlprefix}/kde-l10n/kde-l10n-nb-%{version}.tar.bz2
# Source48-md5:	db0d87c5125b05c25788cbf10fd56490
Source49:	%{_urlprefix}/kde-l10n/kde-l10n-nds-%{version}.tar.bz2
# Source49-md5:	378e068c4c86670788019ae7d0dda136
Source50:	%{_urlprefix}/kde-l10n/kde-l10n-nl-%{version}.tar.bz2
# Source50-md5:	f9174173973b0e235a3d729b0ef2f1cf
Source51:	%{_urlprefix}/kde-l10n/kde-l10n-nn-%{version}.tar.bz2
# Source51-md5:	cff7964f1c88a52d7e64df19e53c88ea
Source52:	%{_urlprefix}/kde-l10n/kde-l10n-pa-%{version}.tar.bz2
# Source52-md5:	a8dded180d298489861d17a761df51f8
Source53:	%{_urlprefix}/kde-l10n/kde-l10n-pl-%{version}.tar.bz2
# Source53-md5:	b04d741a53b0e1ba58d315cf118985e4
Source54:	%{_urlprefix}/kde-l10n/kde-l10n-pt-%{version}.tar.bz2
# Source54-md5:	eabe2a528d1e9d5c10ecae15dea68d26
Source55:	%{_urlprefix}/kde-l10n/kde-l10n-pt_BR-%{version}.tar.bz2
# Source55-md5:	d932254d7168016819aacc45a759592e
Source56:	%{_urlprefix}/kde-l10n/kde-l10n-ru-%{version}.tar.bz2
# Source56-md5:	9038ce82cdddf3fcf028aff50a55932a
Source57:	%{_urlprefix}/kde-l10n/kde-l10n-sl-%{version}.tar.bz2
# Source57-md5:	b24648e4fe6552ed7253acee7306f03e
Source58:	%{_urlprefix}/kde-l10n/kde-l10n-sr-%{version}.tar.bz2
# Source58-md5:	8d58ae783752ba8129df1e3866e8a089
Source59:	%{_urlprefix}/kde-l10n/kde-l10n-sv-%{version}.tar.bz2
# Source59-md5:	efbdb69f70e723c1ce0783e2a0693aaf
#Source60:	%{_urlprefix}/kde-l10n/kde-l10n-ta-%{version}.tar.bz2
# Source60-md5:	586ccb6fa1f2ef63aa1823c57201feb1
Source61:	%{_urlprefix}/kde-l10n/kde-l10n-th-%{version}.tar.bz2
# Source61-md5:	010ba3a0ed85c99cd215623f6d78fcd5
Source62:	%{_urlprefix}/kde-l10n/kde-l10n-tr-%{version}.tar.bz2
# Source62-md5:	850a88f8d82d9d9ab4c5ef2406eba39e
Source63:	%{_urlprefix}/kde-l10n/kde-l10n-uk-%{version}.tar.bz2
# Source63-md5:	7dba32b49fe5d263103a617a49a1849e
Source64:	%{_urlprefix}/kde-l10n/kde-l10n-wa-%{version}.tar.bz2
# Source64-md5:	0db1e8dc944786811cc1364df0ee4cf2
Source65:	%{_urlprefix}/kde-l10n/kde-l10n-zh_CN-%{version}.tar.bz2
# Source65-md5:	c4730babc7bef39cea255c9528607fdc
Source66:	%{_urlprefix}/kde-l10n/kde-l10n-zh_TW-%{version}.tar.bz2
# Source66-md5:	08af73c8b0f82689f5ab046f0700bf9d
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
