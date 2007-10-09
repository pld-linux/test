%bcond_with	i18n
%define		_urlprefix	http://carme.pld-linux.org/~arekm/kde/
%define		artsver	1.5.8
%define		kdevelopver 3.5.0
Summary:	Fetch KDE packages to distfiles
Name:		kdefetch
Version:	3.5.8
Release:	1
License:	GPL
Group:		Networking/Hacking
Source0:	%{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source0-md5:	0ede2d48df626aa436dbe6c741d575f1
Source1:	%{_urlprefix}/kdeaddons-%{version}.tar.bz2
# Source1-md5:	4a338f14210ad920bb54624cd330dd89
Source2:	%{_urlprefix}/arts-%{artsver}.tar.bz2
# Source2-md5:	061ce49351d970a81f4c0a1b0339fb34
Source3:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source3-md5:	324a44d854a92177e71954f9264c98a8
Source4:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source4-md5:	03becf82a233e6007e9372ffa5756d0b
Source5:	%{_urlprefix}/kdebase-%{version}.tar.bz2
# Source5-md5:	9990c669229daaaa8fca4c5e354441fd
Source6:	%{_urlprefix}/kdebindings-%{version}.tar.bz2
# Source6-md5:	4325d22ac70d3945609bd952c19e793b
Source7:	%{_urlprefix}/kdeedu-%{version}.tar.bz2
# Source7-md5:	aaae4c6fe82c806eb20942178cadad9e
Source8:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source8-md5:	786ee4e47820d92aef7db73424b9604c
Source9:	%{_urlprefix}/kdegraphics-%{version}.tar.bz2
# Source9-md5:	a3a31fc0e5b791ef330dd0627095d90f
Source10:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source10-md5:	acaa37e79e840d10dca326277a20863c
Source11:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source11-md5:	9f3c95231ea265b09f3010adb954ae30
Source12:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source12-md5:	0e79374d1109d937b0c9bdd3a75e7476
Source13:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source13-md5:	a1ffff553f1d6739c7791891028b176b
Source14:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source14-md5:	c809c15eb8c09a7eb2d070395202910b
Source15:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source15-md5:	b42c1f08e5c4ac93a04aadb75679139f
Source16:	%{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source16-md5:	d1a0fcc83f35428a76cf7523a04ba19c
Source17:	%{_urlprefix}/kdevelop-%{kdevelopver}.tar.bz2
# Source17-md5:	1101077b3a0164da463f60cad4f13e25
Source18:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source18-md5:	6c17c4b71a4d306da4b81a0cfd3116e1
%if %{with i18n}
Source19:	%{_urlprefix}/kde-i18n/kde-i18n-af-%{version}.tar.bz2
# Source19-md5:	88c320ea5320f6af8236a0ae16483d61
Source20:	%{_urlprefix}/kde-i18n/kde-i18n-ar-%{version}.tar.bz2
# Source20-md5:	3f61f06685f66214ce28426a42419696
Source21:	%{_urlprefix}/kde-i18n/kde-i18n-az-%{version}.tar.bz2
# Source21-md5:	770821f4d53662a9052e26b0b7fc0d86
Source22:	%{_urlprefix}/kde-i18n/kde-i18n-bg-%{version}.tar.bz2
# Source22-md5:	071791e43caac2c3ca1b5f676c3486d7
Source23:	%{_urlprefix}/kde-i18n/kde-i18n-bn-%{version}.tar.bz2
# Source23-md5:	ce4076af2523378de16d52c553a5570a
Source24:	%{_urlprefix}/kde-i18n/kde-i18n-br-%{version}.tar.bz2
# Source24-md5:	903d567ecd398d5dcaac10521f1e2d1a
Source25:	%{_urlprefix}/kde-i18n/kde-i18n-bs-%{version}.tar.bz2
# Source25-md5:	d12aa470ab906726a4e7098b66a3c31d
Source26:	%{_urlprefix}/kde-i18n/kde-i18n-ca-%{version}.tar.bz2
# Source26-md5:	9f1d629826873f17c0c080da113160e7
Source27:	%{_urlprefix}/kde-i18n/kde-i18n-cs-%{version}.tar.bz2
# Source27-md5:	db203a2ae671d59032b50511f5f590b4
Source28:	%{_urlprefix}/kde-i18n/kde-i18n-cy-%{version}.tar.bz2
# Source28-md5:	148faedcc0326cf7256dec99d92bde01
Source29:	%{_urlprefix}/kde-i18n/kde-i18n-da-%{version}.tar.bz2
# Source29-md5:	1fd0439f89c93563a5e0c88e9fe91b88
Source30:	%{_urlprefix}/kde-i18n/kde-i18n-de-%{version}.tar.bz2
# Source30-md5:	541d0f5189126addfdece3410027a6cd
Source31:	%{_urlprefix}/kde-i18n/kde-i18n-el-%{version}.tar.bz2
# Source31-md5:	292682993de7ad01f25715e984ef679e
Source32:	%{_urlprefix}/kde-i18n/kde-i18n-en_GB-%{version}.tar.bz2
# Source32-md5:	656f2b65b1d4157deee397974969e38c
Source33:	%{_urlprefix}/kde-i18n/kde-i18n-eo-%{version}.tar.bz2
# Source33-md5:	fbc2fa7fe6f43cb89328bbc8815487f9
Source34:	%{_urlprefix}/kde-i18n/kde-i18n-es-%{version}.tar.bz2
# Source34-md5:	d6faefeee2d7351cdff5d09d12585785
Source35:	%{_urlprefix}/kde-i18n/kde-i18n-et-%{version}.tar.bz2
# Source35-md5:	3cc413ec7e20a11784779c55c059923f
Source36:	%{_urlprefix}/kde-i18n/kde-i18n-eu-%{version}.tar.bz2
# Source36-md5:	6b47aa2863640739973a5ca390f4c9eb
Source37:	%{_urlprefix}/kde-i18n/kde-i18n-fa-%{version}.tar.bz2
# Source37-md5:	fbbfb775f1b64f8704e29d7fa86a0ab6
Source38:	%{_urlprefix}/kde-i18n/kde-i18n-fi-%{version}.tar.bz2
# Source38-md5:	126039c2f5e3f4bff0036971069a8bed
Source39:	%{_urlprefix}/kde-i18n/kde-i18n-fr-%{version}.tar.bz2
# Source39-md5:	2a64410a4692b7e248fde1e4bdc09f86
Source40:	%{_urlprefix}/kde-i18n/kde-i18n-fy-%{version}.tar.bz2
# Source40-md5:	8f115a9c965f7d18229e8891245c3c13
Source41:	%{_urlprefix}/kde-i18n/kde-i18n-ga-%{version}.tar.bz2
# Source41-md5:	fd7235f1f0b9af0a9c84f835c8c31439
Source42:	%{_urlprefix}/kde-i18n/kde-i18n-gl-%{version}.tar.bz2
# Source42-md5:	243cb631a971a6a4eb6601ffd5b953b6
Source43:	%{_urlprefix}/kde-i18n/kde-i18n-he-%{version}.tar.bz2
# Source43-md5:	fc1c6cba3c11fdc184f334674228a9f3
Source44:	%{_urlprefix}/kde-i18n/kde-i18n-hi-%{version}.tar.bz2
# Source44-md5:	c41c26db86e54efa21748f02ef2f5be4
Source45:	%{_urlprefix}/kde-i18n/kde-i18n-hr-%{version}.tar.bz2
# Source45-md5:	099d3da8a4d375a7e52d88316d4e880b
Source46:	%{_urlprefix}/kde-i18n/kde-i18n-hu-%{version}.tar.bz2
# Source46-md5:	cb519a636b9c8d178578474279a4819f
Source47:	%{_urlprefix}/kde-i18n/kde-i18n-is-%{version}.tar.bz2
# Source47-md5:	50c914274a83c81bc0e000e56aeb7e85
Source48:	%{_urlprefix}/kde-i18n/kde-i18n-it-%{version}.tar.bz2
# Source48-md5:	00f433d262edcea8f2aac4ce02d1ea63
Source49:	%{_urlprefix}/kde-i18n/kde-i18n-ja-%{version}.tar.bz2
# Source49-md5:	1a1b8c4c752c43fcb38767608134fc78
Source50:	%{_urlprefix}/kde-i18n/kde-i18n-kk-%{version}.tar.bz2
# Source50-md5:	7c9ef1b73d57eb865446acd78df662b0
Source51:	%{_urlprefix}/kde-i18n/kde-i18n-km-%{version}.tar.bz2
# Source51-md5:	aab309ee84138818490b5f261bbbdc00
Source52:	%{_urlprefix}/kde-i18n/kde-i18n-ko-%{version}.tar.bz2
# Source52-md5:	ffb76e99343d36c10e88c2c208610f67
Source53:	%{_urlprefix}/kde-i18n/kde-i18n-lt-%{version}.tar.bz2
# Source53-md5:	2d59da372e7b4421fc91c4cb5597a418
Source54:	%{_urlprefix}/kde-i18n/kde-i18n-lv-%{version}.tar.bz2
# Source54-md5:	35a369665f244a85f3b428752e060793
Source55:	%{_urlprefix}/kde-i18n/kde-i18n-mk-%{version}.tar.bz2
# Source55-md5:	7d3214430aa1d68f203f23f2fcca0ebe
Source56:	%{_urlprefix}/kde-i18n/kde-i18n-mn-%{version}.tar.bz2
# Source56-md5:	8946c24129e8f8940084e419c30af8e7
Source57:	%{_urlprefix}/kde-i18n/kde-i18n-ms-%{version}.tar.bz2
# Source57-md5:	238bf49769942b979cbddcaccea5b710
Source58:	%{_urlprefix}/kde-i18n/kde-i18n-nb-%{version}.tar.bz2
# Source58-md5:	01d114b6fa87ad9b5f2048955e7d52e0
Source59:	%{_urlprefix}/kde-i18n/kde-i18n-nds-%{version}.tar.bz2
# Source59-md5:	9fd018b9f51cc8cf6378b304ae7cdbbc
Source60:	%{_urlprefix}/kde-i18n/kde-i18n-nl-%{version}.tar.bz2
# Source60-md5:	97775bbdcaf8d8185eff9ee0f031ab1b
Source61:	%{_urlprefix}/kde-i18n/kde-i18n-nn-%{version}.tar.bz2
# Source61-md5:	67b4f67411042fbb47225d796519e259
Source62:	%{_urlprefix}/kde-i18n/kde-i18n-pa-%{version}.tar.bz2
# Source62-md5:	dd46c1dcfa3d5e1c0d28a91ce80a7e08
Source63:	%{_urlprefix}/kde-i18n/kde-i18n-pl-%{version}.tar.bz2
# Source63-md5:	5467708649518662692c93d3c12dcebb
Source64:	%{_urlprefix}/kde-i18n/kde-i18n-pt-%{version}.tar.bz2
# Source64-md5:	eef833022d79bbb27e14ab3b9b2ea4c5
Source65:	%{_urlprefix}/kde-i18n/kde-i18n-pt_BR-%{version}.tar.bz2
# Source65-md5:	615fb261ba06abc14ea7128ba142ccab
Source66:	%{_urlprefix}/kde-i18n/kde-i18n-ro-%{version}.tar.bz2
# Source66-md5:	459971f0e4ed5cdb6741733ac8aa4979
Source67:	%{_urlprefix}/kde-i18n/kde-i18n-ru-%{version}.tar.bz2
# Source67-md5:	5b88cf9e5ab1e226885118b2022b29b3
Source68:	%{_urlprefix}/kde-i18n/kde-i18n-rw-%{version}.tar.bz2
# Source68-md5:	7bb554107c402f63c3b38f9d6197a985
Source69:	%{_urlprefix}/kde-i18n/kde-i18n-se-%{version}.tar.bz2
# Source69-md5:	d385011a25431cec644c70a40cc06d07
Source70:	%{_urlprefix}/kde-i18n/kde-i18n-sk-%{version}.tar.bz2
# Source70-md5:	bdc21017fdee0fc26045ed8b14cb72d8
Source71:	%{_urlprefix}/kde-i18n/kde-i18n-sl-%{version}.tar.bz2
# Source71-md5:	c5393c84882a953acb2b92296d2324a2
Source72:	%{_urlprefix}/kde-i18n/kde-i18n-sr-%{version}.tar.bz2
# Source72-md5:	ceadb723611f3c32cc8f57a61dbb4ef1
Source73:	%{_urlprefix}/kde-i18n/kde-i18n-sr@Latn-%{version}.tar.bz2
# Source73-md5:	d72f37a5a3a2f060a0f5024cd5f63440
Source74:	%{_urlprefix}/kde-i18n/kde-i18n-ss-%{version}.tar.bz2
# Source74-md5:	1e66fa69e5b3ed74e986d9b98a7502e0
Source75:	%{_urlprefix}/kde-i18n/kde-i18n-sv-%{version}.tar.bz2
# Source75-md5:	8b7fe01c959630fca516151b5635b525
Source76:	%{_urlprefix}/kde-i18n/kde-i18n-ta-%{version}.tar.bz2
# Source76-md5:	59e6f48dc6ce52ad6792579dd97a468b
Source77:	%{_urlprefix}/kde-i18n/kde-i18n-tg-%{version}.tar.bz2
# Source77-md5:	3a5286aabef22fbab5e3ec94c388bc8e
Source78:	%{_urlprefix}/kde-i18n/kde-i18n-tr-%{version}.tar.bz2
# Source78-md5:	317e4f9dd07e907f88f2c0331692a7c7
Source79:	%{_urlprefix}/kde-i18n/kde-i18n-uk-%{version}.tar.bz2
# Source79-md5:	2187a208bfdff609078e3afeaf8e02f3
Source80:	%{_urlprefix}/kde-i18n/kde-i18n-uz-%{version}.tar.bz2
# Source80-md5:	c36c41e57e7677705732e43d69d51b63
Source81:	%{_urlprefix}/kde-i18n/kde-i18n-vi-%{version}.tar.bz2
# Source81-md5:	5e025aa483bfd52d05ad9b28028c3515
Source82:	%{_urlprefix}/kde-i18n/kde-i18n-zh_CN-%{version}.tar.bz2
# Source82-md5:	29e2e6756afa3a6ad1b9014c91137b18
Source83:	%{_urlprefix}/kde-i18n/kde-i18n-zh_TW-%{version}.tar.bz2
# Source83-md5:	7defcfa0506759695f92e2835b06abeb
Source84:	%{_urlprefix}/kde-i18n/kde-i18n-wa-%{version}.tar.bz2
# Source84-md5:	80ab89389e45431fedf5b57630a91108
Source85:	%{_urlprefix}/kde-i18n/kde-i18n-te-%{version}.tar.bz2
# Source85-md5:	99623b9d093f65c63c74a6e433eef14c
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
