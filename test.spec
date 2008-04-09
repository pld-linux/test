# - easy way to update all sources with new/old locales:
#   lynx -dump http://carme.pld-linux.org/~arekm/kde/kde-i18n | awk -vi=19 '/3.5.9.tar.bz2$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   sed -i -e 's,http://carme.pld-linux.org/~arekm/kde/kde-i18n/,%{_urlprefix}/kde-i18n/,' out
#   sed -i -e 's,3.5.9,%{version},' out
#   and then :r out in vim and ./builder -a5 the spec
%bcond_with	i18n
%define		_urlprefix	http://carme.pld-linux.org/~arekm/kde/
%define		artsver	1.5.9
%define		kdevelopver 3.5.1
Summary:	Fetch KDE packages to distfiles
Name:		kdefetch
Version:	3.5.9
Release:	2
License:	GPL
Group:		Networking/Hacking
Source0:	%{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source0-md5:	79c7fa53ec60ad51fbdb16aac56d85a1
Source1:	%{_urlprefix}/kdeaddons-%{version}.tar.bz2
# Source1-md5:	eaa3832a25b483d1a9613f75991c3d7b
Source2:	%{_urlprefix}/arts-%{artsver}.tar.bz2
# Source2-md5:	62a5e4d522314bab19288e4702480c93
Source3:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source3-md5:	e6607ea27b332616d20f4564656cb885
Source4:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source4-md5:	ec526eba38421fd3b143682b8d683c86
Source5:	%{_urlprefix}/kdebase-%{version}.tar.bz2
# Source5-md5:	c8c35389a238aa1b73e68ef5298eadf8
Source6:	%{_urlprefix}/kdebindings-%{version}.tar.bz2
# Source6-md5:	ba780920f6b810a30a61b1ffa888706b
Source7:	%{_urlprefix}/kdeedu-%{version}.tar.bz2
# Source7-md5:	cbdabe916ce6fa300f8dab972c5cb4a4
Source8:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source8-md5:	472385f21a692270fb5643d7617c7ff3
Source9:	%{_urlprefix}/kdegraphics-%{version}.tar.bz2
# Source9-md5:	3d75e27180573a4e077e0245055891a5
Source10:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source10-md5:	55e5f00874933d1a7ba7c95e369a205e
Source11:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source11-md5:	fdfafe38d2c7e3019dafc80c177add15
Source12:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source12-md5:	0ec1d4ccd550510821a622eb91b893e8
Source13:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source13-md5:	ba27b06599556c572a26f03608471ee2
Source14:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source14-md5:	fd86abfe0ac7c5af61b15eb5367d0399
Source15:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source15-md5:	10fd55e004a582f87eed6796811bb3b8
Source16:	%{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source16-md5:	dbe5ddff57141f27778601df5571e182
Source17:	%{_urlprefix}/kdevelop-%{kdevelopver}.tar.bz2
# Source17-md5:	80d2216a0089fe142735d34ae8de6a0c
Source18:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source18-md5:	e95d1fbb698ec76966abfa5bdf96bd5e
%if %{with i18n}
Source19:	%{_urlprefix}/kde-i18n/kde-i18n-af-%{version}.tar.bz2
# Source19-md5:	d0ad0a95f63aacfa0dd11b90d7bbea29
Source20:	%{_urlprefix}/kde-i18n/kde-i18n-ar-%{version}.tar.bz2
# Source20-md5:	6211dd0fc0c4a78635bf101c5cd02b5e
Source21:	%{_urlprefix}/kde-i18n/kde-i18n-az-%{version}.tar.bz2
# Source21-md5:	11170e2e598ac406c08e85b9a1288b44
Source22:	%{_urlprefix}/kde-i18n/kde-i18n-be-%{version}.tar.bz2
# Source22-md5:	496f9b817f68bf07617f499c3da8d9e6
Source23:	%{_urlprefix}/kde-i18n/kde-i18n-bg-%{version}.tar.bz2
# Source23-md5:	eb39d6b16dbe6d3ce7892ada50e410fe
Source24:	%{_urlprefix}/kde-i18n/kde-i18n-bn-%{version}.tar.bz2
# Source24-md5:	7ce4868d7ae6cccbff8a5ba458bce8ea
Source25:	%{_urlprefix}/kde-i18n/kde-i18n-br-%{version}.tar.bz2
# Source25-md5:	1eb0051fddfe0f7ca5489999ad0a954b
Source26:	%{_urlprefix}/kde-i18n/kde-i18n-bs-%{version}.tar.bz2
# Source26-md5:	0e4c58a49b4b338c91741bc5a30925c7
Source27:	%{_urlprefix}/kde-i18n/kde-i18n-ca-%{version}.tar.bz2
# Source27-md5:	a59840da5d7b85206442e97ade2593e0
Source28:	%{_urlprefix}/kde-i18n/kde-i18n-cs-%{version}.tar.bz2
# Source28-md5:	5a93c2949eaee06e340fdd27eded8f0f
Source29:	%{_urlprefix}/kde-i18n/kde-i18n-csb-%{version}.tar.bz2
# Source29-md5:	d231225a393f42dbde0cbc5b10a80b2c
Source30:	%{_urlprefix}/kde-i18n/kde-i18n-cy-%{version}.tar.bz2
# Source30-md5:	653ffd44e9ba7fb06cfa3c85efc774c1
Source31:	%{_urlprefix}/kde-i18n/kde-i18n-da-%{version}.tar.bz2
# Source31-md5:	951f305c56de946b4184f0f2671d1d98
Source32:	%{_urlprefix}/kde-i18n/kde-i18n-de-%{version}.tar.bz2
# Source32-md5:	61a65a171c992f5569c4586e7d84ea3c
Source33:	%{_urlprefix}/kde-i18n/kde-i18n-el-%{version}.tar.bz2
# Source33-md5:	9e08c7b4717718f9de94eaed573e3c84
Source34:	%{_urlprefix}/kde-i18n/kde-i18n-en_GB-%{version}.tar.bz2
# Source34-md5:	2ff484173da22e8ca6257caeba0930c8
Source35:	%{_urlprefix}/kde-i18n/kde-i18n-eo-%{version}.tar.bz2
# Source35-md5:	1a4f43840f0e9db500f19e2098afbd2c
Source36:	%{_urlprefix}/kde-i18n/kde-i18n-es-%{version}.tar.bz2
# Source36-md5:	5c6c4e421fa082470dfc4c30317b9b61
Source37:	%{_urlprefix}/kde-i18n/kde-i18n-et-%{version}.tar.bz2
# Source37-md5:	d728e6d136b5d69692e72abd2486e487
Source38:	%{_urlprefix}/kde-i18n/kde-i18n-eu-%{version}.tar.bz2
# Source38-md5:	689f53701a70821cbcf0313d0b2f76ec
Source39:	%{_urlprefix}/kde-i18n/kde-i18n-fa-%{version}.tar.bz2
# Source39-md5:	19179b0afb39aef4f228878d5e29f517
Source40:	%{_urlprefix}/kde-i18n/kde-i18n-fi-%{version}.tar.bz2
# Source40-md5:	7ca0c2d8b52b53fc6afb9bbe32241db6
Source41:	%{_urlprefix}/kde-i18n/kde-i18n-fr-%{version}.tar.bz2
# Source41-md5:	c90cbd2437f4f83ac55f3e7b5fc168b0
Source42:	%{_urlprefix}/kde-i18n/kde-i18n-fy-%{version}.tar.bz2
# Source42-md5:	ce68f337016dd9dbf82bfc7c48e81824
Source43:	%{_urlprefix}/kde-i18n/kde-i18n-ga-%{version}.tar.bz2
# Source43-md5:	7320493d51e3a1c01f95e27afbff6c70
Source44:	%{_urlprefix}/kde-i18n/kde-i18n-gl-%{version}.tar.bz2
# Source44-md5:	09501e314fe3eef6274918c03e4fbd1a
Source45:	%{_urlprefix}/kde-i18n/kde-i18n-he-%{version}.tar.bz2
# Source45-md5:	074d617454bf56185361d4fa71aba96e
Source46:	%{_urlprefix}/kde-i18n/kde-i18n-hi-%{version}.tar.bz2
# Source46-md5:	07924a60a5246a49603d0cfb5b7675af
Source47:	%{_urlprefix}/kde-i18n/kde-i18n-hr-%{version}.tar.bz2
# Source47-md5:	58987c041e008c523bc074d9a18e6497
Source48:	%{_urlprefix}/kde-i18n/kde-i18n-hu-%{version}.tar.bz2
# Source48-md5:	7d0fac1410fdc08522f7ec4111245615
Source49:	%{_urlprefix}/kde-i18n/kde-i18n-is-%{version}.tar.bz2
# Source49-md5:	4196b2e01c5e959375ab9a3cf12c264f
Source50:	%{_urlprefix}/kde-i18n/kde-i18n-it-%{version}.tar.bz2
# Source50-md5:	d2dc789e4e77e195c36e900f472bf1f2
Source51:	%{_urlprefix}/kde-i18n/kde-i18n-ja-%{version}.tar.bz2
# Source51-md5:	42af0c4b72c8f4980f6b76e6643b573e
Source52:	%{_urlprefix}/kde-i18n/kde-i18n-kk-%{version}.tar.bz2
# Source52-md5:	a8ba5a53ab25643ff99b49c8e23848c1
Source53:	%{_urlprefix}/kde-i18n/kde-i18n-km-%{version}.tar.bz2
# Source53-md5:	8aa4613c4c0a4435d158354836b672a0
Source54:	%{_urlprefix}/kde-i18n/kde-i18n-ko-%{version}.tar.bz2
# Source54-md5:	769b35812de7bef6f8d7fd3b091413c9
Source55:	%{_urlprefix}/kde-i18n/kde-i18n-lt-%{version}.tar.bz2
# Source55-md5:	b5468778503a6d870e5cd8c09fcdb4ac
Source56:	%{_urlprefix}/kde-i18n/kde-i18n-lv-%{version}.tar.bz2
# Source56-md5:	63de24f8cfd7401874a234c517a06d5d
Source57:	%{_urlprefix}/kde-i18n/kde-i18n-mk-%{version}.tar.bz2
# Source57-md5:	15e49cd39c452410f4fe4a39ee4be6e1
Source58:	%{_urlprefix}/kde-i18n/kde-i18n-mn-%{version}.tar.bz2
# Source58-md5:	9fa32ae4216ddbadb54e12af5d78e8f0
Source59:	%{_urlprefix}/kde-i18n/kde-i18n-ms-%{version}.tar.bz2
# Source59-md5:	d5f6cb0e72559106a602d26e80fdb98c
Source60:	%{_urlprefix}/kde-i18n/kde-i18n-nb-%{version}.tar.bz2
# Source60-md5:	a1268287cf867503641ed9505dc271f6
Source61:	%{_urlprefix}/kde-i18n/kde-i18n-nds-%{version}.tar.bz2
# Source61-md5:	5db3906323e018bea9cf260364d5c5d3
Source62:	%{_urlprefix}/kde-i18n/kde-i18n-nl-%{version}.tar.bz2
# Source62-md5:	da217d35e1f8fab4d53622888459942c
Source63:	%{_urlprefix}/kde-i18n/kde-i18n-nn-%{version}.tar.bz2
# Source63-md5:	6cd1f400cd12c46a9826d3c51f8e5478
Source64:	%{_urlprefix}/kde-i18n/kde-i18n-pa-%{version}.tar.bz2
# Source64-md5:	3d0815c760939d6f0a03417001056ef1
Source65:	%{_urlprefix}/kde-i18n/kde-i18n-pl-%{version}.tar.bz2
# Source65-md5:	4f60d874b599abca41e1c1f34b8246af
Source66:	%{_urlprefix}/kde-i18n/kde-i18n-pt-%{version}.tar.bz2
# Source66-md5:	3a698240517f9193a760f2285bd891e4
Source67:	%{_urlprefix}/kde-i18n/kde-i18n-pt_BR-%{version}.tar.bz2
# Source67-md5:	e20c9a990701bd3e85a4c456815c652b
Source68:	%{_urlprefix}/kde-i18n/kde-i18n-ro-%{version}.tar.bz2
# Source68-md5:	1e11b29a81ac67d9545bbdd053428642
Source69:	%{_urlprefix}/kde-i18n/kde-i18n-ru-%{version}.tar.bz2
# Source69-md5:	eaf85b9354c4fa6af65e592e48b15041
Source70:	%{_urlprefix}/kde-i18n/kde-i18n-rw-%{version}.tar.bz2
# Source70-md5:	7a675983304f80561e4ce0948569663e
Source71:	%{_urlprefix}/kde-i18n/kde-i18n-se-%{version}.tar.bz2
# Source71-md5:	c39451b79cad946ea95dba338fce4196
Source72:	%{_urlprefix}/kde-i18n/kde-i18n-sk-%{version}.tar.bz2
# Source72-md5:	0d0611c736d0d2bc4cf46c0e411a6085
Source73:	%{_urlprefix}/kde-i18n/kde-i18n-sl-%{version}.tar.bz2
# Source73-md5:	91b950dcaf610ac25d6a882f4e5e8f1b
Source74:	%{_urlprefix}/kde-i18n/kde-i18n-sr-%{version}.tar.bz2
# Source74-md5:	f350a5572ddda5fad629d0ccd340d463
Source75:	%{_urlprefix}/kde-i18n/kde-i18n-sr@Latn-%{version}.tar.bz2
# Source75-md5:	5be944f2d524656389b5f06ea0a86229
Source76:	%{_urlprefix}/kde-i18n/kde-i18n-ss-%{version}.tar.bz2
# Source76-md5:	f8a454d22133f961c35ff4a5c2f298d0
Source77:	%{_urlprefix}/kde-i18n/kde-i18n-sv-%{version}.tar.bz2
# Source77-md5:	74ffe1e5cc7066f30f60483129f05072
Source78:	%{_urlprefix}/kde-i18n/kde-i18n-ta-%{version}.tar.bz2
# Source78-md5:	489d1ca912353049693edfe61fb1290c
Source79:	%{_urlprefix}/kde-i18n/kde-i18n-te-%{version}.tar.bz2
# Source79-md5:	eaf58f054eae1b3f3bce3757179b4d22
Source80:	%{_urlprefix}/kde-i18n/kde-i18n-tg-%{version}.tar.bz2
# Source80-md5:	e83a4c33e1301a5252b9c34bcb5412f5
Source81:	%{_urlprefix}/kde-i18n/kde-i18n-th-%{version}.tar.bz2
# Source81-md5:	0f9bd089333fc4b91ef88f15fa1dd7be
Source82:	%{_urlprefix}/kde-i18n/kde-i18n-tr-%{version}.tar.bz2
# Source82-md5:	9e6eb6503c467a5bfcfa2545abdf0c9e
Source83:	%{_urlprefix}/kde-i18n/kde-i18n-uk-%{version}.tar.bz2
# Source83-md5:	76b84d1592ed0b417b29048f0dfa57df
Source84:	%{_urlprefix}/kde-i18n/kde-i18n-uz-%{version}.tar.bz2
# Source84-md5:	239bc9e96e99de436a4f32b9b7f160b7
Source85:	%{_urlprefix}/kde-i18n/kde-i18n-vi-%{version}.tar.bz2
# Source85-md5:	48d5c0bb1e86e95c8000baeaddce130d
Source86:	%{_urlprefix}/kde-i18n/kde-i18n-wa-%{version}.tar.bz2
# Source86-md5:	3b262f503789d69d5f919ecfde422233
Source87:	%{_urlprefix}/kde-i18n/kde-i18n-zh_CN-%{version}.tar.bz2
# Source87-md5:	232a615fc0dedb13615d4d89dcd6d416
Source88:	%{_urlprefix}/kde-i18n/kde-i18n-zh_TW-%{version}.tar.bz2
# Source88-md5:	4e247ee8af22a2a08edb67d083425b90
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
