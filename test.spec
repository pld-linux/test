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
%define		_build_kernels		%{alt_kernel}
%else
%define		_build_kernels		%{?build_kernels:,%{?build_kernels}}
%endif

%define		kpkg	%(echo %{_build_kernels} | tr , '\\n' | while read n ; do echo %%undefine alt_kernel ; [ -z "$n" ] || echo %%define alt_kernel $n ; echo %%kernel_pkg ; done)
%define		bkpkg	%(echo %{_build_kernels} | tr , '\\n' | while read n ; do echo %%undefine alt_kernel ; [ -z "$n" ] || echo %%define alt_kernel $n ; echo %%build_kernel_pkg ; done)
%define		ikpkg	%(echo %{_build_kernels} | tr , '\\n' | while read n ; do echo %%undefine alt_kernel ; [ -z "$n" ] || echo %%define alt_kernel $n ; echo %%install_kernel_pkg ; done)

%define		rel	0.1
%define		pname	test

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
%files -n kernel%{_alt_kernel}-net-%{pname} -f kernel%{_alt_kernel}-net-%{pname}.list\
%defattr(755,root,root,755)\
%{nil}

%define build_kernel_pkg()\
echo %{_kernelsrcdir}\
touch kernel%{_alt_kernel}-net-%{pname}.list\
%{nil}

Summary:	testing something
Name:		%{pname}
Version:	1
Release:	%{rel}%{?with_kernel:@%{_kernel_ver_str}}
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
#BuildRequires:	rpm-build-macros >= 1.676
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testing something

%{?with_kernel:%{expand:%kpkg}}

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{?with_kernel:%{expand:%bkpkg}}

%clean

%files
%defattr(644,root,root,755)
