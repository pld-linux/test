# Module for kernels <2.6.24
#
# Conditional build:
%bcond_without	dist_kernel	# allow non-distribution kernel
%bcond_without	kernel		# don't build kernel modules
%bcond_with	verbose		# verbose build (V=1)

%if %{without kernel}
%undefine with_dist_kernel
%endif

%if "%{_alt_kernel}" != "%{nil}"
%if 0%{?build_kernels:1}
%{error:alt_kernel and build_kernels are mutually exclusive}
exit 1
%endif
%undefine	with_userspace
%global		_build_kernels		%{alt_kernel}
%else
%global		_build_kernels		%{?build_kernels:,%{?build_kernels}}
%endif

%define		kpkg	%(echo %{_build_kernels} | tr , '\\n' | while read n ; do echo %%undefine alt_kernel ; [ -z "$n" ] || echo %%define alt_kernel $n ; echo %%kernel_pkg ; done)
%define		bkpkg	%(echo %{_build_kernels} | tr , '\\n' | while read n ; do echo %%undefine alt_kernel ; [ -z "$n" ] || echo %%define alt_kernel $n ; echo %%build_kernel_pkg ; done)
%define		ikpkg	%(echo %{_build_kernels} | tr , '\\n' | while read n ; do echo %%undefine alt_kernel ; [ -z "$n" ] || echo %%define alt_kernel $n ; echo %%install_kernel_pkg ; done)

%define		rel	0.1
%define		pname	e1000e

%define	kernel_pkg()\
%package -n kernel%{_alt_kernel}-net-%{pname}\
Summary:	Intel(R) PRO/1000e driver for Linux %{_kernelsrcdir}:%{__kernel_rpmvr}\
Summary(pl.UTF-8):	Sterownik do karty Intel® PRO/1000e\
Release:	%{rel}@%{_kernel_ver_str}\
Group:		Base/Kernel\
Requires(post,postun):	/sbin/depmod\
%if %{with dist_kernel}\
%requires_releq_kernel\
Requires(postun):	%releq_kernel\
%endif\
\
%description -n kernel%{_alt_kernel}-net-%{pname}\
This package contains the Linux driver for the Intel(R) PRO/1000\
family of 10/100/1000 Ethernet network adapters. This driver is\
designed to work with the Intel(R) 82571/2/3/4 PCI-E family of gigabit\
adapters and 82567 controllers.\
\
%description -n kernel%{_alt_kernel}-net-%{pname} -l pl.UTF-8\
Ten pakiet zawiera sterownik dla Linuksa do kart sieciowych\
10/100/1000Mbit z rodziny Intel® PRO/1000. Ten sterownik jest\
stworzony aby pracować z kartami gigabitowymi rodziny Intel®\
82571/2/3/4 PCI-E oraz kontrolerami 82567.\
\
%if %{with kernel}\
%files -n kernel%{_alt_kernel}-net-%{pname}\
%defattr(755,root,root,755)\
%doc e1000e.7 README\
/etc/modprobe.d/%{_kernel_ver}/%{pname}.conf\
/lib/modules/%{_kernel_ver}/kernel/drivers/net/%{pname}*.ko*\
%endif\
%{nil}

%define build_kernel_pkg()\
%build_kernel_modules -C src -m %{pname}\
%install_kernel_modules -D installed -m src/%{pname} -d kernel/drivers/net -n %{pname} -s current\
%{nil}

%define install_kernel_pkg()\
install -d $RPM_BUILD_ROOT/etc/modprobe.d/%{_kernel_ver}\
# blacklist kernel module\
cat > $RPM_BUILD_ROOT/etc/modprobe.d/%{_kernel_ver}/%{pname}.conf <<'EOF'\
blacklist e1000e\
alias e1000e e1000e-current\
EOF\
%{nil}

Summary:	testing something
Name:		%{pname}%{_alt_kernel}
Version:	2.4.14
Release:	%{rel}%{?with_kernel:@%{_kernel_ver_str}}
License:	GPL v2
Group:		Base/Kernel
Source0:	http://downloads.sourceforge.net/e1000/%{pname}-%{version}.tar.gz
# Source0-md5:	05bae01409bb699f14297d726df2aa23
URL:		http://www.pld-linux.org/
BuildRequires:	rpm-build-macros >= 1.677
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.20.2}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testing something

%{?with_kernel:%{expand:%kpkg}}

%prep
%setup -q -n %{pname}-%{version}

cat > src/Makefile <<'EOF'
obj-m := e1000e.o
e1000e-objs := netdev.o ethtool.o param.o \
82571.o ich8lan.o 80003es2lan.o \
mac.o nvm.o phy.o manage.o kcompat.o

EXTRA_CFLAGS=-DDRIVER_E1000E -DCONFIG_E1000E_SEPARATE_TX_HANDLER
EOF
# add -DE1000E_NO_NAPI to disable NAPI

%build
%{?with_kernel:%{expand:%bkpkg}}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%if %{with kernel}
%{expand:%ikpkg}
cp -a installed/* $RPM_BUILD_ROOT
%endif

%clean

%files
%defattr(644,root,root,755)
