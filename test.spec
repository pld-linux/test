# - easy way to update all sources with new/old locales:
#   lynx -dump http://carme.pld-linux.org/~arekm/kde/kde-l10n | awk -vi=19 '/3.5.9.tar.bz2$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   sed -i -e 's,http://carme.pld-linux.org/~arekm/kde/kde-l10n/,%{_urlprefix}/kde-l10n/,' out
#   sed -i -e 's,3.5.9,%{version},' out
#   and then :r out in vim and ./builder -a5 the spec
%bcond_with	l10n
%define		_urlprefix	http://carme.pld-linux.org/~arekm/kde/
Summary:	Fetch KDE packages to distfiles
Name:		kdefetch
Version:	4.1.0
Release:	1	
License:	GPL
Group:		Networking/Hacking
Source0:	%{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source0-md5:	7d53001b2db8d7d8bd82a63e8be882ae
Source1:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source1-md5:	c814d39956c605a8cc60016a26a9401f
Source2:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source2-md5:	3de07b7d7bc5219d135c68dce4266861
Source3:	%{_urlprefix}/kdebase-%{version}.tar.bz2
# Source3-md5:	6b58b056d27e3103f087f12abe899a49
Source4:	%{_urlprefix}/kdebindings-%{version}.tar.bz2
# Source4-md5:	0552896de98a70c94baf76be68a1bc5a
Source5:	%{_urlprefix}/kdeedu-%{version}.tar.bz2
# Source5-md5:	0debdf843969152cb14b7186919b8c2b
Source6:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source6-md5:	2c0a4c089bf31ff9bd3133c3f58c4dc7
Source7:	%{_urlprefix}/kdegraphics-%{version}.tar.bz2
# Source7-md5:	ebaf7fc86d35587ce188e8e440bc8bcf
Source8:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source8-md5:	86496aed25d4dce440418b3064a27913
Source9:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source9-md5:	7965e42c3de193bde7f1e5437c9bedec
Source10:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source10-md5:	a28c85e1c51ed293e72813b80bb21a3c
Source11:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source11-md5:	5ccd9ca2bf92c0f94ac3b0bf5a5a1344
Source12:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source12-md5:	eb4e7bc753c80f617c113f31ab501168
Source13:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source13-md5:	c8c9c2f66f65fc7acfa8060d08667406
Source14:	%{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source14-md5:	456d811618e5417e224476089df9a3b3
Source15:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source15-md5:	58a1b35897cf0194476c9aac8a1d61e0
%if %{with l10n}
Source23:	%{_urlprefix}/kde-l10n/kde-l10n-bg-%{version}.tar.bz2
# Source23-md5:	6ea143c07fec4c221163d518a6b4a6ba
Source27:	%{_urlprefix}/kde-l10n/kde-l10n-ca-%{version}.tar.bz2
# Source27-md5:	9d3b148e2519ecdd3413e75ced74d74d
Source28:	%{_urlprefix}/kde-l10n/kde-l10n-cs-%{version}.tar.bz2
# Source28-md5:	587b64f8faa341deacdcb001cb6c1d49
Source29:	%{_urlprefix}/kde-l10n/kde-l10n-csb-%{version}.tar.bz2
# Source29-md5:	3f554dca9db73ae823de6a59e6c1fccb
Source31:	%{_urlprefix}/kde-l10n/kde-l10n-da-%{version}.tar.bz2
# Source31-md5:	c0f1a76fa98261532b5b2ec7677b122c
Source32:	%{_urlprefix}/kde-l10n/kde-l10n-de-%{version}.tar.bz2
# Source32-md5:	4b4692687b61fe38b1936de557ad76fc
Source33:	%{_urlprefix}/kde-l10n/kde-l10n-el-%{version}.tar.bz2
# Source33-md5:	8a1cd5d567c3f73f3359aa33bf102eef
Source34:	%{_urlprefix}/kde-l10n/kde-l10n-en_GB-%{version}.tar.bz2
# Source34-md5:	5c812fd8335c70aabcff3c92bd6fad2e
Source35:	%{_urlprefix}/kde-l10n/kde-l10n-eo-%{version}.tar.bz2
# Source35-md5:	b35462218b9cfe29bf106aba8e8a0a3c
Source36:	%{_urlprefix}/kde-l10n/kde-l10n-es-%{version}.tar.bz2
# Source36-md5:	81e8d8a287c29b5ff099075d6e91f777
Source37:	%{_urlprefix}/kde-l10n/kde-l10n-et-%{version}.tar.bz2
# Source37-md5:	2515a4e55e10a01c5edad030e1c4ee58
Source40:	%{_urlprefix}/kde-l10n/kde-l10n-fi-%{version}.tar.bz2
# Source40-md5:	a47ae43bbe50e733e8ad33d91a54e60d
Source41:	%{_urlprefix}/kde-l10n/kde-l10n-fr-%{version}.tar.bz2
# Source41-md5:	ba690a8e9409f5c934b7db78c4b26da8
Source42:	%{_urlprefix}/kde-l10n/kde-l10n-fy-%{version}.tar.bz2
# Source42-md5:	4c0808126a3171a2f88b075aac46c3c1
Source43:	%{_urlprefix}/kde-l10n/kde-l10n-ga-%{version}.tar.bz2
# Source43-md5:	d5cd12cd6d1cf9329b6029406b5c1e0f
Source44:	%{_urlprefix}/kde-l10n/kde-l10n-gl-%{version}.tar.bz2
# Source44-md5:	66718341e6fbec3144a8a6e6ff12eaf9
Source46:	%{_urlprefix}/kde-l10n/kde-l10n-hi-%{version}.tar.bz2
# Source46-md5:	5759f8639cebab9e0eeb36092c4530cd
Source48:	%{_urlprefix}/kde-l10n/kde-l10n-hu-%{version}.tar.bz2
# Source48-md5:	c6cf7a32ef93f571a5929ad8567828c8
Source50:	%{_urlprefix}/kde-l10n/kde-l10n-it-%{version}.tar.bz2
# Source50-md5:	da1a689abd2cab8e16b63ebfbc1781a9
Source51:	%{_urlprefix}/kde-l10n/kde-l10n-ja-%{version}.tar.bz2
# Source51-md5:	21fdce21cbc277c99ab47548b1574277
Source52:	%{_urlprefix}/kde-l10n/kde-l10n-kk-%{version}.tar.bz2
# Source52-md5:	f77ef65e194f2a7d6a9471ae5b09cdb2
Source53:	%{_urlprefix}/kde-l10n/kde-l10n-km-%{version}.tar.bz2
# Source53-md5:	5334d54a5eb05d2f9e036bcbe436c7f1
Source54:	%{_urlprefix}/kde-l10n/kde-l10n-ko-%{version}.tar.bz2
# Source54-md5:	8517edcee2bd74c2b6ae2817b6419ef9
Source45:	%{_urlprefix}/kde-l10n/kde-l10n-ku-%{version}.tar.bz2
# Source45-md5:	c57f29f55575513b237e442de7db5621
Source55:	%{_urlprefix}/kde-l10n/kde-l10n-lt-%{version}.tar.bz2
# Source55-md5:	d197c08f054dd248217ab0fc0e349f08
Source56:	%{_urlprefix}/kde-l10n/kde-l10n-lv-%{version}.tar.bz2
# Source56-md5:	eb9a66e0a50ce7ca2956fcde580a4861
Source57:	%{_urlprefix}/kde-l10n/kde-l10n-mk-%{version}.tar.bz2
# Source57-md5:	c96fe5683d10216dab91044a6e8d067e
Source58:	%{_urlprefix}/kde-l10n/kde-l10n-ml-%{version}.tar.bz2
# Source58-md5:	2d17d45b54abd9e4d6ffb7760eff1e35
Source60:	%{_urlprefix}/kde-l10n/kde-l10n-nb-%{version}.tar.bz2
# Source60-md5:	5dabe6c3a7b7510d84ddc385e08da932
Source61:	%{_urlprefix}/kde-l10n/kde-l10n-nds-%{version}.tar.bz2
# Source61-md5:	aac9294f3b1550ef2721e34c958f21f0
Source62:	%{_urlprefix}/kde-l10n/kde-l10n-nl-%{version}.tar.bz2
# Source62-md5:	e0d37ba868babd2a139cbb288e9705ca
Source63:	%{_urlprefix}/kde-l10n/kde-l10n-nn-%{version}.tar.bz2
# Source63-md5:	b6ca1a9578358163c65ead322f172b6b
Source64:	%{_urlprefix}/kde-l10n/kde-l10n-pa-%{version}.tar.bz2
# Source64-md5:	b996ea1acc09bc3dc9432a96a948bb8e
Source65:	%{_urlprefix}/kde-l10n/kde-l10n-pl-%{version}.tar.bz2
# Source65-md5:	bdc1403f878cf95771ef1f55eaea5bf1
Source66:	%{_urlprefix}/kde-l10n/kde-l10n-pt-%{version}.tar.bz2
# Source66-md5:	5af76c57b9aa57163192bc5ca6f51d56
Source67:	%{_urlprefix}/kde-l10n/kde-l10n-pt_BR-%{version}.tar.bz2
# Source67-md5:	de0643177deb5e71994d9a6f011e3a7c
Source69:	%{_urlprefix}/kde-l10n/kde-l10n-ru-%{version}.tar.bz2
# Source69-md5:	4bf857f4f2fd8ca8fd647b02806216c8
Source73:	%{_urlprefix}/kde-l10n/kde-l10n-sl-%{version}.tar.bz2
# Source73-md5:	1a326e1e690d91e1452cf9ff5367c1a2
Source74:	%{_urlprefix}/kde-l10n/kde-l10n-sr-%{version}.tar.bz2
# Source74-md5:	05d7d2eb92edfceb0d0daa7967e531a8
Source77:	%{_urlprefix}/kde-l10n/kde-l10n-sv-%{version}.tar.bz2
# Source77-md5:	e7af80be264b2345897587631024ee10
Source78:	%{_urlprefix}/kde-l10n/kde-l10n-ta-%{version}.tar.bz2
# Source78-md5:	9958be9594b7a0e78a58628e9d549d0d
Source81:	%{_urlprefix}/kde-l10n/kde-l10n-th-%{version}.tar.bz2
# Source81-md5:	d694f4c914c5694ea891d96ee2050c7c
Source82:	%{_urlprefix}/kde-l10n/kde-l10n-tr-%{version}.tar.bz2
# Source82-md5:	7eb8f931768d071dee725226289a66df
Source83:	%{_urlprefix}/kde-l10n/kde-l10n-uk-%{version}.tar.bz2
# Source83-md5:	a5c44a250439d0653bacaffa89ecafbb
Source86:	%{_urlprefix}/kde-l10n/kde-l10n-wa-%{version}.tar.bz2
# Source86-md5:	a309ad111b09c205a94efa932f902e8b
Source87:	%{_urlprefix}/kde-l10n/kde-l10n-zh_CN-%{version}.tar.bz2
# Source87-md5:	48aef075bef64f8d57ba124620a17eaa
Source88:	%{_urlprefix}/kde-l10n/kde-l10n-zh_TW-%{version}.tar.bz2
# Source88-md5:	7ef18fe5d0fee8252ff0f1186b2f8a4f
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
