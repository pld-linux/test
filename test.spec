%include	/usr/lib/rpm/macros.perl
Summary:	testing something
Name:		test
Version:	8.72
Release:	10
License:	GPL
Group:		Applications/System
URL:		http://www.pld-linux.org/
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testing something.

%prep
%setup -q -c -T

%build
cat >a.c <<EOF
int main() { return 0; };
EOF
gcc a.c -o a

%install
install -d $RPM_BUILD_ROOT
install a $RPM_BUILD_ROOT

%clean

%files
%defattr(644,root,root,755)
/a
