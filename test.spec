%include	/usr/lib/rpm/macros.java
Summary:	test package to run COMMAND like commands on builder :/
Name:		test.foobar
Version:	8.56
Release:	0.6
License:	GPL
Source0:	http://dl.sourceforge.net/junit/junit4.1.zip
# Source0-md5:	e66d3e77c70b3297f2c6a12990fc3120
Source1:	Test.java
Group:		Applications/System
BuildRequires:	rpm-javaprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
this package should be never installed.

%prep
%setup -q -n junit4.1
cp %{SOURCE1} Test.java

%build
%javac Test.java

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -D junit-4.1.jar $RPM_BUILD_ROOT%{_javadir}/junit.jar
install Test.class $RPM_BUILD_ROOT%{_javadir}
install -D /bin/true $RPM_BUILD_ROOT%{_bindir}/untrue

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/untrue
%{_javadir}/*.jar
%{_javadir}/*.class
