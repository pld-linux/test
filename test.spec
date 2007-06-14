# 2.18.0
# http://ftp.gnome.org/pub/GNOME/teams/releng/2.18.0/versions
Summary:	Gnome updater
Name:		gnome-updater
Version:	2.18.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/teams/releng/2.18.0/versions
NoSource:	0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -qcT
cp %{SOURCE0} .

%build
awk -F: '
/^##/{pkg = tolower(substr($0, 4)); subpkg = ""; d = 0; next }
/^#/ {subpkg = tolower(substr($0, 3)); d = 0; next }

!/^$/{
if (!d) {
	if (subpkg) {
		name = pkg "-" subpkg;
	} else {
		name = pkg;
	}
	printf("\n%%%%files %%s\n", name);
	printf("\n%%%%package %%s\n", name);
	d = 1;
}
printf("Requires: %%s >= %%s\n", $2, $3);
}' versions > base.spec

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
