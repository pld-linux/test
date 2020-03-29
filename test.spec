# skeleton for rpm testing.
# create your own test in separate branch, keep master branch clean
#
# git checkout -b test/feature
# git push origin -u test/feature
Summary:	testing pear deps
Name:		test-peardep
Version:	1.0
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://lists.pld-linux.org/mailman/pipermail/pld-devel-en/2020-March/025891.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprov_pear .*

%description
%{summary}.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
cat<<'EOF' > $RPM_BUILD_ROOT/test.php
<?php

require 'foo.php';
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/test.php
