%include	/usr/lib/rpm/macros.perl
Summary:	fake xorg provider
Name:		fake-xorg
Version:	0.8.56
Release:	0.3
License:	GPL
Group:		Applications/System
Requires:	XFree86-Xvfb
Requires:	XFree86-devel
Provides:	xorg-lib-libX11-devel
Provides:	xorg-lib-libXext-devel
Provides:	xorg-lib-libXft-devel = 2.1
Provides:	xorg-lib-libXi-devel
Provides:	xorg-lib-libXinerama-devel
Provides:	xorg-lib-libXmu-devel
Provides:	xorg-lib-libXp-devel
Provides:	xorg-lib-libXt-devel
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
