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
Release:	0.2
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
# Source4-md5:	a3fbdae9774545991aac839d9971f62c
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
# Source20-md5:	6ea143c07fec4c221163d518a6b4a6ba
Source21:	%{_urlprefix}/kde-l10n/kde-l10n-ca-%{version}.tar.bz2
# Source21-md5:	9d3b148e2519ecdd3413e75ced74d74d
Source22:	%{_urlprefix}/kde-l10n/kde-l10n-cs-%{version}.tar.bz2
# Source22-md5:	587b64f8faa341deacdcb001cb6c1d49
Source23:	%{_urlprefix}/kde-l10n/kde-l10n-csb-%{version}.tar.bz2
# Source23-md5:	3f554dca9db73ae823de6a59e6c1fccb
Source24:	%{_urlprefix}/kde-l10n/kde-l10n-da-%{version}.tar.bz2
# Source24-md5:	c0f1a76fa98261532b5b2ec7677b122c
Source25:	%{_urlprefix}/kde-l10n/kde-l10n-de-%{version}.tar.bz2
# Source25-md5:	4b4692687b61fe38b1936de557ad76fc
Source26:	%{_urlprefix}/kde-l10n/kde-l10n-el-%{version}.tar.bz2
# Source26-md5:	8a1cd5d567c3f73f3359aa33bf102eef
Source27:	%{_urlprefix}/kde-l10n/kde-l10n-en_GB-%{version}.tar.bz2
# Source27-md5:	5c812fd8335c70aabcff3c92bd6fad2e
Source28:	%{_urlprefix}/kde-l10n/kde-l10n-eo-%{version}.tar.bz2
# Source28-md5:	b35462218b9cfe29bf106aba8e8a0a3c
Source29:	%{_urlprefix}/kde-l10n/kde-l10n-es-%{version}.tar.bz2
# Source29-md5:	81e8d8a287c29b5ff099075d6e91f777
Source30:	%{_urlprefix}/kde-l10n/kde-l10n-et-%{version}.tar.bz2
# Source30-md5:	2515a4e55e10a01c5edad030e1c4ee58
Source31:	%{_urlprefix}/kde-l10n/kde-l10n-fi-%{version}.tar.bz2
# Source31-md5:	a47ae43bbe50e733e8ad33d91a54e60d
Source32:	%{_urlprefix}/kde-l10n/kde-l10n-fr-%{version}.tar.bz2
# Source32-md5:	ba690a8e9409f5c934b7db78c4b26da8
Source33:	%{_urlprefix}/kde-l10n/kde-l10n-fy-%{version}.tar.bz2
# Source33-md5:	4c0808126a3171a2f88b075aac46c3c1
Source34:	%{_urlprefix}/kde-l10n/kde-l10n-ga-%{version}.tar.bz2
# Source34-md5:	d5cd12cd6d1cf9329b6029406b5c1e0f
Source35:	%{_urlprefix}/kde-l10n/kde-l10n-gl-%{version}.tar.bz2
# Source35-md5:	66718341e6fbec3144a8a6e6ff12eaf9
Source36:	%{_urlprefix}/kde-l10n/kde-l10n-hi-%{version}.tar.bz2
# Source36-md5:	5759f8639cebab9e0eeb36092c4530cd
Source37:	%{_urlprefix}/kde-l10n/kde-l10n-hu-%{version}.tar.bz2
# Source37-md5:	c6cf7a32ef93f571a5929ad8567828c8
Source38:	%{_urlprefix}/kde-l10n/kde-l10n-it-%{version}.tar.bz2
# Source38-md5:	da1a689abd2cab8e16b63ebfbc1781a9
Source39:	%{_urlprefix}/kde-l10n/kde-l10n-ja-%{version}.tar.bz2
# Source39-md5:	21fdce21cbc277c99ab47548b1574277
Source40:	%{_urlprefix}/kde-l10n/kde-l10n-kk-%{version}.tar.bz2
# Source40-md5:	f77ef65e194f2a7d6a9471ae5b09cdb2
Source41:	%{_urlprefix}/kde-l10n/kde-l10n-km-%{version}.tar.bz2
# Source41-md5:	5334d54a5eb05d2f9e036bcbe436c7f1
Source42:	%{_urlprefix}/kde-l10n/kde-l10n-ko-%{version}.tar.bz2
# Source42-md5:	8517edcee2bd74c2b6ae2817b6419ef9
Source43:	%{_urlprefix}/kde-l10n/kde-l10n-ku-%{version}.tar.bz2
# Source43-md5:	c57f29f55575513b237e442de7db5621
Source44:	%{_urlprefix}/kde-l10n/kde-l10n-lt-%{version}.tar.bz2
# Source44-md5:	d197c08f054dd248217ab0fc0e349f08
Source45:	%{_urlprefix}/kde-l10n/kde-l10n-lv-%{version}.tar.bz2
# Source45-md5:	eb9a66e0a50ce7ca2956fcde580a4861
Source46:	%{_urlprefix}/kde-l10n/kde-l10n-mk-%{version}.tar.bz2
# Source46-md5:	c96fe5683d10216dab91044a6e8d067e
Source47:	%{_urlprefix}/kde-l10n/kde-l10n-ml-%{version}.tar.bz2
# Source47-md5:	2d17d45b54abd9e4d6ffb7760eff1e35
Source48:	%{_urlprefix}/kde-l10n/kde-l10n-nb-%{version}.tar.bz2
# Source48-md5:	5dabe6c3a7b7510d84ddc385e08da932
Source49:	%{_urlprefix}/kde-l10n/kde-l10n-nds-%{version}.tar.bz2
# Source49-md5:	aac9294f3b1550ef2721e34c958f21f0
Source50:	%{_urlprefix}/kde-l10n/kde-l10n-nl-%{version}.tar.bz2
# Source50-md5:	e0d37ba868babd2a139cbb288e9705ca
Source51:	%{_urlprefix}/kde-l10n/kde-l10n-nn-%{version}.tar.bz2
# Source51-md5:	b6ca1a9578358163c65ead322f172b6b
Source52:	%{_urlprefix}/kde-l10n/kde-l10n-pa-%{version}.tar.bz2
# Source52-md5:	b996ea1acc09bc3dc9432a96a948bb8e
Source53:	%{_urlprefix}/kde-l10n/kde-l10n-pl-%{version}.tar.bz2
# Source53-md5:	bdc1403f878cf95771ef1f55eaea5bf1
Source54:	%{_urlprefix}/kde-l10n/kde-l10n-pt-%{version}.tar.bz2
# Source54-md5:	5af76c57b9aa57163192bc5ca6f51d56
Source55:	%{_urlprefix}/kde-l10n/kde-l10n-pt_BR-%{version}.tar.bz2
# Source55-md5:	de0643177deb5e71994d9a6f011e3a7c
Source56:	%{_urlprefix}/kde-l10n/kde-l10n-ru-%{version}.tar.bz2
# Source56-md5:	4bf857f4f2fd8ca8fd647b02806216c8
Source57:	%{_urlprefix}/kde-l10n/kde-l10n-sl-%{version}.tar.bz2
# Source57-md5:	1a326e1e690d91e1452cf9ff5367c1a2
Source58:	%{_urlprefix}/kde-l10n/kde-l10n-sr-%{version}.tar.bz2
# Source58-md5:	05d7d2eb92edfceb0d0daa7967e531a8
Source59:	%{_urlprefix}/kde-l10n/kde-l10n-sv-%{version}.tar.bz2
# Source59-md5:	e7af80be264b24.1.07587631024ee10
Source60:	%{_urlprefix}/kde-l10n/kde-l10n-ta-%{version}.tar.bz2
# Source60-md5:	9958be9594b7a0e78a58628e9d549d0d
Source61:	%{_urlprefix}/kde-l10n/kde-l10n-th-%{version}.tar.bz2
# Source61-md5:	d694f4c914c5694ea891d96ee2050c7c
Source62:	%{_urlprefix}/kde-l10n/kde-l10n-tr-%{version}.tar.bz2
# Source62-md5:	7eb8f931768d071dee725226289a66df
Source63:	%{_urlprefix}/kde-l10n/kde-l10n-uk-%{version}.tar.bz2
# Source63-md5:	a5c44a250439d0653bacaffa89ecafbb
Source64:	%{_urlprefix}/kde-l10n/kde-l10n-wa-%{version}.tar.bz2
# Source64-md5:	a309ad111b09c205a94efa932f902e8b
Source65:	%{_urlprefix}/kde-l10n/kde-l10n-zh_CN-%{version}.tar.bz2
# Source65-md5:	48aef075bef64f8d57ba124620a17eaa
Source66:	%{_urlprefix}/kde-l10n/kde-l10n-zh_TW-%{version}.tar.bz2
# Source66-md5:	7ef18fe5d0fee8252ff0f1186b2f8a4f
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
