%include	/usr/lib/rpm/macros.perl
Summary:	test package to run COMMAND like commands on builder :/
Name:		test.foobar
Version:	8.56
Release:	0.6
License:	GPL
Group:		Applications/System
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%{expand:%%define	__cc	%(set -x;echo %__cc | sed -e 's,-gcc,-gcc4,')}
%{expand:%%define	__cxx	%(set -x;echo %__cxx | sed -e 's,-g++,-g++4,')}
%{expand:%%define	__cpp	%(set -x; echo %__cpp | sed -e 's,-gcc,-gcc4,')}

%description
this package should be never installed.

%package addon-enigmail
Summary:	Extension for the authentication and encryption features provided by GnuPG
Summary(pl):	Rozszerzenie do uwierzytelniania i szyfrowania zapewnianego przez GnuPG
Version:	0.93
Release:	1
License:	MPL/LGPL
Group:		Applications/Networking
URL:		http://enigmail.mozdev.org/

%description addon-enigmail
Enigmail is an extension to the mail client of Mozilla Thunderbird

%prep
%setup -qcT
: CC: %{__cc}
: CXX: %{__cxx}
: CPP: %{__cpp}
exit 1

%clean
rm -rf $RPM_BUILD_ROOT

%install

%pre

%files
%defattr(644,root,root,755)
