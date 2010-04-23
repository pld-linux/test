%include	/usr/lib/rpm/macros.java
Summary:	java-sun killer
Name:		test
Version:	3
Release:	141592
License:	Fri
Group:		Applications/System
BuildConflicts:	java-sun
BuildConflicts:	java-sun-jre
BuildConflicts:	java-sun-tools
BuildRequires:	icedtea6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package should never be installed.

%prep
%setup -qcT

%clean
rm -rf $RPM_BUILD_ROOT

%pre
false

%files
%defattr(644,root,root,755)
