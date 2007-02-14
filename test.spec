%include	/usr/lib/rpm/macros.perl
Summary:	test package to run COMMAND like commands on builder :/
Summary(pl.UTF-8):	Polskie ogonki ąęśżźćółń
Summary(ru.UTF-8):	SMB клиент и сервер
Name:		test
Version:	8.56
Release:	0.5
License:	GPL
Group:		Applications/System
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
this package should be never installed.

%prep
%setup -qcT
#exit 1

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files
%defattr(644,root,root,755)
