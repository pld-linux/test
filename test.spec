Summary:	307183
Name:		fdleak
Version:	307183
Release:	1
License:	GPL
Group:		Hacking/Bugs
Requires:	lvm2 >= 2.02
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
307183

%prep

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/lvs || :

%files
%defattr(644,root,root,755)
