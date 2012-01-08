Summary:	rpm symlins test
Name:		rpm-symlinks
Version:	1
Release:	1
License:	GPL
URL:	http://lists.pld-linux.org/mailman/pipermail/pld-devel-en/2012-January/022402.html
Group:		Applications/System
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/tmp/%{name}

%description
why is my symlink gone????

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}
ln -s /etc/fstab $RPM_BUILD_ROOT%{_prefix}/fstablink

touch $RPM_BUILD_ROOT%{_prefix}/testfile
ln -s testfile $RPM_BUILD_ROOT%{_prefix}/testlink

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}
