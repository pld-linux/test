%include	/usr/lib/rpm/macros.perl
Summary:	test package to run COMMAND like commands on builder :/
Name:		test.foobar
Version:	8.56
Release:	0.6
License:	GPL
Group:		Applications/System
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
this package should be never installed.

%prep
%setup -qcT

%clean
rm -rf $RPM_BUILD_ROOT

%install

%pre
%groupadd test

%files
%defattr(644,root,root,755)
