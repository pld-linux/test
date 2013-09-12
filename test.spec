%define		src_ver	7u40
Summary:	fetch sun (oracle) jdk
Name:		test
Version:	1.7.0.40
Release:	2
License:	restricted, distributable
# http://www.oracle.com/technetwork/java/javase/terms/license/index.html
# See "LICENSE TO DISTRIBUTE SOFTWARE" section, which states you can
# redistribute in unmodified form.
Group:		Applications/System
# Accept license and download from
# http://www.oracle.com/technetwork/java/javase/downloads/index.html
Source0:	jdk-%{src_ver}-linux-i586.tar.gz
# Source0-md5:	0079cecc8c4d0f088ace5d0ea99d0c5c
Source1:	jdk-%{src_ver}-linux-x64.tar.gz
# Source1-md5:	511ea34e4a42955bc03c28afa4b8f6cf
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
