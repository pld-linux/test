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
%{__cc} -shared test.c -o libtest.so -Wl,-rpath,'$ORIGIN:/opt/%{_lib}:/lib/../%{_lib}/modules:/%{_lib}' -lz
%{__cc} -shared test.c -o libtest2.so -Wl,-rpath,'$ORIGIN'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install libtest.so $RPM_BUILD_ROOT%{_libdir}
install -D libtest2.so $RPM_BUILD_ROOT%{_libdir}/ratherlongpath/libtest2.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtest.so
%dir %{_libdir}/ratherlongpath
%attr(755,root,root) %{_libdir}/ratherlongpath/libtest2.so
