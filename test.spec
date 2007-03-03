%include	/usr/lib/rpm/macros.perl
Summary:	test package to run COMMAND like commands on builder :/
Summary(pl.UTF-8):	Polskie ogonki ąęśżźćółń
Summary(ru.UTF-8):	SMB клиент и сервер
Name:		test
Version:	8.56
Release:	0.5
License:	GPL
Group:		Applications/System
#BuildArch:	noarch
ExclusiveArch:	arm4
BuildRequires:	inexisttent-package
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout_c		-march=.*
%define		filterout_cxx	-march=.*

%description
this package should be never installed.

%prep
%setup -qcT
ls -ld /proc
ls -ld /proc/cpuinfo
ls -l /proc
echo CFLAGS: %{rpmcflags}
echo CXXFLAFGS: %{rpmcxxflags}
exit 1

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files
%defattr(644,root,root,755)
