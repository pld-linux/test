Summary:	fake dep
Name:		xorg-driver-video-vga
Version:	0.0
Release:	1
License:	GPL
Group:		Networking/Daemons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fake dep

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
