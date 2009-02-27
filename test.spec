# - easy way to update all sources with new/old locales:
#   lynx -dump http://carme.pld-linux.org/~arekm/kde/kde-l10n | awk -vi=19 '/4.1.0.tar.bz2$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   sed -i -e 's,http://carme.pld-linux.org/~arekm/kde/kde-l10n/,%{_urlprefix}/kde-l10n/,' out
#   sed -i -e 's,4.1.0,%{version},' out
#   and then :r out in vim and ./builder -a5 the spec
%bcond_with	l10n
%bcond_with	koffice
#%%define		_urlprefix	http://carme.pld-linux.org/~arekm/kde/
%define		_urlprefix	http://nomeno.pl/~shadzik/kde4/
%define		kofficever	1.9.98.7
#%%define		_urlprefix	ftp://ftp.pbone.net/mirror/ftp.kde.org/pub/kde/unstable/%{version}/src
Summary:	Fetch KDE packages to distfiles
Name:		kdefetch
Version:	4.2.1
Release:	1
License:	GPL
Group:		Networking/Hacking
Source100:	kde4diff.sh
Source0:	%{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source0-md5:	4005e2acc05a2479d83386588b91668f
Source1:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source1-md5:	11dde15ee5150357801c245d1290f38d
Source2:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source2-md5:	2712142e1cd452f6ada441a310a971d6
Source3:	%{_urlprefix}/kdebase-%{version}.tar.bz2
# Source3-md5:	a8f391db7b98feaa6ae81b8f1e99ed5a
Source4:	%{_urlprefix}/kdebase-runtime-%{version}.tar.bz2
# Source4-md5:	93ef480ed5376ce02324d1b85b8bae0f
Source5:	%{_urlprefix}/kdebase-workspace-%{version}.tar.bz2
# Source5-md5:	0401441f4e26c47c9381048ef0398e5b
Source6:	%{_urlprefix}/kdebindings-%{version}.tar.bz2
# Source6-md5:	8b81bc56e77404fd377af56224bd966f
Source7:	%{_urlprefix}/kdeedu-%{version}.tar.bz2
# Source7-md5:	bc8fb562cf0564ce50486b83f7c94d01
Source8:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source8-md5:	c640899282024033124de5655a520d21
Source9:	%{_urlprefix}/kdegraphics-%{version}.tar.bz2
# Source9-md5:	9cc2bc859e678aa6178a5c6cf87eb0ab
Source10:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source10-md5:	3ccc094df33db9d61f5ad065b9b857ac
Source11:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source11-md5:	d3916cb7a0dd5cb4e230e5c19d99563b
Source12:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source12-md5:	17ba9800af0bfcf20a49337624f9946a
Source13:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source13-md5:	2ebc3730aaee53f494e8e6abd26029bd
Source14:	%{_urlprefix}/kdepimlibs-%{version}.tar.bz2
# Source14-md5:	5f220939f33c38992f419d5dfc6874df
Source15:	%{_urlprefix}/kdeplasma-addons-%{version}.tar.bz2
# Source15-md5:	55219414d52924cb22ea2953cd2ae78b
Source16:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source16-md5:	e1c95a5ab0e34d2d084677199af0b093
Source17:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source17-md5:	78cd751eb92ec2f068c8dc39794175e6
Source18:	%{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source18-md5:	ed3397244a64530c108e76d6767c07d0
Source19:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source19-md5:	38e6f1343cf1024e52059146609a6a85
%if %{with l10n}
Source20:	%{_urlprefix}/kde-l10n/kde-l10n-bg-%{version}.tar.bz2
# Source20-md5:	f6621960e9a1f3328e42a6f5735083c7
Source21:	%{_urlprefix}/kde-l10n/kde-l10n-ca-%{version}.tar.bz2
# Source21-md5:	b4e42ac60e2491025705ef7d4f9ff613
Source22:	%{_urlprefix}/kde-l10n/kde-l10n-cs-%{version}.tar.bz2
# Source22-md5:	7787304141fa31c4b967297b2d75b36f
Source23:	%{_urlprefix}/kde-l10n/kde-l10n-csb-%{version}.tar.bz2
# Source23-md5:	2f2ca099814cd3bbf1a0273d0b027b80
Source24:	%{_urlprefix}/kde-l10n/kde-l10n-da-%{version}.tar.bz2
# Source24-md5:	7765ade376b10d25d88e0b9d7ea7ef94
Source25:	%{_urlprefix}/kde-l10n/kde-l10n-de-%{version}.tar.bz2
# Source25-md5:	c1521b6517667e9dd1a29ffb9182cd0e
Source26:	%{_urlprefix}/kde-l10n/kde-l10n-el-%{version}.tar.bz2
# Source26-md5:	53df4a6bd3f6ce8aa4130ab4c927ec93
Source27:	%{_urlprefix}/kde-l10n/kde-l10n-en_GB-%{version}.tar.bz2
# Source27-md5:	bb92656ccfd7c4e1c28b8e1ae53d01b5
#Source28:	%{_urlprefix}/kde-l10n/kde-l10n-eo-%{version}.tar.bz2
# Source28-md5:	59f6247d771d39abc48ec803cc0a1cfa
Source29:	%{_urlprefix}/kde-l10n/kde-l10n-es-%{version}.tar.bz2
# Source29-md5:	249501d5acaf9cdaa1c81ecc7892ee9f
Source30:	%{_urlprefix}/kde-l10n/kde-l10n-et-%{version}.tar.bz2
# Source30-md5:	4d7ba6e07f6949bf03d810e67d55230c
Source31:	%{_urlprefix}/kde-l10n/kde-l10n-fi-%{version}.tar.bz2
# Source31-md5:	4b69917aee664dd2b10471d8a9294dd2
Source32:	%{_urlprefix}/kde-l10n/kde-l10n-fr-%{version}.tar.bz2
# Source32-md5:	d9b613ccb77cce12385ba77bfc0eb5ec
#Source33:	%{_urlprefix}/kde-l10n/kde-l10n-fy-%{version}.tar.bz2
# Source33-md5:	e5046259747f18c9d017f3606eda444c
Source34:	%{_urlprefix}/kde-l10n/kde-l10n-ga-%{version}.tar.bz2
# Source34-md5:	e5b10ab623c56b45cf206db37024049a
Source35:	%{_urlprefix}/kde-l10n/kde-l10n-gl-%{version}.tar.bz2
# Source35-md5:	fafa0c2a2f6b46d0c9f4c11508ac86e6
Source36:	%{_urlprefix}/kde-l10n/kde-l10n-hi-%{version}.tar.bz2
# Source36-md5:	8b4a197ff42a3ec17624a612db748205
Source37:	%{_urlprefix}/kde-l10n/kde-l10n-hu-%{version}.tar.bz2
# Source37-md5:	fe62f86cea5b6022b40650299ed5223c
Source38:	%{_urlprefix}/kde-l10n/kde-l10n-it-%{version}.tar.bz2
# Source38-md5:	5f366b474472536371baf9890458f1a0
Source39:	%{_urlprefix}/kde-l10n/kde-l10n-ja-%{version}.tar.bz2
# Source39-md5:	f43e96ea7eba05616b25145cf3e26e9a
Source40:	%{_urlprefix}/kde-l10n/kde-l10n-kk-%{version}.tar.bz2
# Source40-md5:	e32ff330ab1caa8cc45e6474bda42fc9
Source41:	%{_urlprefix}/kde-l10n/kde-l10n-km-%{version}.tar.bz2
# Source41-md5:	3db01f4d93ef17a03173e2c0b4693889
Source42:	%{_urlprefix}/kde-l10n/kde-l10n-ko-%{version}.tar.bz2
# Source42-md5:	a05b21792fb0a2dc032454852a1d75e6
Source43:	%{_urlprefix}/kde-l10n/kde-l10n-ku-%{version}.tar.bz2
# Source43-md5:	d065d40014e1a4a8d120b4c60ac4e298
Source44:	%{_urlprefix}/kde-l10n/kde-l10n-lt-%{version}.tar.bz2
# Source44-md5:	e10ac0d7d88183849a1a811dd1dc4191
Source45:	%{_urlprefix}/kde-l10n/kde-l10n-lv-%{version}.tar.bz2
# Source45-md5:	2591ad3682547ad5c5ddce2d99644325
Source46:	%{_urlprefix}/kde-l10n/kde-l10n-mk-%{version}.tar.bz2
# Source46-md5:	c02330d7c1de2386dca89f9c5f4e124e
Source47:	%{_urlprefix}/kde-l10n/kde-l10n-ml-%{version}.tar.bz2
# Source47-md5:	27d628c4230b378bdbe5ac74b1fd7611
Source48:	%{_urlprefix}/kde-l10n/kde-l10n-nb-%{version}.tar.bz2
# Source48-md5:	e4b6d5a8f7a6acb46c6493986deb2fc0
Source49:	%{_urlprefix}/kde-l10n/kde-l10n-nds-%{version}.tar.bz2
# Source49-md5:	6b3cd678e8d2bfdb3b3b28d1dbc17c9a
Source50:	%{_urlprefix}/kde-l10n/kde-l10n-nl-%{version}.tar.bz2
# Source50-md5:	c5612a215db0b13b0cfd5b17e337300e
Source51:	%{_urlprefix}/kde-l10n/kde-l10n-nn-%{version}.tar.bz2
# Source51-md5:	80a3b5932356f21a8b9068ca40f7e0c1
Source52:	%{_urlprefix}/kde-l10n/kde-l10n-pa-%{version}.tar.bz2
# Source52-md5:	385983a3584a639c91f0c489140e9d28
Source53:	%{_urlprefix}/kde-l10n/kde-l10n-pl-%{version}.tar.bz2
# Source53-md5:	6cc2883667a293f7db927fd076623f93
Source54:	%{_urlprefix}/kde-l10n/kde-l10n-pt-%{version}.tar.bz2
# Source54-md5:	55e15795d4901701b7deab813857ec06
Source55:	%{_urlprefix}/kde-l10n/kde-l10n-pt_BR-%{version}.tar.bz2
# Source55-md5:	a77c500292a1615f77a519d84d6f5a7c
Source56:	%{_urlprefix}/kde-l10n/kde-l10n-ru-%{version}.tar.bz2
# Source56-md5:	770d39e08471b0fe91762dbee93d6d00
Source57:	%{_urlprefix}/kde-l10n/kde-l10n-sl-%{version}.tar.bz2
# Source57-md5:	d643261b6b97a587a9d3fc682f4b01b0
Source58:	%{_urlprefix}/kde-l10n/kde-l10n-sr-%{version}.tar.bz2
# Source58-md5:	6ec221411c0e338bb25234c95abd3045
Source59:	%{_urlprefix}/kde-l10n/kde-l10n-sv-%{version}.tar.bz2
# Source59-md5:	4f2a5b6ee87c129499350418d1a0a17e
#Source60:	%{_urlprefix}/kde-l10n/kde-l10n-ta-%{version}.tar.bz2
# Source60-md5:	586ccb6fa1f2ef63aa1823c57201feb1
Source61:	%{_urlprefix}/kde-l10n/kde-l10n-th-%{version}.tar.bz2
# Source61-md5:	62c1114df471bc35e05e2980e2c12b47
Source62:	%{_urlprefix}/kde-l10n/kde-l10n-tr-%{version}.tar.bz2
# Source62-md5:	8ce5790512f818320804967a6e5c6204
Source63:	%{_urlprefix}/kde-l10n/kde-l10n-uk-%{version}.tar.bz2
# Source63-md5:	40f6a3fd553144ccd8a576fed272fb6d
Source64:	%{_urlprefix}/kde-l10n/kde-l10n-wa-%{version}.tar.bz2
# Source64-md5:	9334b0cd1a718afb59b81906a677ac44
Source65:	%{_urlprefix}/kde-l10n/kde-l10n-zh_CN-%{version}.tar.bz2
# Source65-md5:	f3cbd496581e3acdaf5bb371549103ee
Source66:	%{_urlprefix}/kde-l10n/kde-l10n-zh_TW-%{version}.tar.bz2
# Source66-md5:	4b78c747661c0f1f7840f180b06e48a8
%endif
%if %{with koffice}
Source67:	%{_urlprefix}/koffice-%{kofficever}/koffice-%{kofficever}.tar.bz2
# Source67-md5:	1b44eb284f35d148ea6aacb0f2408277
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
