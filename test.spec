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
# Source19-md5:	9fc56e59816271c09922f08738ebce6f
Source20:	%{_urlprefix}/kde-i18n/kde-i18n-ar-%{version}.tar.bz2
# Source20-md5:	d2d0628ce887766965b6bca2015f99c8
Source21:	%{_urlprefix}/kde-i18n/kde-i18n-az-%{version}.tar.bz2
# Source21-md5:	c2039b4e65e61dbbe095032d6a6f5e38
Source22:	%{_urlprefix}/kde-i18n/kde-i18n-bg-%{version}.tar.bz2
# Source22-md5:	f865993d0be0eef709e86fcefd4e9d01
Source23:	%{_urlprefix}/kde-i18n/kde-i18n-bn-%{version}.tar.bz2
# Source23-md5:	9e329981b6938e358c9b6647fb07b8c2
Source24:	%{_urlprefix}/kde-i18n/kde-i18n-br-%{version}.tar.bz2
# Source24-md5:	d112abe01375048fde57c58f2e60e63a
Source25:	%{_urlprefix}/kde-i18n/kde-i18n-bs-%{version}.tar.bz2
# Source25-md5:	4828cc85cdb5b242c37af963432d1792
Source26:	%{_urlprefix}/kde-i18n/kde-i18n-ca-%{version}.tar.bz2
# Source26-md5:	4ca083e7a1702365f2de35ff79fd41e0
Source27:	%{_urlprefix}/kde-i18n/kde-i18n-cs-%{version}.tar.bz2
# Source27-md5:	350a29c5166640bb7f4030dc45da6c48
Source28:	%{_urlprefix}/kde-i18n/kde-i18n-cy-%{version}.tar.bz2
# Source28-md5:	49b3d60531a0fbb050ec30df8135c07f
Source29:	%{_urlprefix}/kde-i18n/kde-i18n-da-%{version}.tar.bz2
# Source29-md5:	a13e84cbdb6b6fd89034efa33ea87266
Source30:	%{_urlprefix}/kde-i18n/kde-i18n-de-%{version}.tar.bz2
# Source30-md5:	ffba95578d4ffd07dd5488a6610cb3c8
Source31:	%{_urlprefix}/kde-i18n/kde-i18n-el-%{version}.tar.bz2
# Source31-md5:	995d8c13bc0eccacc5c53d40b948e03e
Source32:	%{_urlprefix}/kde-i18n/kde-i18n-en_GB-%{version}.tar.bz2
# Source32-md5:	1efad85761ec1fa03290204e562adac4
Source33:	%{_urlprefix}/kde-i18n/kde-i18n-eo-%{version}.tar.bz2
# Source33-md5:	853f24c711ed787adfd901d6be5f5b3f
Source34:	%{_urlprefix}/kde-i18n/kde-i18n-es-%{version}.tar.bz2
# Source34-md5:	cc0c23885bc71637cb045069896545b5
Source35:	%{_urlprefix}/kde-i18n/kde-i18n-et-%{version}.tar.bz2
# Source35-md5:	4103433d895c818c4213993ec818aad1
Source36:	%{_urlprefix}/kde-i18n/kde-i18n-eu-%{version}.tar.bz2
# Source36-md5:	e11781e87059cc9cc1570fcd4d3c9279
Source37:	%{_urlprefix}/kde-i18n/kde-i18n-fa-%{version}.tar.bz2
# Source37-md5:	bc71ddcd6b6c6fa765591d12befefc66
Source38:	%{_urlprefix}/kde-i18n/kde-i18n-fi-%{version}.tar.bz2
# Source38-md5:	18682d8351c70d2b483c2b55706025f0
Source39:	%{_urlprefix}/kde-i18n/kde-i18n-fr-%{version}.tar.bz2
# Source39-md5:	f6ddf4a9eeb3748fcbf781ff4c3c4edb
Source40:	%{_urlprefix}/kde-i18n/kde-i18n-fy-%{version}.tar.bz2
# Source40-md5:	d6c5182349c6b448edcd63a8cb737859
Source41:	%{_urlprefix}/kde-i18n/kde-i18n-ga-%{version}.tar.bz2
# Source41-md5:	e33342045b81dd4df200f56d615d3590
Source42:	%{_urlprefix}/kde-i18n/kde-i18n-gl-%{version}.tar.bz2
# Source42-md5:	7a25eef435e4daca31f6507be216b060
Source43:	%{_urlprefix}/kde-i18n/kde-i18n-he-%{version}.tar.bz2
# Source43-md5:	0f2fb7c7538ce15fbbfb5a4f19e78b73
Source44:	%{_urlprefix}/kde-i18n/kde-i18n-hi-%{version}.tar.bz2
# Source44-md5:	46cc5b60e42f260a6ee4d4b5cc53851b
Source45:	%{_urlprefix}/kde-i18n/kde-i18n-hr-%{version}.tar.bz2
# Source45-md5:	7ec644927e8d4606caf0a017f5c177ea
Source46:	%{_urlprefix}/kde-i18n/kde-i18n-hu-%{version}.tar.bz2
# Source46-md5:	f10056e1dbb1955f2ba3cbba8a50a08b
Source47:	%{_urlprefix}/kde-i18n/kde-i18n-is-%{version}.tar.bz2
# Source47-md5:	b86b28fec7ff948c97df15c972553900
Source48:	%{_urlprefix}/kde-i18n/kde-i18n-it-%{version}.tar.bz2
# Source48-md5:	a04a26135303cef25f74373e07df0157
Source49:	%{_urlprefix}/kde-i18n/kde-i18n-ja-%{version}.tar.bz2
# Source49-md5:	797df078ef3dc7f3cd095311a62c56e2
Source50:	%{_urlprefix}/kde-i18n/kde-i18n-kk-%{version}.tar.bz2
# Source50-md5:	0d8295e47c2ee65da1845e224470c5dd
Source51:	%{_urlprefix}/kde-i18n/kde-i18n-km-%{version}.tar.bz2
# Source51-md5:	b1564f042ba6f7cd5cb2341d3f18f86f
Source52:	%{_urlprefix}/kde-i18n/kde-i18n-ko-%{version}.tar.bz2
# Source52-md5:	32ede9542bdc84f33ea56d5d4b33c7f2
Source53:	%{_urlprefix}/kde-i18n/kde-i18n-lt-%{version}.tar.bz2
# Source53-md5:	6774803f35f4accba712a7fa1fce50d8
Source54:	%{_urlprefix}/kde-i18n/kde-i18n-lv-%{version}.tar.bz2
# Source54-md5:	2e67dcb10511415f09f33e2142ebc504
Source55:	%{_urlprefix}/kde-i18n/kde-i18n-mk-%{version}.tar.bz2
# Source55-md5:	a8fafdfe962f310ca968a81a7db0adbe
Source56:	%{_urlprefix}/kde-i18n/kde-i18n-mn-%{version}.tar.bz2
# Source56-md5:	a375fb5e27447e566a95660057af122e
Source57:	%{_urlprefix}/kde-i18n/kde-i18n-ms-%{version}.tar.bz2
# Source57-md5:	566168896b51d93f9e1c11a0ec84db68
Source58:	%{_urlprefix}/kde-i18n/kde-i18n-nb-%{version}.tar.bz2
# Source58-md5:	0b66b0265556c7892f13d20d30f61423
Source59:	%{_urlprefix}/kde-i18n/kde-i18n-nds-%{version}.tar.bz2
# Source59-md5:	f5c1fd976b345bfa5a5ec91aec0c1d29
Source60:	%{_urlprefix}/kde-i18n/kde-i18n-nl-%{version}.tar.bz2
# Source60-md5:	0bc7c76717a67da18a5bcfb1dda278ef
Source61:	%{_urlprefix}/kde-i18n/kde-i18n-nn-%{version}.tar.bz2
# Source61-md5:	9364ceaf89c1e3b1d5d957d0f8cc9826
Source62:	%{_urlprefix}/kde-i18n/kde-i18n-pa-%{version}.tar.bz2
# Source62-md5:	20d4043b002dad7fc9ff4aa319561f27
Source63:	%{_urlprefix}/kde-i18n/kde-i18n-pl-%{version}.tar.bz2
# Source63-md5:	c5a58fb84ce0f19e908b3a65f699e880
Source64:	%{_urlprefix}/kde-i18n/kde-i18n-pt-%{version}.tar.bz2
# Source64-md5:	696b4d75f81231e43f898e7c703d133d
Source65:	%{_urlprefix}/kde-i18n/kde-i18n-pt_BR-%{version}.tar.bz2
# Source65-md5:	c7fc3d50c3fb27d8560412156dc464fb
Source66:	%{_urlprefix}/kde-i18n/kde-i18n-ro-%{version}.tar.bz2
# Source66-md5:	81eb9ede8fa9073a997d3366ca236f96
Source67:	%{_urlprefix}/kde-i18n/kde-i18n-ru-%{version}.tar.bz2
# Source67-md5:	b0a0edf56a5444d74dca527556a59ae3
Source68:	%{_urlprefix}/kde-i18n/kde-i18n-rw-%{version}.tar.bz2
# Source68-md5:	69240b537d68e84a727ecbc54a471cb0
Source69:	%{_urlprefix}/kde-i18n/kde-i18n-se-%{version}.tar.bz2
# Source69-md5:	a5dc3120ccbea37cc4e6423d4bb2fbac
Source70:	%{_urlprefix}/kde-i18n/kde-i18n-sk-%{version}.tar.bz2
# Source70-md5:	b2c5da89f8b5df63991deb47674bdbb9
Source71:	%{_urlprefix}/kde-i18n/kde-i18n-sl-%{version}.tar.bz2
# Source71-md5:	5b2eff146028bffeb84315aaafa5ea5d
Source72:	%{_urlprefix}/kde-i18n/kde-i18n-sr-%{version}.tar.bz2
# Source72-md5:	06099c0a4a7c84115e06c40256ed97ff
Source73:	%{_urlprefix}/kde-i18n/kde-i18n-sr@Latn-%{version}.tar.bz2
# Source73-md5:	1cbde47602550b462e91e4a7b5bbe8c8
Source74:	%{_urlprefix}/kde-i18n/kde-i18n-ss-%{version}.tar.bz2
# Source74-md5:	def410b2a9ff67e03138c2acd98382a3
Source75:	%{_urlprefix}/kde-i18n/kde-i18n-sv-%{version}.tar.bz2
# Source75-md5:	26fcaf78f44e67e3bda09e187fa85374
Source76:	%{_urlprefix}/kde-i18n/kde-i18n-ta-%{version}.tar.bz2
# Source76-md5:	c6798c99e32ea3b1e4817b1f1e2857b5
Source77:	%{_urlprefix}/kde-i18n/kde-i18n-tg-%{version}.tar.bz2
# Source77-md5:	41b096c7409bcdc7d32aa97f3547d4bc
Source78:	%{_urlprefix}/kde-i18n/kde-i18n-tr-%{version}.tar.bz2
# Source78-md5:	90326b113d8e77497a3eb1d0d87ed65c
Source79:	%{_urlprefix}/kde-i18n/kde-i18n-uk-%{version}.tar.bz2
# Source79-md5:	cee28788e68efeb77fd672a31e206e8e
Source80:	%{_urlprefix}/kde-i18n/kde-i18n-uz-%{version}.tar.bz2
# Source80-md5:	068da2a91ee5a06a4c9c18853336074e
Source81:	%{_urlprefix}/kde-i18n/kde-i18n-vi-%{version}.tar.bz2
# Source81-md5:	f8aa01eea219b5ed34ecc312a42c50fe
Source82:	%{_urlprefix}/kde-i18n/kde-i18n-zh_CN-%{version}.tar.bz2
# Source82-md5:	ef0bf6dcdf3c05bf6a775abfae1944b9
Source83:	%{_urlprefix}/kde-i18n/kde-i18n-zh_TW-%{version}.tar.bz2
# Source83-md5:	d5a68ed78b436874bb41c1e9c423b3ac
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alien allows you to convert Debian, Stampede and Slackware Packages
into PLD packages, which can be installed with rpm. It can also
convert into Slackware, Debian, and Stampede packages. This is a tool
only suitable for binary packages.

%prep
exit 1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
