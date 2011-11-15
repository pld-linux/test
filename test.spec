Summary:	Distfiles Fetcher
Name:		distfiles-mtime
Version:	2011.11.02
Release:	1
License:	GPL
Group:		Networking/Hacking
Source0:	http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
# Source0-md5:	2f6e084013b442bb94a7ef0232818d3f
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
this test should ensure distfiles stores files with original timestamp

%prep
%setup -qcT
cp -p %{SOURCE0} .
ls -l *dat*
gunzip GeoIP.dat.gz
ls -l *dat*

ver=$(stat -c '%y' GeoIP.dat | awk '{print $1}' | tr - .)
if [ "$ver" != %{version} ]; then
	exit 1
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
