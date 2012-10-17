%include	/usr/lib/rpm/macros.php
Summary:	php deps tester
Name:		php-deps
Version:	1
Release:	0.1
License:	GPL
Group:		Development/Languages/PHP
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_pear Excluded.php

%description
Testing PHP deps.

%prep
%setup -qcT
cat <<EOF
%__noautoreq
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
cat <<EOF > $RPM_BUILD_ROOT%{php_pear_dir}/a.php
<?php
require_once 'PEAR.php';
require_once 'Excluded.php';
EOF

%clean
install -d $RPM_BUILD_ROOT
pkg=%{_rpmdir}/%{name}-%{version}-%{release}.%{_target_cpu}.rpm
rpm -qp --provides $pkg | tee provides.log
rpm -qp --requires $pkg | tee requires.log

%files
%defattr(644,root,root,755)
%{php_pear_dir}/*
