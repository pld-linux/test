Summary:	test cpuflags
Name:		test
Version:	5.3.11
Release:	0.11
License:	GPL
Group:		Applications/System
%ifarch %{x8664}
Requires(cpuflags):	lm
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
test cpuflags on x86_64 that the kernel is compatible with target cpu. thus if
you install rpm on 32bit booted kernel it could be still validated to be arch
compatible.

%prep
%setup -qcT

%clean
rm -rf $RPM_BUILD_ROOT

%pretrans
%ifarch %{x8664}
if [ -e /proc/cpuinfo ] && ! grep -q '\<lm\>' /proc/cpuinfo; then
	echo >&2 "WARNING: This hardware does not support x86_64 architecture"
	exit 1
fi
%endif

%pre
%ifarch %{x8664}
if [ -e /proc/cpuinfo ] && ! grep -q '\<lm\>' /proc/cpuinfo; then
	echo >&2 "WARNING: This hardware does not support x86_64 architecture"
	exit 1
fi
%endif

%files
%defattr(644,root,root,755)
