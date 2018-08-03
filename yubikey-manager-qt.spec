Summary:	Tool for managing your YubiKey configuration
Summary(pl.UTF-8):	Narzędzie do zarządzania urządzeniami YubiKey
Name:		yubikey-manager-qt
Version:	0.5.2
Release:	1
License:	BSD
Group:		Applications/System
Source0:	https://developers.yubico.com/yubikey-manager-qt/Releases/%{name}-%{version}.tar.gz
# Source0-md5:	387cf107c8462819ef0fb8d81be922c5
URL:		https://developers.yubico.com/yubikey-manager-qt/
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Qml-devel >= 5
BuildRequires:	Qt5Quick-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-linguist >= 5
BuildRequires:	qt5-qmake >= 5
Requires:	python-cryptography
Requires:	python-fido2
# python-ykman
Requires:	yubikey-manager >= 0.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This application provides an easy way to perform the most common
configuration tasks on a YubiKey.

%description
Ta aplikacja pozwala w łatwy sposób wykonać większość zadań
konfiguracyjnych urządzeń YubiKey.

%prep
%setup -qc

%build
qmake-qt5 yubikey-manager-qt.pro \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

cp -p resources/ykman-gui.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -p resources/icons/ykman.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README
%attr(755,root,root) %{_bindir}/ykman-gui
%{_desktopdir}/ykman-gui.desktop
%{_pixmapsdir}/ykman.png
