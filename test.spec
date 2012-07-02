Summary:	fetch sun (oracle) jdk
Name:		test
Version:	1.6.0.33
Release:	1
License:	restricted, distributable
# http://www.oracle.com/technetwork/java/javase/terms/license/index.html
# See "LICENSE TO DISTRIBUTE SOFTWARE" section, which states you can
# redistribute in unmodified form.
Group:		Applications/System
# Accept license and download from
# http://www.oracle.com/technetwork/java/javase/downloads/index.html
Source0:	jdk-6u33-linux-i586.bin
# Source0-md5:	276d31fabcc1f10b401c1e8b7680e460
Source1:	jdk-6u33-linux-x64.bin
# Source1-md5:	b6764210dc436d43b5bb8caa1cc1f461
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
