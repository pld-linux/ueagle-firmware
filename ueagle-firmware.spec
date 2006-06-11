Summary:	The non-free firmware for eagle (SAGEM f@st) USB ADSL modem
Summary(pl):	Firmware dla modemów ADSL eagle (SAGEM f@st) USB
Name:		ueagle-firmware
Version:	1.1
Release:	1
License:	restricted, non-distributable
Group:		Libraries
Source0:	http://castet.matthieu.free.fr/eagle/non-free/ueagle-data-%{version}.tar.gz
# NoSource0-md5:	7df45e6c0b68ba3048eb18e730ebedee
NoSource:	0
URL:		http://castet.matthieu.free.fr/eagle/non-free/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		hotplugfwdir	/lib/firmware

%description
The non-free firmware for eagle (SAGEM f@st) USB ADSL modem.

%description -l pl
Firmware dla modemów ADSL eagle (SAGEM f@ast) USB.

%prep
%setup -q -n ueagle-data-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{hotplugfwdir}/ueagle-atm

install *.bin $RPM_BUILD_ROOT%{hotplugfwdir}/ueagle-atm
install *.fw $RPM_BUILD_ROOT%{hotplugfwdir}/ueagle-atm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/ueagle-atm
