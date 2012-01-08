Summary:	rpm symlins test
Name:		rpm-symlinks
Version:	1
Release:	10
License:	GPL
Group:		Applications/System
URL:		http://lists.pld-linux.org/mailman/pipermail/pld-devel-en/2012-January/022402.html
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/tmp/%{name}

%define		certsdir	%{_prefix}/kk
%define		cacertsdir	/usr/share/ca-certificates
%define		_sysconfdir	/etc/fetch-crl.d

%description
why is my symlink gone????

%prep
%setup -qcT

%build
for cert in %{cacertsdir}/esteid/*.crt; do
	ln -s $cert $(basename $cert .crt).pem
done
c_rehash.sh .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/kk
ln -s /etc/fstab $RPM_BUILD_ROOT%{_prefix}/fstablink
ln -s /etc/fstab $RPM_BUILD_ROOT%{_prefix}/kk/fstablink.1
ln -s /etc/fstab.crt $RPM_BUILD_ROOT%{_prefix}/fflink

touch $RPM_BUILD_ROOT%{_prefix}/testfile
ln -s testfile $RPM_BUILD_ROOT%{_prefix}/testlink
cp -pl $RPM_BUILD_ROOT%{_prefix}/testlink{,2}
date > id.ee.conf

install -d $RPM_BUILD_ROOT{%{certsdir},%{_sysconfdir}}
cp -p id.ee.conf $RPM_BUILD_ROOT%{_sysconfdir}
cp -pl *.pem *.0 $RPM_BUILD_ROOT%{certsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}
