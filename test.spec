%include	/usr/lib/rpm/macros.perl
Summary:	fake xorg provider
Name:		fake-xorg
Version:	7.0
Release:	0.2
License:	GPL
Group:		Applications/System
Requires:	X11
Requires:	X11-fonts-base
Requires:	X11-imake
Requires:	X11-libs
Requires:	XFree86-Xvfb
Requires:	XFree86-devel
Provides:	xorg-app-bdftopcf
Provides:	xorg-app-iceauth
Provides:	xorg-cf-files
Provides:	xorg-font-font-cursor-misc
Provides:	xorg-font-font-misc-misc-base
Provides:	xorg-lib-libSM-devel
Provides:	xorg-lib-libX11-devel
Provides:	xorg-lib-libXScrnSaver-devel
Provides:	xorg-lib-libXaw-devel
Provides:	xorg-lib-libXcomposite-devel
Provides:	xorg-lib-libXcursor-devel
Provides:	xorg-lib-libXcursor-devel
Provides:	xorg-lib-libXdamage-devel
Provides:	xorg-lib-libXext-devel
Provides:	xorg-lib-libXfixes-devel
Provides:	xorg-lib-libXft-devel = 2.1
Provides:	xorg-lib-libXi-devel
Provides:	xorg-lib-libXinerama-devel
Provides:	xorg-lib-libXmu-devel
Provides:	xorg-lib-libXp-devel
Provides:	xorg-lib-libXpm-devel
Provides:	xorg-lib-libXrandr-devel
Provides:	xorg-lib-libXrender-devel
Provides:	xorg-lib-libXt-devel
Provides:	xorg-lib-libXtst-devel
Provides:	xorg-lib-libXv-devel
Provides:	xorg-lib-libXvMC-devel
Provides:	xorg-lib-libXxf86dga-devel
Provides:	xorg-lib-libXxf86vm-devel
Provides:	xorg-lib-libfontenc-devel
Provides:	xorg-lib-libxkbfile-devel
Provides:	xorg-proto-scrnsaverproto-devel
Provides:	xorg-proto-xextproto-devel
Provides:	xorg-util-imake
Provides:	xorg-util-util-macros
Provides:	xorg-xserver-Xvfb
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fake package providing xorg deps for building xorg dependant packages
on ac without caring about exact xfree deps.

%prep
%setup -qcT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
