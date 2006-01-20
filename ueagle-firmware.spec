Summary:	The non-free firmware for eagle usb adsl modem
Summary(pl):	Firmware dla modemów SAGEM f@ast usb
Name:		ueagle-firmware
Version:	1.0
Release:	1
License:	restricted, non-distributable
Group:		Libraries
Source0:	http://castet.matthieu.free.fr/eagle/release/ueagle-data-%{version}.tar.gz
# NoSource0-md5:	e86b86462ce022e1399acfb37d2daf3f
NoSource:	0
URL:		http://castet.matthieu.free.fr/eagle/release/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		hotplugfwdir	/lib/firmware

%description
The non-free firmware for eagle usb adsl modem.

%description -l pl
Firmware dla modemów SAGEM f@ast usb.

%prep
%setup -q -n ueagle-data-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{hotplugfwdir}/ueagle-atm

install *.bin $RPM_BUILD_ROOT/%{hotplugfwdir}/ueagle-atm
install *.fw $RPM_BUILD_ROOT/%{hotplugfwdir}/ueagle-atm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/ueagle-atm
