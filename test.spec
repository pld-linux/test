#
# Conditional build:
%bcond_with	source		# build noarch kernel-source package
#
%if "%{_arch}" == "noarch"
%define		with_source	1
%endif
Summary:	test
Name:		kernel%{?with_source:-source}
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/System
%if %{with source}
BuildArch:	noarch
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package should be never installed.

%prep
%setup -qcT
echo "target: %{_arch}"

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
