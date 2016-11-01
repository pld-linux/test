#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	-
Summary(pl.UTF-8):	-
Name:		template
Version:	_
Release:	0.1
License:	- (enter GPL/GPL v2/GPL v3/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
# SF URL: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# github URL https://github.com/USER/PROJECT/archive/v%{version}/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	-
#Source1:	-
# Source1-md5:	-
#Patch0:		%{name}-DESTDIR.patch
URL:		-
%if %{with initscript}
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
%endif
%if %{with systemd_service}
BuildRequires:	rpmbuild(macros) >= 1.647
Requires(post,preun,postun):	systemd-units >= 38
Requires:	systemd-units >= 0.38
%endif
#BuildRequires:	-
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	intltool
#BuildRequires:	libtool
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires:	-
#Provides:	-
#Provides:	group(foo)
#Provides:	user(foo)
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
#ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%package subpackage
Summary:	-
Summary(pl.UTF-8):	-
Group:		-
# noarch subpackages only when building with rpm5
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description subpackage

%description subpackage -l pl.UTF-8

%package libs
Summary:	-
Summary(pl.UTF-8):	-
Group:		Libraries

%description libs

%description libs -l pl.UTF-8

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
# if base package contains shared library for which these headers are
#Requires:	%{name} = %{version}-%{release}
# if -libs package contains shared library for which these headers are
#Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka %{name}.

%prep
%setup -q
#%setup -q -c -T
#%setup -q -n %{name}
#%setup -q -n %{name}-%{version}.orig -a 1
#%patch0 -p1

# undos the source
#find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'

# remove CVS control files
#find -name CVS -print0 | xargs -0 rm -rf

# you'll need this if you cp -a complete dir in source
# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%{__intltoolize}
#%{__gettextize}
#%{__libtoolize}
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#%{__automake}
# if not running libtool or automake, but config.sub is too old:
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
%if %{with initscript}
install -d $RPM_BUILD_ROOT/etc/{sysconfig,rc.d/init.d}
%endif
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g xxx %{name}
%useradd -u xxx -d /var/lib/%{name} -g %{name} -c "XXX User" %{name}

%post

%preun

%postun
if [ "$1" = "0" ]; then
	%userremove %{name}
	%groupremove %{name}
fi

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%if %{with initscript}
%post
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi
%endif

%if %{with systemd_service}
%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_reload
%endif

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS CHANGES ChangeLog NEWS README THANKS TODO

%if 0
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/%{name}
%endif

# initscript and its config
%if %{with initscript}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%endif

%if %{with systemd_service}
%{systemdunitdir}/%{name}.service
%endif

#%{_examplesdir}/%{name}-%{version}

%if %{with subpackage}
%files subpackage
%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
%endif
