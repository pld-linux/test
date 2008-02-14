Summary:	testing
Name:		test4-1
Version:	4
Release:	0-01
License:	GPL
Group:		Applications/System
BuildRequires:	less
BuildRequires:	passivetex
BuildRequires:	gpgme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package should be never installed.

%prep
%setup -qcT

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- %{name} <= 2
echo "%{name}-%{version}-%{release} postun on %{name} < 2"

%triggerpostun -- %{name} <= 3
echo "%{name}-%{version}-%{release} postun on %{name} < 3"

%triggerpostun -- %{name} < 4
echo "%{name}-%{version}-%{release} postun on %{name} < 4"

%files
%defattr(644,root,root,755)
