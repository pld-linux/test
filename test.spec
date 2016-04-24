# skeleton for rpm testing.
# create your own test in separate branch, keep master branch clean
# git checkout -b somebranch
# git push origin -u somebranch
Summary:	testing something
Name:		test
Version:	1
Release:	7
License:	GPL
Group:		Applications/System
Source0:    test.tgz
# Source0-md5:   a23576184c7a93c5f02401aca9907dbd
URL:		http://www.pld-linux.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testing something

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cat >$RPM_BUILD_ROOT%{_bindir}/test1 <<'EOF'
ffkdljgldfn ldn d
dskjf; k
s dsk jf
sdfk jsdk
EOF

cat >$RPM_BUILD_ROOT%{_bindir}/test2 <<'EOF'
#!/usr/bin/python

print "test2"
EOF

cat >$RPM_BUILD_ROOT%{_bindir}/test3 <<'EOF'
#!/usr/bin/python2

print "test3"
EOF

cat >$RPM_BUILD_ROOT%{_bindir}/test4 <<'EOF'
#!/usr/bin/python3

print("test4")
EOF

cat >$RPM_BUILD_ROOT%{_bindir}/test5 <<'EOF'
#!/usr/bin/env python

print "test5"
EOF

cat >$RPM_BUILD_ROOT%{_bindir}/test6 <<'EOF'
#!/usr/bin/env python2

print "test6"
EOF

cat >$RPM_BUILD_ROOT%{_bindir}/test7 <<'EOF'
#!/usr/bin/env python3

print("test7")
EOF

cat >$RPM_BUILD_ROOT%{_bindir}/test8 <<'EOF'
#! /usr/bin/python2

print "test8"
EOF

cat >$RPM_BUILD_ROOT%{_bindir}/test9 <<'EOF'
#! /usr/bin/env python3

print("test9")
EOF

cat >$RPM_BUILD_ROOT%{_bindir}/test10 <<'EOF'
#!/bin/sh

echo test10
EOF

cat >$RPM_BUILD_ROOT%{_bindir}/test11 <<'EOF'
#!/usr/bin/python9.9

print "test11"
EOF

cat >$RPM_BUILD_ROOT%{_bindir}/test12 <<'EOF'
#!/usr/bin/python%{py_ver}

print "test12"
EOF

cat >$RPM_BUILD_ROOT%{_bindir}/test13 <<'EOF'
#!/usr/bin/python%{py3_ver}

print("test13")
EOF

cat >$RPM_BUILD_ROOT%{_bindir}/"test14 with space" <<'EOF'
#!/usr/bin/python

print "test14"
EOF

install -d $RPM_BUILD_ROOT/%{_datadir}/"dir with spaces"
cat >$RPM_BUILD_ROOT%{_datadir}/"dir with spaces"/test15 <<'EOF'
#!/usr/bin/python

print "test15"
EOF

chmod a+x $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/"dir with spaces"}/*

%clean

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*/*
