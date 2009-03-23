%bcond_without	pkg1	# build the "first" package
%bcond_with	pkg2	# build the "second" package

%if %{with pkg2}
# disable pkg1 if pkg2 is built
%undefine	with_pkg1
%endif
Summary:	triggertest
Name:		triggers
Version:	4
Release:	%{?with_pkg1:1}%{?with_pkg2:4}
License:	GPL
Group:		Applications/System
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package should be never installed.

%prep
%setup -qcT

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%if %{with pkg2}
%triggerpostun -- %{name} < 2
echo "%{name}-%{version}-%{release} postun on %{name} < 2"

%triggerpostun -- %{name} < 3
echo "%{name}-%{version}-%{release} postun on %{name} < 3"

%triggerpostun -- %{name} < 4
echo "%{name}-%{version}-%{release} postun on %{name} < 4"
%endif

%files
%defattr(644,root,root,755)
