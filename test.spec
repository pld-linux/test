Summary:	test user/group add/remove
Name:		users
Version:	4
Release:	1
License:	GPL
Group:		Tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tests user/group add/remove.

%prep
%setup -qcT

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%pre
set -x
%addusertogroup -q clamav amavis

%files
%defattr(644,root,root,755)
