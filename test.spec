%define		src_ver	7u45
Summary:	fetch sun (oracle) jdk
Name:		test
Version:	1.7.0.45
Release:	2
License:	restricted, distributable
# http://www.oracle.com/technetwork/java/javase/terms/license/index.html
# See "LICENSE TO DISTRIBUTE SOFTWARE" section, which states you can
# redistribute in unmodified form.
Group:		Applications/System
# Accept license and download from
# http://www.oracle.com/technetwork/java/javase/downloads/index.html
Source0:	jdk-%{src_ver}-linux-i586.tar.gz
# Source0-md5:	66b47e77d963c5dd652f0c5d3b03cb52
Source1:	jdk-%{src_ver}-linux-x64.tar.gz
# Source1-md5:	bea330fcbcff77d31878f21753e09b30
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
