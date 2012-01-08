Summary:	rpm symlins test
Name:		rpm-symlinks
Version:	2
Release:	10
License:	GPL
Group:		Applications/System
URL:		http://lists.pld-linux.org/mailman/pipermail/pld-devel-en/2012-January/022402.html
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		certsdir	/tmp/%{name}

%description
why is my symlink gone????

# symlinked file with n>1 hardlinks not installed
103886316 lrwxrwxrwx 2 glen glen 10 Jan  9 00:32 1.pem -> /etc/fstab
204945483 lrwxrwxrwx 1 glen glen 10 Jan  9 00:32 2.pem -> /etc/fstab
204945484 lrwxrwxrwx 1 glen glen 10 Jan  9 00:32 3.pem -> /etc/fstab

%prep
%setup -qcT

%build
ln -s /etc/fstab 1.pem
ln -s /etc/fstab 2.pem

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{certsdir}
# lost:
cp -pl 1.pem $RPM_BUILD_ROOT%{certsdir}

# installed:
cp -a 2.pem $RPM_BUILD_ROOT%{certsdir}

# installed:
ln -s /etc/fstab $RPM_BUILD_ROOT%{certsdir}/3.pem

ls -li $RPM_BUILD_ROOT%{certsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{certsdir}
