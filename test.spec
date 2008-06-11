Summary:	test path stripping
Name:		t-rpath
Version:	4.69
Release:	3
Epoch:		2
License:	GPL
Group:		Networking/Daemons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{summary}

%prep
%setup -qcT
cat <<'EOF'> test.c
int main() { return 1; }
EOF

%build
%{__cc} -shared test.c -o libtest.so -Wl,-rpath,'$ORIGIN'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install libtest.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/libtest.so
