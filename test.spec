#
# Conditional build:
%bcond_with	noarch	# build noarch kernel-source package
#
Summary:	test
Name:		testarch
Version:	2
Release:	0.2
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
install -d $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
