# - easy way to update all sources with new/old locales:
#   lynx -dump http://carme.pld-linux.org/~arekm/kde/kde-l10n | awk -vi=19 '/4.1.0.tar.xz$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   sed -i -e 's,http://carme.pld-linux.org/~arekm/kde/kde-l10n/,%{_urlprefix}/kde-l10n/kde-l10n/,' out
#   sed -i -e 's,4.1.0,%{version},' out
#   and then :r out in vim and ./builder -a5 the spec
%bcond_with	l10n
%bcond_with	koffice
%define		_urlprefix	http://ixion.pld-linux.org/~arekm/kde/
#%%define		_urlprefix	http://shadzik.nomeno.pl/kde4/
%define		kofficever	2.3.1
#%%define		_urlprefix	ftp://ftp.pbone.net/mirror/ftp.kde.org/pub/kde/unstable/%{version}/src
Summary:	Fetch KDE packages to distfiles
Name:		kdefetch
Version:	4.8.2
Release:	1
License:	GPL
Group:		Networking/Hacking
Source100:	kde4diff.sh
# Source100-md5:	e335c913f721664dc383542367cdcbf2
Source0:	%{_urlprefix}/analitza-%{version}.tar.xz
# Source0-md5:	958ba4437ebd99cad2ea34638766d84e
Source1:	%{_urlprefix}/ark-%{version}.tar.xz
# Source1-md5:	02f303761c006cb76788e61f1c7d265d
Source2:	%{_urlprefix}/blinken-%{version}.tar.xz
# Source2-md5:	a337504a3ef0aa6b61732d9e842e5c6b
Source3:	%{_urlprefix}/cantor-%{version}.tar.xz
# Source3-md5:	952688ad96bfbd9b7fa8dd3dc36f3480
Source4:	%{_urlprefix}/filelight-%{version}.tar.xz
# Source4-md5:	eba36d5930fc44f51a8a17c44af5ccfd
Source5:	%{_urlprefix}/gwenview-%{version}.tar.xz
# Source5-md5:	c6e6b596a4e501edb744ded1b0dd2969
Source6:	%{_urlprefix}/jovie-%{version}.tar.xz
# Source6-md5:	6baf12c46947605121b2593972b32e26
Source7:	%{_urlprefix}/kaccessible-%{version}.tar.xz
# Source7-md5:	61cc8da2ffdd45e9e92ffbe5179fb88f
Source8:	%{_urlprefix}/kactivities-%{version}.tar.xz
# Source8-md5:	be75237315c5b30ad89020e4fcc8b03c
Source9:	%{_urlprefix}/kalgebra-%{version}.tar.xz
# Source9-md5:	3167f5cd027817a01b5979dfd08aabda
Source10:	%{_urlprefix}/kalzium-%{version}.tar.xz
# Source10-md5:	fc5aac0104f2536a8a77cd8b3b93043a
Source11:	%{_urlprefix}/kamera-%{version}.tar.xz
# Source11-md5:	6a79007a55224fbfde27f7b0232b7da6
Source12:	%{_urlprefix}/kanagram-%{version}.tar.xz
# Source12-md5:	e84c3457972fcb0ce691996a5cba3235
Source13:	%{_urlprefix}/kate-%{version}.tar.xz
# Source13-md5:	3ba1635dfd76593d0b4b2f7c4b29543c
Source14:	%{_urlprefix}/kbruch-%{version}.tar.xz
# Source14-md5:	961e79c6c7b90f503d3929557267bad1
Source15:	%{_urlprefix}/kcalc-%{version}.tar.xz
# Source15-md5:	853d812ce36d6845af7e9720d51e2b0a
Source16:	%{_urlprefix}/kcharselect-%{version}.tar.xz
# Source16-md5:	837c4c9abfa5c0b400cae8a700838f3b
Source17:	%{_urlprefix}/kcolorchooser-%{version}.tar.xz
# Source17-md5:	e866dc17081f8bada98681bc0e252ca5
Source18:	%{_urlprefix}/kde-baseapps-%{version}.tar.xz
# Source18-md5:	561cf69f77973262dcda3ca7e79af5ce
Source19:	%{_urlprefix}/kde-l10n
# Source19-md5:	40ff7f8eb50b837f871140280f3f5634
Source20:	%{_urlprefix}/kde-runtime-%{version}.tar.xz
# Source20-md5:	d954bf534c796f15088d78c03b955754
Source21:	%{_urlprefix}/kde-wallpapers-%{version}.tar.xz
# Source21-md5:	9e3dcf2d0f593795f6b7ee09b4fb1595
Source22:	%{_urlprefix}/kde-workspace-%{version}.tar.xz
# Source22-md5:	a725122bc968cce959fd2dfe3ef552ff
Source23:	%{_urlprefix}/kdeadmin-%{version}.tar.xz
# Source23-md5:	8f68d983f0028fe2c5e4566f5adada44
Source24:	%{_urlprefix}/kdeartwork-%{version}.tar.xz
# Source24-md5:	9e1e5133770f974dcc8ddb16cf95add6
Source25:	%{_urlprefix}/kdegames-%{version}.tar.xz
# Source25-md5:	bcc278edc7999bd33e8299f213ebd34d
Source26:	%{_urlprefix}/kdegraphics-mobipocket-%{version}.tar.xz
# Source26-md5:	6c36479b12d33134e249366c9913155f
Source27:	%{_urlprefix}/kdegraphics-strigi-analyzer-%{version}.tar.xz
# Source27-md5:	5861f8949ef44016df972c7796323039
Source28:	%{_urlprefix}/kdegraphics-thumbnailers-%{version}.tar.xz
# Source28-md5:	493671b6b298770025cd812f6443e3e2
Source29:	%{_urlprefix}/kdelibs-%{version}.tar.xz
# Source29-md5:	e9dc9a76a785045642fb3098692618d2
Source30:	%{_urlprefix}/kdemultimedia-%{version}.tar.xz
# Source30-md5:	1d95dadbe405d551ffe6458a4b266d1f
Source31:	%{_urlprefix}/kdenetwork-%{version}.tar.xz
# Source31-md5:	2fa12b6d7c2ca4b959ebd64398970503
Source32:	%{_urlprefix}/kdepim-%{version}.tar.xz
# Source32-md5:	95784f2f3c67889205c6537255c3f9b5
Source33:	%{_urlprefix}/kdepim-runtime-%{version}.tar.xz
# Source33-md5:	ac3b7c787813ff0d1b47b6ec9d888773
Source34:	%{_urlprefix}/kdepimlibs-%{version}.tar.xz
# Source34-md5:	ec4a0c4aae5aadf3be024254fe733139
Source35:	%{_urlprefix}/kdeplasma-addons-%{version}.tar.xz
# Source35-md5:	baafb502d214c1a4869f5cf2487e7e59
Source36:	%{_urlprefix}/kdesdk-%{version}.tar.xz
# Source36-md5:	a47a7a28ba48e5553bdb610c548a32dd
Source37:	%{_urlprefix}/kdetoys-%{version}.tar.xz
# Source37-md5:	5a51eb19db0fc195d782459a86544496
Source38:	%{_urlprefix}/kdewebdev-%{version}.tar.xz
# Source38-md5:	d39dd6ab7b90cff85215d62891c6f56b
Source39:	%{_urlprefix}/kdf-%{version}.tar.xz
# Source39-md5:	79a172615d6c06a7bcab0452d0497e0e
Source40:	%{_urlprefix}/kfloppy-%{version}.tar.xz
# Source40-md5:	7d8b58bdab103f83a36075c69a227f0f
Source41:	%{_urlprefix}/kgamma-%{version}.tar.xz
# Source41-md5:	297b8f7b17eee60648a98b04800eaf83
Source42:	%{_urlprefix}/kgeography-%{version}.tar.xz
# Source42-md5:	2b74ad3ee4d9655a7c8a751088f401d0
Source43:	%{_urlprefix}/kgpg-%{version}.tar.xz
# Source43-md5:	8da268005c9251234493291c232ac6f7
Source44:	%{_urlprefix}/khangman-%{version}.tar.xz
# Source44-md5:	0f19eb9b2cc15896eae3cf4b75698a61
Source45:	%{_urlprefix}/kig-%{version}.tar.xz
# Source45-md5:	8bdcd06de7f9aa176d8df477bb090bba
Source46:	%{_urlprefix}/kimono-%{version}.tar.xz
# Source46-md5:	b2460c571a30902ed359055ed73c7990
Source47:	%{_urlprefix}/kiten-%{version}.tar.xz
# Source47-md5:	5b7f66317c1a6ebc470067d502f01621
Source48:	%{_urlprefix}/klettres-%{version}.tar.xz
# Source48-md5:	62564ece1ad344a6a6c8e24d7883c046
Source49:	%{_urlprefix}/kmag-%{version}.tar.xz
# Source49-md5:	f83442152d51b6e93853f22db74a1c9d
Source50:	%{_urlprefix}/kmousetool-%{version}.tar.xz
# Source50-md5:	03796e4b0cc69ca4f4f8e3fdb4b6d37b
Source51:	%{_urlprefix}/kmouth-%{version}.tar.xz
# Source51-md5:	b5798a7f4098f4c2cf97b42b64abcfb0
Source52:	%{_urlprefix}/kmplot-%{version}.tar.xz
# Source52-md5:	35021c525f4556019535e881b07bc504
Source53:	%{_urlprefix}/kolourpaint-%{version}.tar.xz
# Source53-md5:	5b3642128da6afe5d7e06da8b5163b1b
Source54:	%{_urlprefix}/konsole-%{version}.tar.xz
# Source54-md5:	c63b525e94a0e7e1753ea3d9dbff6970
Source55:	%{_urlprefix}/korundum-%{version}.tar.xz
# Source55-md5:	66345740580f485d6956e926f17ef673
Source56:	%{_urlprefix}/kremotecontrol-%{version}.tar.xz
# Source56-md5:	601533b8a0b27b817a7bcac9f956408a
Source57:	%{_urlprefix}/kross-interpreters-%{version}.tar.xz
# Source57-md5:	d43b733d2fc76bafee4689687dbef188
Source58:	%{_urlprefix}/kruler-%{version}.tar.xz
# Source58-md5:	fb012d343198549b7e079fdcfa072eec
Source59:	%{_urlprefix}/ksaneplugin-%{version}.tar.xz
# Source59-md5:	52d95e9afc3f1bff411bec4f4a61c956
Source60:	%{_urlprefix}/ksecrets-%{version}.tar.xz
# Source60-md5:	6a6152aa4f6663a0f8ec8954f3650e0e
Source61:	%{_urlprefix}/ksnapshot-%{version}.tar.xz
# Source61-md5:	fbd406dfbd67849464455f6a5aa46316
Source62:	%{_urlprefix}/kstars-%{version}.tar.xz
# Source62-md5:	a262b3f33c1f8934729c120406b31fdb
Source63:	%{_urlprefix}/ktimer-%{version}.tar.xz
# Source63-md5:	c731e7bc3fa47d503a2c4d183155ecba
Source64:	%{_urlprefix}/ktouch-%{version}.tar.xz
# Source64-md5:	a58566635ae6805b39728622bf15bb3b
Source65:	%{_urlprefix}/kturtle-%{version}.tar.xz
# Source65-md5:	2dcfceeecd6e2d3c543daeeb4f9693ec
Source66:	%{_urlprefix}/kwallet-%{version}.tar.xz
# Source66-md5:	59501670e400320594b9d23f1658f28c
Source67:	%{_urlprefix}/kwordquiz-%{version}.tar.xz
# Source67-md5:	361342e06522041362796b0687ef5905
Source68:	%{_urlprefix}/libkdcraw-%{version}.tar.xz
# Source68-md5:	8ba6ef179a0948e84cbf22af3f5a1bae
Source69:	%{_urlprefix}/libkdeedu-%{version}.tar.xz
# Source69-md5:	676cf15837c1c9b42b7d2e8f614d6883
Source70:	%{_urlprefix}/libkexiv2-%{version}.tar.xz
# Source70-md5:	d929565d18d7be60239a2f2f9df7613e
Source71:	%{_urlprefix}/libkipi-%{version}.tar.xz
# Source71-md5:	826621c3d0f5230f48ec84f5a4ca9a5d
Source72:	%{_urlprefix}/libksane-%{version}.tar.xz
# Source72-md5:	4053c4a050868dbce4673bc19b75157b
Source73:	%{_urlprefix}/marble-%{version}.tar.xz
# Source73-md5:	9048b46cf0be1959b3a82bcae9fbe010
Source74:	%{_urlprefix}/okular-%{version}.tar.xz
# Source74-md5:	9c297fabcb8130f617dc5718a20f89cb
Source75:	%{_urlprefix}/oxygen-icons-%{version}.tar.xz
# Source75-md5:	04d27cec77197f6f0a0472f6e751f20e
Source76:	%{_urlprefix}/parley-%{version}.tar.xz
# Source76-md5:	df74618312a796257373e978811f400f
Source77:	%{_urlprefix}/perlkde-%{version}.tar.xz
# Source77-md5:	d029f15aa3c3ccb2e53f2e8bbe4786a6
Source78:	%{_urlprefix}/perlqt-%{version}.tar.xz
# Source78-md5:	c1c2b46e9614670065144e12525e44e2
Source79:	%{_urlprefix}/printer-applet-%{version}.tar.xz
# Source79-md5:	20ddad2ae53143cff877df4482f38f7a
Source80:	%{_urlprefix}/pykde4-%{version}.tar.xz
# Source80-md5:	f48d3b2b4f75e652c27a5ccda7dedc90
Source81:	%{_urlprefix}/qtruby-%{version}.tar.xz
# Source81-md5:	c9634bdb68a87d7f473704e0041702d1
Source82:	%{_urlprefix}/qyoto-%{version}.tar.xz
# Source82-md5:	381bb2dd8170cad77214def6ae46cf15
Source83:	%{_urlprefix}/rocs-%{version}.tar.xz
# Source83-md5:	ebf52f349f31ab6768686af4150b269d
Source84:	%{_urlprefix}/smokegen-%{version}.tar.xz
# Source84-md5:	cd15f9a8d8ed871a31dd907de1950c9a
Source85:	%{_urlprefix}/smokekde-%{version}.tar.xz
# Source85-md5:	f76e50f2379d2ba8afb6bda90d69c04f
Source86:	%{_urlprefix}/smokeqt-%{version}.tar.xz
# Source86-md5:	1a6956ca84c83aff7931d51a0956c109
Source87:	%{_urlprefix}/step-%{version}.tar.xz
# Source87-md5:	f7e58639dd86b6c134f1689eaf8396fe
Source88:	%{_urlprefix}/superkaramba-%{version}.tar.xz
# Source88-md5:	9133d228b18f261de3206358b923a684
Source89:	%{_urlprefix}/svgpart-%{version}.tar.xz
# Source89-md5:	1c44b0fc9fc75df18aab9e951c929271
Source90:	%{_urlprefix}/sweeper-%{version}.tar.xz
# Source90-md5:	062cd5c187b50c90817a0087e11d9ae4
%if %{with l10n}
Source101: %{_urlprefix}/kde-l10n/kde-l10n-ar-%{version}.tar.xz
# Source101-md5:	29f33aaf81241771560a03c4f9f94153
Source102: %{_urlprefix}/kde-l10n/kde-l10n-bg-%{version}.tar.xz
# Source102-md5:	f1901bf01ef965caf2d6f79f02de3eae
Source103: %{_urlprefix}/kde-l10n/kde-l10n-bs-%{version}.tar.xz
# Source103-md5:	138ee322fbecb53db7bf434a82f216a2
Source104: %{_urlprefix}/kde-l10n/kde-l10n-ca-%{version}.tar.xz
# Source104-md5:	f1a7b42524dcc6ac334378ec69370094
Source105: %{_urlprefix}/kde-l10n/kde-l10n-ca@valencia-%{version}.tar.xz
# Source105-md5:	0bb404597925159a4b1a896bba8e8e2d
Source106: %{_urlprefix}/kde-l10n/kde-l10n-cs-%{version}.tar.xz
# Source106-md5:	52db534259b9ec9bf449722dcc9c26b8
Source107: %{_urlprefix}/kde-l10n/kde-l10n-da-%{version}.tar.xz
# Source107-md5:	fb4fd304a9881792367afd9ee986604c
Source108: %{_urlprefix}/kde-l10n/kde-l10n-de-%{version}.tar.xz
# Source108-md5:	73b213a802feec528503bad8d9316be2
Source109: %{_urlprefix}/kde-l10n/kde-l10n-el-%{version}.tar.xz
# Source109-md5:	ed29f1ca2ab9fc46da43647ed2e05305
Source110: %{_urlprefix}/kde-l10n/kde-l10n-en_GB-%{version}.tar.xz
# Source110-md5:	bb90d978eed77bec3a49e1d8dbeb3f37
Source111: %{_urlprefix}/kde-l10n/kde-l10n-es-%{version}.tar.xz
# Source111-md5:	3fc8742cbc8754e559c8c8a232cb9b5e
Source112: %{_urlprefix}/kde-l10n/kde-l10n-et-%{version}.tar.xz
# Source112-md5:	54407fb246495cf73d4fcc782bbf5bb2
Source113: %{_urlprefix}/kde-l10n/kde-l10n-eu-%{version}.tar.xz
# Source113-md5:	28bdd742bbdcd22873306eb6af60e536
Source114: %{_urlprefix}/kde-l10n/kde-l10n-fa-%{version}.tar.xz
# Source114-md5:	ece464c57cda6e70282ff8a19ca4ae1f
Source115: %{_urlprefix}/kde-l10n/kde-l10n-fi-%{version}.tar.xz
# Source115-md5:	04287a09b0be05023aee4075a4cf525c
Source116: %{_urlprefix}/kde-l10n/kde-l10n-fr-%{version}.tar.xz
# Source116-md5:	50a4abec138d586c07d562c1c6d796b6
Source117: %{_urlprefix}/kde-l10n/kde-l10n-ga-%{version}.tar.xz
# Source117-md5:	140877f608d44201182fc530bc941eea
Source118: %{_urlprefix}/kde-l10n/kde-l10n-gl-%{version}.tar.xz
# Source118-md5:	efae88b09cb3f1dd5085a01c1f36487f
Source119: %{_urlprefix}/kde-l10n/kde-l10n-hr-%{version}.tar.xz
# Source119-md5:	80f7eed191c1815709a183dcfb36e5f9
Source120: %{_urlprefix}/kde-l10n/kde-l10n-hu-%{version}.tar.xz
# Source120-md5:	2a284d7392654ea7ec7659ee64f26075
Source121: %{_urlprefix}/kde-l10n/kde-l10n-ia-%{version}.tar.xz
# Source121-md5:	0b8ef0edd985670b14cc79ac01aaecec
Source122: %{_urlprefix}/kde-l10n/kde-l10n-is-%{version}.tar.xz
# Source122-md5:	9e26509ca3b93192df338178889e5c33
Source123: %{_urlprefix}/kde-l10n/kde-l10n-it-%{version}.tar.xz
# Source123-md5:	7f03e6afcac2439813b89ac25a056669
Source124: %{_urlprefix}/kde-l10n/kde-l10n-ja-%{version}.tar.xz
# Source124-md5:	bfd8367ed52ffffee9bda6196cbbc154
Source125: %{_urlprefix}/kde-l10n/kde-l10n-kk-%{version}.tar.xz
# Source125-md5:	32c5c774e74ba20ebf664804cb7b2533
Source126: %{_urlprefix}/kde-l10n/kde-l10n-km-%{version}.tar.xz
# Source126-md5:	213ba5624f1ad9530dfbeced6136be4c
Source127: %{_urlprefix}/kde-l10n/kde-l10n-ko-%{version}.tar.xz
# Source127-md5:	24873964d55eee97670ee9532d1ea6bc
Source128: %{_urlprefix}/kde-l10n/kde-l10n-lt-%{version}.tar.xz
# Source128-md5:	39c86e292843f2ddd98861a54677e257
Source129: %{_urlprefix}/kde-l10n/kde-l10n-lv-%{version}.tar.xz
# Source129-md5:	e7d0c5248d5c22f9bd15e16d7304e5ff
Source130: %{_urlprefix}/kde-l10n/kde-l10n-nb-%{version}.tar.xz
# Source130-md5:	e8be311dd09969a41ca5ef9136a58bb9
Source131: %{_urlprefix}/kde-l10n/kde-l10n-nds-%{version}.tar.xz
# Source131-md5:	2f4e9e3a9344c97ed62c138b0299bd7e
Source132: %{_urlprefix}/kde-l10n/kde-l10n-nl-%{version}.tar.xz
# Source132-md5:	12c4531be3d2cece936490d997864a95
Source133: %{_urlprefix}/kde-l10n/kde-l10n-nn-%{version}.tar.xz
# Source133-md5:	689f2b5f062fb0b278809929f20a1c97
Source134: %{_urlprefix}/kde-l10n/kde-l10n-pa-%{version}.tar.xz
# Source134-md5:	3839b67f23225b172b72650d4ea42631
Source135: %{_urlprefix}/kde-l10n/kde-l10n-pl-%{version}.tar.xz
# Source135-md5:	6a57c52eca974460e8a21d6ac4a5cd92
Source136: %{_urlprefix}/kde-l10n/kde-l10n-pt-%{version}.tar.xz
# Source136-md5:	23f4e63b18f53259c9e06ffd5c47139e
Source137: %{_urlprefix}/kde-l10n/kde-l10n-pt_BR-%{version}.tar.xz
# Source137-md5:	c565ac0f0f3df05ad03b9df92f3ce464
Source138: %{_urlprefix}/kde-l10n/kde-l10n-ro-%{version}.tar.xz
# Source138-md5:	572043c7a277d1781eee52fce82702ef
Source139: %{_urlprefix}/kde-l10n/kde-l10n-ru-%{version}.tar.xz
# Source139-md5:	7924789dfd2b384f17d3ac3987644b01
Source140: %{_urlprefix}/kde-l10n/kde-l10n-si-%{version}.tar.xz
# Source140-md5:	4a8de7fceab09230ea546d3ce08387be
Source141: %{_urlprefix}/kde-l10n/kde-l10n-sk-%{version}.tar.xz
# Source141-md5:	b596f86205e32e0d61b38fa7bfce9ff2
Source142: %{_urlprefix}/kde-l10n/kde-l10n-sl-%{version}.tar.xz
# Source142-md5:	3bff2eb12fd34559e3fd39173c929212
Source143: %{_urlprefix}/kde-l10n/kde-l10n-sr-%{version}.tar.xz
# Source143-md5:	4761afb61efb6c79b809e64a2390a48f
Source144: %{_urlprefix}/kde-l10n/kde-l10n-sv-%{version}.tar.xz
# Source144-md5:	b484167eb5d3a53c0ba539abee71703e
Source145: %{_urlprefix}/kde-l10n/kde-l10n-tg-%{version}.tar.xz
# Source145-md5:	12fe3db75b444984b0f783b2b71023fe
Source146: %{_urlprefix}/kde-l10n/kde-l10n-th-%{version}.tar.xz
# Source146-md5:	a32f63d8cdfc1896b75f48996c69136c
Source147: %{_urlprefix}/kde-l10n/kde-l10n-tr-%{version}.tar.xz
# Source147-md5:	8dc4743d67580ab711476a1c781c53cb
Source148: %{_urlprefix}/kde-l10n/kde-l10n-uk-%{version}.tar.xz
# Source148-md5:	c8e56e7b964ced291e23364f4f227017
Source149: %{_urlprefix}/kde-l10n/kde-l10n-vi-%{version}.tar.xz
# Source149-md5:	d6315d5a6088344a297a6955b9918bc4
Source150: %{_urlprefix}/kde-l10n/kde-l10n-wa-%{version}.tar.xz
# Source150-md5:	922f83d26df8b44aafdadcb533d9b9bf
Source151: %{_urlprefix}/kde-l10n/kde-l10n-zh_CN-%{version}.tar.xz
# Source151-md5:	b3bea59a34bc603a871b4174436fc58c
Source152: %{_urlprefix}/kde-l10n/kde-l10n-zh_TW-%{version}.tar.xz
# Source152-md5:	f7b80c66072a8a4244636a5e4f73e189
%endif
%if %{with koffice}
Source68:	%{_urlprefix}/koffice-%{kofficever}/koffice-%{kofficever}.tar.bz2
# Source68-md5:	8ba6ef179a0948e84cbf22af3f5a1bae
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
