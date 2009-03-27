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
Version:	4.2.2
Release:	1
License:	GPL
Group:		Networking/Hacking
Source100:	kde4diff.sh
Source0:	%{_urlprefix}/kdeaccessibility-%{version}.tar.bz2
# Source0-md5:	7fd255ecf2274f868d4634b0f44e41af
Source1:	%{_urlprefix}/kdeadmin-%{version}.tar.bz2
# Source1-md5:	b9104de38fa36962a2812aa9cae8fc5f
Source2:	%{_urlprefix}/kdeartwork-%{version}.tar.bz2
# Source2-md5:	2315d64bb543decdb602b01376f5fc1e
Source3:	%{_urlprefix}/kdebase-%{version}.tar.bz2
# Source3-md5:	7f6b0d5051f251d0f34ee797a8e2b54a
Source4:	%{_urlprefix}/kdebase-runtime-%{version}.tar.bz2
# Source4-md5:	cff3fbdb98faeec0ae65d8caea7a5b0f
Source5:	%{_urlprefix}/kdebase-workspace-%{version}.tar.bz2
# Source5-md5:	ac494815044eefc3a181488871225eda
Source6:	%{_urlprefix}/kdebindings-%{version}.tar.bz2
# Source6-md5:	56adf7d276957d87102457165739f764
Source7:	%{_urlprefix}/kdeedu-%{version}.tar.bz2
# Source7-md5:	132724e6d8d874372c218ed138cb2091
Source8:	%{_urlprefix}/kdegames-%{version}.tar.bz2
# Source8-md5:	d78bba18dcf6bcdf86f77b26596f4c71
Source9:	%{_urlprefix}/kdegraphics-%{version}.tar.bz2
# Source9-md5:	92ccbd703885a1f7788e4f27f281a75c
Source10:	%{_urlprefix}/kdelibs-%{version}.tar.bz2
# Source10-md5:	c60ab0b2efca14ed8913ac702de94666
Source11:	%{_urlprefix}/kdemultimedia-%{version}.tar.bz2
# Source11-md5:	ebdf9ccc9eae935eda5f78d56773ee9a
Source12:	%{_urlprefix}/kdenetwork-%{version}.tar.bz2
# Source12-md5:	72193b5eb050ef45fad76422a15e0e1a
Source13:	%{_urlprefix}/kdepim-%{version}.tar.bz2
# Source13-md5:	964208d570845c75e0c482bb3d33892f
Source14:	%{_urlprefix}/kdepimlibs-%{version}.tar.bz2
# Source14-md5:	62562a3025138a08ffdf08e6466b5065
Source15:	%{_urlprefix}/kdeplasma-addons-%{version}.tar.bz2
# Source15-md5:	809887da8ee9f7674761e0f46fa966a2
Source16:	%{_urlprefix}/kdesdk-%{version}.tar.bz2
# Source16-md5:	018767d862229899f4a648a6c36fd0f6
Source17:	%{_urlprefix}/kdetoys-%{version}.tar.bz2
# Source17-md5:	dcc17b3d719c7ddb48f75b64f34af261
Source18:	%{_urlprefix}/kdeutils-%{version}.tar.bz2
# Source18-md5:	3df5186f9dacddbce48a1c7eb35515cd
Source19:	%{_urlprefix}/kdewebdev-%{version}.tar.bz2
# Source19-md5:	82e057a10a6c840949aee3e98d8e2261
Source20:	%{_urlprefix}/oxygen-icons-%{version}.tar.bz2
# Source20-md5:	584cff3a47ac7eda4bec61ae5f6417aa
%if %{with l10n}
Source21:	%{_urlprefix}/kde-l10n/kde-l10n-bg-%{version}.tar.bz2
# Source21-md5:	d6f9cc4fce05427c23e05ad7a6e501f8
Source22:	%{_urlprefix}/kde-l10n/kde-l10n-ca-%{version}.tar.bz2
# Source22-md5:	f860f8c0eb81764bf48d27fa253d1abd
Source23:	%{_urlprefix}/kde-l10n/kde-l10n-cs-%{version}.tar.bz2
# Source23-md5:	c8aa7eab14d89466bf3738e70e255d87
Source24:	%{_urlprefix}/kde-l10n/kde-l10n-csb-%{version}.tar.bz2
# Source24-md5:	70145686a60f2db1ab66d0fe3a395e59
Source25:	%{_urlprefix}/kde-l10n/kde-l10n-da-%{version}.tar.bz2
# Source25-md5:	2db197e069695fe6ddaa709e2e646878
Source26:	%{_urlprefix}/kde-l10n/kde-l10n-de-%{version}.tar.bz2
# Source26-md5:	4a669b86c523cb78a45bbf3e1d03507d
Source27:	%{_urlprefix}/kde-l10n/kde-l10n-el-%{version}.tar.bz2
# Source27-md5:	1dd033fc59ce3874d6cd30244a715253
Source28:	%{_urlprefix}/kde-l10n/kde-l10n-en_GB-%{version}.tar.bz2
# Source28-md5:	bec69c9899683a35b40fea7dc65cc920
Source29:	%{_urlprefix}/kde-l10n/kde-l10n-es-%{version}.tar.bz2
# Source29-md5:	37c561521e1d89389a0f1d5df39cc1b3
Source30:	%{_urlprefix}/kde-l10n/kde-l10n-et-%{version}.tar.bz2
# Source30-md5:	c536c5f67a5cff82dc097c01f081e16d
Source31:	%{_urlprefix}/kde-l10n/kde-l10n-fi-%{version}.tar.bz2
# Source31-md5:	4c11d695a375f5fe830d92e80a19a8bf
Source32:	%{_urlprefix}/kde-l10n/kde-l10n-fr-%{version}.tar.bz2
# Source32-md5:	d0fbc486e241dd0a1ad650c044c82656
#Source33:	%{_urlprefix}/kde-l10n/kde-l10n-fy-%{version}.tar.bz2
# Source33-md5:	e5046259747f18c9d017f3606eda444c
Source34:	%{_urlprefix}/kde-l10n/kde-l10n-ga-%{version}.tar.bz2
# Source34-md5:	d9f5a315259812b48ca86cc3818d5825
Source35:	%{_urlprefix}/kde-l10n/kde-l10n-gl-%{version}.tar.bz2
# Source35-md5:	b268bdfa5b8f603cdbe0a557aaedb1bc
Source36:	%{_urlprefix}/kde-l10n/kde-l10n-hi-%{version}.tar.bz2
# Source36-md5:	f43d0563b66a16a73bb3f2f5f95362bf
Source37:	%{_urlprefix}/kde-l10n/kde-l10n-hu-%{version}.tar.bz2
# Source37-md5:	4f58a17ed248c57ea55dbceeacf359e2
Source38:	%{_urlprefix}/kde-l10n/kde-l10n-it-%{version}.tar.bz2
# Source38-md5:	c54364f89abb34d2469bc4cf4da6f840
Source39:	%{_urlprefix}/kde-l10n/kde-l10n-ja-%{version}.tar.bz2
# Source39-md5:	a8022ab1be8c8e143167828cdbcf0e1e
Source40:	%{_urlprefix}/kde-l10n/kde-l10n-kk-%{version}.tar.bz2
# Source40-md5:	d441ed4bed5e3dca6e8498f762f042c2
Source41:	%{_urlprefix}/kde-l10n/kde-l10n-km-%{version}.tar.bz2
# Source41-md5:	1443dad476a3df65222030000262001a
Source42:	%{_urlprefix}/kde-l10n/kde-l10n-ko-%{version}.tar.bz2
# Source42-md5:	2680181faf79a7c893a1a1240a2adf4d
Source43:	%{_urlprefix}/kde-l10n/kde-l10n-ku-%{version}.tar.bz2
# Source43-md5:	58e0a1ed8627c5b841b44994665ae5dc
Source44:	%{_urlprefix}/kde-l10n/kde-l10n-lt-%{version}.tar.bz2
# Source44-md5:	c7b90195d2cd4be2a723e8c0e9089166
Source45:	%{_urlprefix}/kde-l10n/kde-l10n-lv-%{version}.tar.bz2
# Source45-md5:	028be5e0d058ab8759792e3da7d0daa9
Source46:	%{_urlprefix}/kde-l10n/kde-l10n-mk-%{version}.tar.bz2
# Source46-md5:	7cdd7d4e33bb782a541f1d004f444e24
Source47:	%{_urlprefix}/kde-l10n/kde-l10n-ml-%{version}.tar.bz2
# Source47-md5:	0f6ea12f6db2cace8491a7a2c4879b3b
Source48:	%{_urlprefix}/kde-l10n/kde-l10n-nb-%{version}.tar.bz2
# Source48-md5:	7d8fec243c5b76a29807413d372e0356
Source49:	%{_urlprefix}/kde-l10n/kde-l10n-nds-%{version}.tar.bz2
# Source49-md5:	346172f49029f9aa621bd8fa4e401083
Source50:	%{_urlprefix}/kde-l10n/kde-l10n-nl-%{version}.tar.bz2
# Source50-md5:	bb7f95e030ee6b0b13ab12489ce5f963
Source51:	%{_urlprefix}/kde-l10n/kde-l10n-nn-%{version}.tar.bz2
# Source51-md5:	5ada2c1895846e9c9985a8ea4f34f0e5
Source52:	%{_urlprefix}/kde-l10n/kde-l10n-pa-%{version}.tar.bz2
# Source52-md5:	b019a54c931b1dcae659976f56d236c5
Source53:	%{_urlprefix}/kde-l10n/kde-l10n-pl-%{version}.tar.bz2
# Source53-md5:	118f22de9b47b1ac326d849175ddd6f5
Source54:	%{_urlprefix}/kde-l10n/kde-l10n-pt-%{version}.tar.bz2
# Source54-md5:	394964f96e21d087dfdf52989a2ec2fe
Source55:	%{_urlprefix}/kde-l10n/kde-l10n-pt_BR-%{version}.tar.bz2
# Source55-md5:	b3ab2486a8079791682b17c3caa89ed1
Source56:	%{_urlprefix}/kde-l10n/kde-l10n-ru-%{version}.tar.bz2
# Source56-md5:	45b2679ac7c1554ec02816a2c509dea0
Source57:	%{_urlprefix}/kde-l10n/kde-l10n-sl-%{version}.tar.bz2
# Source57-md5:	3d8b43de7bd364364f01648a3bc9cf95
Source58:	%{_urlprefix}/kde-l10n/kde-l10n-sr-%{version}.tar.bz2
# Source58-md5:	166976c4a4129fa361f7643e57bcebce
Source59:	%{_urlprefix}/kde-l10n/kde-l10n-sv-%{version}.tar.bz2
# Source59-md5:	d993387a13813af942154cc1d10a3ce5
#Source60:	%{_urlprefix}/kde-l10n/kde-l10n-ta-%{version}.tar.bz2
# Source60-md5:	586ccb6fa1f2ef63aa1823c57201feb1
Source61:	%{_urlprefix}/kde-l10n/kde-l10n-th-%{version}.tar.bz2
# Source61-md5:	bf04317460335654aa0482ad0000b58f
Source62:	%{_urlprefix}/kde-l10n/kde-l10n-tr-%{version}.tar.bz2
# Source62-md5:	04c3780701be20682bd772159ec78f1f
Source63:	%{_urlprefix}/kde-l10n/kde-l10n-uk-%{version}.tar.bz2
# Source63-md5:	3863787f2e4721b1568db2a9736454e7
Source64:	%{_urlprefix}/kde-l10n/kde-l10n-wa-%{version}.tar.bz2
# Source64-md5:	c2a082a4049fe340d108d1145d53451c
Source65:	%{_urlprefix}/kde-l10n/kde-l10n-zh_CN-%{version}.tar.bz2
# Source65-md5:	34de085cac6f862b359d1ce3e9ccfeed
Source66:	%{_urlprefix}/kde-l10n/kde-l10n-zh_TW-%{version}.tar.bz2
# Source66-md5:	f0c15cd1f14783f7d895355fe5754f61
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
