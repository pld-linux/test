Summary:	test package to run COMMAND like commands on builder :/
Name:		test
Version:	2.1.7
Release:	0.10
License:	GPL
Group:		Applications/System
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/itext/iText-src-2.1.7.tar.gz/38c3d47e0f0a87a8151b5b2f208b461e/iText-src-2.1.7.tar.gz
# Source0-md5:	38c3d47e0f0a87a8151b5b2f208b461e
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
