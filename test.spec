Summary:	undos macro testing
Name:		undos
Version:	1
Release:	1
License:	GPL
Group:		Hacking/Bugs
BuildRequires:	rpmbuild(macros) >= 1.565
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
undos macro testing

%prep
%setup -qcT
: if we exit with status 42, we passed

touch one two three
touch mina.jah sina.nii homme.naa sööme.õun toitu.jää

: 1. undos list of files
: 2. undos files case insensitive by extension
: 3. undos files by extension

%undos one two three
%undos -i -f jah,nii,naa
%undos -f õun,jää

exit 42

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
