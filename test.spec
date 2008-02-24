#
# Conditional build:
%bcond_with	noarch	# build noarch kernel-source package

%if "%{_arch}" == "noarch"
%define		with_noarch	1
%endif
#
Summary:	test
Name:		testarch
Version:	3
Release:	0.2
License:	GPL
Group:		Applications/System
%{?with_noarch:BuildArch:	noarch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package should be never installed.

%package source
Summary:	source
Group:		Applications/System

%description source
source

%prep
%setup -qcT
echo "target: %{_arch}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%if %{without noarch}
%files
%defattr(644,root,root,755)
%endif

%if %{with noarch}
%files source
%defattr(644,root,root,755)
%endif
