
%define		kpkg	%(echo %{ksa} | tr , '\\n' | while read n ; do echo %%pkg $n; done)

Summary:	testing something
Name:		test
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	kernel_pkg()\
%package -n kernel%{_alt_kernel}-net-%{pname} %1\
Summary:	Intel(R) PRO/1000e driver for Linux
Summary(pl.UTF-8):	Sterownik do karty Intel® PRO/1000e
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-net-%{pname}
This package contains the Linux driver for the Intel(R) PRO/1000
family of 10/100/1000 Ethernet network adapters. This driver is
designed to work with the Intel(R) 82571/2/3/4 PCI-E family of gigabit
adapters and 82567 controllers.

%description -n kernel%{_alt_kernel}-net-%{pname} -l pl.UTF-8
Ten pakiet zawiera sterownik dla Linuksa do kart sieciowych
10/100/1000Mbit z rodziny Intel® PRO/1000. Ten sterownik jest
stworzony aby pracować z kartami gigabitowymi rodziny Intel®
82571/2/3/4 PCI-E oraz kontrolerami 82567.

Summary:	Munin plugins from MuninExchange - %1\
Summary(pl.UTF-8):	Wtyczki munina z MuninExchange - %1\
Group:		Daemons\
Requires:	munin-node\
\
%description %1\
This package contains plugins for Munin from MuninExchange repository\
located at <https://github.com/munin-monitoring/contrib/>.\
\
%description %1 -l pl.UTF-8\
Ten pakiet zawera wtyczki dla Munina z repozytorium MuninExchange,\
znajdującym się na <https://github.com/munin-monitoring/contrib/>.\
\
%files %1 -f %1.list\
%defattr(755,root,root,755)\
%{nil}

%description
testing something

%{expand:%kpkg}

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

touch a.list b.list c.list

%define _alt_kernel    xxx
echo %{_kernelsrcdir}
%define _alt_kernel    zzz
echo %{_kernelsrcdir}

%clean

%files
%defattr(644,root,root,755)
