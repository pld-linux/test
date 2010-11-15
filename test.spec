#define		rel		7%{?with_multigl:.mgl}
%include	/usr/lib/rpm/macros.perl
Summary:	testing something
Name:		test
Version:	8.72
Release:	10
#Release:	%{rel}
License:	GPL
Group:		Applications/System
Source0:	http://execve.pl/u/u?r=23#/xxx
# Source0-md5:	6de9439834c9147569741d3c9c9fc010
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
