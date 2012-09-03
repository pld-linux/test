%define		src_ver	6u35
Summary:	fetch sun (oracle) jdk
Name:		test
Version:	1.6.0.35
Release:	1
License:	restricted, distributable
# http://www.oracle.com/technetwork/java/javase/terms/license/index.html
# See "LICENSE TO DISTRIBUTE SOFTWARE" section, which states you can
# redistribute in unmodified form.
Group:		Applications/System
# Accept license and download from
# http://www.oracle.com/technetwork/java/javase/downloads/index.html
Source0:	jdk-%{src_ver}-linux-i586.bin
# Source0-md5:	592b60fcc11cbd6d323a3f357327d701
Source1:	jdk-%{src_ver}-linux-x64.bin
# Source1-md5:	3876e012629977ce08054347cf3bfdb0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
oracle download urls need cookie and java.net offers just early access
snapshots

%prep
%setup -qcT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
