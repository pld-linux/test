Summary:	testing builder
Name:		builder
Version:	1
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testing something

%prep
%setup -qcT
install -d a-dir

%install
install -d $RPM_BUILD_ROOT
ls -ld %{_builddir}/%{name}-%{version}/a-dir

%clean

%files
%defattr(644,root,root,755)
