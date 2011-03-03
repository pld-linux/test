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
Version:	4.6.1
Release:	1
License:	GPL
Group:		Networking/Hacking
Source100:	kde4diff.sh
Source0:	%{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source0-md5:	60cb5a87c210721155019d0ef334f8f5
Source1:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source1-md5:	a3e5aae644fd6cd49de1378e37b5a0e6
Source2:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source2-md5:	b7a96990bff6d53b2519e49dfb8daf67
Source3:	%{_urlprefix}/kdebase-%{version}.tar.bz2
# Source3-md5:	d032fb52e5fdf2eb0b3ab37a7a06eacf
Source4:	%{_urlprefix}/kdebase-runtime-%{version}.tar.bz2
# Source4-md5:	26ad7899eb589a8bc260749fd22186a8
Source5:	%{_urlprefix}/kdebase-workspace-%{version}.tar.bz2
# Source5-md5:	b56385957880f08b664b055ae978d8db
Source6:	%{_urlprefix}/kdebindings-%{version}.tar.bz2
# Source6-md5:	bdb0180bdff41ad644155d2071c98c7a
Source7:	%{_urlprefix}/kdeedu-%{version}.tar.bz2
# Source7-md5:	48503c6bcc58c598ee48b684f662d8fe
Source8:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source8-md5:	079faf5198928e595acce2243daad39c
Source9:	%{_urlprefix}/kdegraphics-%{version}.tar.bz2
# Source9-md5:	9a0ca27211e309b57033c93c5c96268e
Source10:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source10-md5:	0cdc56a73009c65b5ad9ba3167ebb227
#Source11:	%{_urlprefix}/kdepim-runtime-%{version}.tar.bz2
# Source11-md5:	63dff808a6a6d4b4467fddd3bfbfc0da
Source12:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source12-md5:	6028c6e8ad41dfd32f8ae62314766f8f
Source13:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source13-md5:	f8aefe5e7b5d773745af442009026951
#Source14:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source14-md5:	aae69bbf54ffac3563f19a72b06f60b3
Source15:	%{_urlprefix}/kdepimlibs-%{version}.tar.bz2
# Source15-md5:	250d3d448c0e2a585b38e2c75c46d07f
Source16:	%{_urlprefix}/kdeplasma-addons-%{version}.tar.bz2
# Source16-md5:	c73ba7a4a3824f4334efd333bf61a3fd
Source17:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source17-md5:	2e199d9299a562b790676cb0455b9b6f
Source18:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source18-md5:	3b06a825425fd9388f64c3e916622d5a
Source19:	%{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source19-md5:	76b4d4fc3ff0d1d1b77742fede68589b
Source20:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source20-md5:	f4deca78e13c1bfba70f19ce56964b13
Source21:	%{_urlprefix}/oxygen-icons-%{version}.tar.bz2
# Source21-md5:	a856835ed19dffcd4d0eeae9d7c5a3a9
%if %{with l10n}
Source22:	%{_urlprefix}/kde-l10n/kde-l10n-bg-%{version}.tar.bz2
# Source22-md5:	5ace305d3d81a1a33cdb2de073e2030d
Source23:	%{_urlprefix}/kde-l10n/kde-l10n-ca-%{version}.tar.bz2
# Source23-md5:	4b8622573661c2f950155df654534961
Source24:	%{_urlprefix}/kde-l10n/kde-l10n-cs-%{version}.tar.bz2
# Source24-md5:	ae419d8574ca08ecf792036910f91557
#Source25:	%{_urlprefix}/kde-l10n/kde-l10n-csb-%{version}.tar.bz2
## Source25-md5:	aaca61dfd1f6aa5ddf620dad9d2dc409
Source26:	%{_urlprefix}/kde-l10n/kde-l10n-da-%{version}.tar.bz2
# Source26-md5:	a777268db485e47da4b7ad14db06aebb
Source27:	%{_urlprefix}/kde-l10n/kde-l10n-de-%{version}.tar.bz2
# Source27-md5:	8673677af34897e1a4bf18bcc88274be
Source28:	%{_urlprefix}/kde-l10n/kde-l10n-el-%{version}.tar.bz2
# Source28-md5:	b503900853ac69f1a8b4c11a31b64361
Source29:	%{_urlprefix}/kde-l10n/kde-l10n-en_GB-%{version}.tar.bz2
# Source29-md5:	ab61a106d80e5540872ef3600949e273
Source30:	%{_urlprefix}/kde-l10n/kde-l10n-es-%{version}.tar.bz2
# Source30-md5:	75395f769f88ccdd422756f5c5ffc436
Source31:	%{_urlprefix}/kde-l10n/kde-l10n-et-%{version}.tar.bz2
# Source31-md5:	2d1e7b7d5c9315df3eefb42d4a31601f
Source32:	%{_urlprefix}/kde-l10n/kde-l10n-fi-%{version}.tar.bz2
# Source32-md5:	239c39402e5fcfca4ef759c99faf42ba
Source33:	%{_urlprefix}/kde-l10n/kde-l10n-fr-%{version}.tar.bz2
# Source33-md5:	550b8b999d86e8ae0b9a86a51462af59
#Source34:	%{_urlprefix}/kde-l10n/kde-l10n-fy-%{version}.tar.bz2
# Source34-md5:	e5046259747f18c9d017f3606eda444c
Source35:	%{_urlprefix}/kde-l10n/kde-l10n-ga-%{version}.tar.bz2
# Source35-md5:	a5f57fbc9a63ff2f8749a82462521acb
Source36:	%{_urlprefix}/kde-l10n/kde-l10n-gl-%{version}.tar.bz2
# Source36-md5:	1a3f06e27849c607906431fbc33793b5
Source37:	%{_urlprefix}/kde-l10n/kde-l10n-hi-%{version}.tar.bz2
# Source37-md5:	215646ad9d40c2e34c2ddc40445e1ba0
Source38:	%{_urlprefix}/kde-l10n/kde-l10n-hu-%{version}.tar.bz2
# Source38-md5:	c15ce6d0173c21d21f8cf806194fa06e
Source39:	%{_urlprefix}/kde-l10n/kde-l10n-it-%{version}.tar.bz2
# Source39-md5:	e93a99f6c56f381dc24492515b6ad026
Source40:	%{_urlprefix}/kde-l10n/kde-l10n-ja-%{version}.tar.bz2
# Source40-md5:	e53e4a0e638c5dcfe6d540c0af87e0f1
Source41:	%{_urlprefix}/kde-l10n/kde-l10n-kk-%{version}.tar.bz2
# Source41-md5:	a86e35c7bee3938aaff781f488c15213
Source42:	%{_urlprefix}/kde-l10n/kde-l10n-km-%{version}.tar.bz2
# Source42-md5:	d218648998f4802624e739c104b208c5
Source43:	%{_urlprefix}/kde-l10n/kde-l10n-ko-%{version}.tar.bz2
# Source43-md5:	dbb8948f3baf39526225c66539e8a3ae
#Source44:	%{_urlprefix}/kde-l10n/kde-l10n-ku-%{version}.tar.bz2
## Source44-md5:	80dbde92c9cc2a3b18ddc8f8e6bf6228
Source45:	%{_urlprefix}/kde-l10n/kde-l10n-lt-%{version}.tar.bz2
# Source45-md5:	313dfd7881bcbd7d822ac163f67cc2a3
Source46:	%{_urlprefix}/kde-l10n/kde-l10n-lv-%{version}.tar.bz2
# Source46-md5:	4c70ad25c985485db15db4ce7f5a92d4
#Source47:	%{_urlprefix}/kde-l10n/kde-l10n-mk-%{version}.tar.bz2
## Source47-md5:	e391f33ac404ac3d0700137d1f8f9522
#Source48:	%{_urlprefix}/kde-l10n/kde-l10n-ml-%{version}.tar.bz2
## Source48-md5:	18953920117d90624f329f11b9f49fe3
Source49:	%{_urlprefix}/kde-l10n/kde-l10n-nb-%{version}.tar.bz2
# Source49-md5:	d0f882a5baed31585211531108b60d3a
Source50:	%{_urlprefix}/kde-l10n/kde-l10n-nds-%{version}.tar.bz2
# Source50-md5:	5f19668f488c4dd8f511f5ae7ca2bb3f
Source51:	%{_urlprefix}/kde-l10n/kde-l10n-nl-%{version}.tar.bz2
# Source51-md5:	6925f669acc443d2a4939aebcfedb48f
Source52:	%{_urlprefix}/kde-l10n/kde-l10n-nn-%{version}.tar.bz2
# Source52-md5:	6b7923a585488ece1966f7ee720bd699
Source53:	%{_urlprefix}/kde-l10n/kde-l10n-pa-%{version}.tar.bz2
# Source53-md5:	5a7870eabfa76421a83c8ea88b7b9cdd
Source54:	%{_urlprefix}/kde-l10n/kde-l10n-pl-%{version}.tar.bz2
# Source54-md5:	101ac29adc2dfa6d3093908f980358a2
Source55:	%{_urlprefix}/kde-l10n/kde-l10n-pt-%{version}.tar.bz2
# Source55-md5:	5d6fd0349c790ac73a486273ecc2b15d
Source56:	%{_urlprefix}/kde-l10n/kde-l10n-pt_BR-%{version}.tar.bz2
# Source56-md5:	283bfc4058fde09b5f40ef47dd7e93cb
Source57:	%{_urlprefix}/kde-l10n/kde-l10n-ru-%{version}.tar.bz2
# Source57-md5:	a306528247533e226612682d1b78aa6c
Source58:	%{_urlprefix}/kde-l10n/kde-l10n-sl-%{version}.tar.bz2
# Source58-md5:	60bdefeffff0b41445eddcc0f5ec4010
Source59:	%{_urlprefix}/kde-l10n/kde-l10n-sk-%{version}.tar.bz2
# Source59-md5:	110fc8e07bd3f981a49889459a4d8c33
Source60:	%{_urlprefix}/kde-l10n/kde-l10n-sr-%{version}.tar.bz2
# Source60-md5:	6b6c2c829cbc930431b76e179b78d123
Source61:	%{_urlprefix}/kde-l10n/kde-l10n-sv-%{version}.tar.bz2
# Source61-md5:	5d27d83ffa3aa8ed959960a2cb4e7cb5
#Source62:	%{_urlprefix}/kde-l10n/kde-l10n-th-%{version}.tar.bz2
## Source62-md5:	2c5dd52012d3e21eaefde4211bee2d1c
Source63:	%{_urlprefix}/kde-l10n/kde-l10n-tr-%{version}.tar.bz2
# Source63-md5:	60b85552abc123250ba53f9379f968e6
Source64:	%{_urlprefix}/kde-l10n/kde-l10n-uk-%{version}.tar.bz2
# Source64-md5:	4c164359f76720a23b048981a4ee46f7
Source65:	%{_urlprefix}/kde-l10n/kde-l10n-wa-%{version}.tar.bz2
# Source65-md5:	a6cf14141167a94d3e0be31a3ddd282f
Source66:	%{_urlprefix}/kde-l10n/kde-l10n-zh_CN-%{version}.tar.bz2
# Source66-md5:	d2c98100febc94a0dbe75782636f506e
Source67:	%{_urlprefix}/kde-l10n/kde-l10n-zh_TW-%{version}.tar.bz2
# Source67-md5:	6fae277af3874504e157890539565d0b
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
