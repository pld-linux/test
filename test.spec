%include	/usr/lib/rpm/macros.perl
Summary:	test package to run COMMAND like commands on builder :/
Name:		test.foobar
Version:	8.56
Release:	0.6
License:	GPL
Group:		Applications/System
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# add suffix, but allow ccache, etc in ~/.rpmmacros
%{expand:%%define	__cc	%(set -x;echo %__cc | sed -e 's,-gcc,-gcc4,')}
%{expand:%%define	__cxx	%(set -x;echo %__cxx | sed -e 's,-g++,-g++4,')}
%{expand:%%define	__cpp	%(set -x; echo %__cpp | sed -e 's,-gcc,-gcc4,')}

%description
this package should be never installed.

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
