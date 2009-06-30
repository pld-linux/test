%include	/usr/lib/rpm/macros.perl
Summary:	testing something
Name:		test
Version:	8.72
Release:	3
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testing something

%prep
%setup -q -c -T

%clean

%files
%defattr(644,root,root,755)
