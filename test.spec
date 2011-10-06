%include	/usr/lib/rpm/macros.java
Summary:	test package to run COMMAND like commands on builder :/
Name:		test
Version:	5.3.11
Release:	0.10
License:	GPL
Group:		Applications/System
# extracted from http://rpm5.org/files/rpm/rpm-5.3/rpm-5.3.11-0.20110602.src.rpm
Source0:	rpm-%{version}.tar.gz
# Source0-md5:	7c1f624c22143324ee372dffd1a209c2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rpm5.org distributes now in src.rpm format, but we need tar.gz

%prep
%setup -qcT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
