
# Internal QML imports
%global __requires_exclude qt6qmlimport\\(org\\.kde\\.kwin\\.3.*
# %%global __requires_exclude qmlimport\\((org\\.kde\\.private\\.kcms\\.kwin\\.effects|org\\.kde\\.kcms\\.kwinrules|org\\.kde\\.kwin\\.private\\.overview|org\\.kde.kwin\\.private\\.desktopgrid|org\\.kde\\.KWin\\.Effect\\.WindowView|org\\.kde\\.kwin\\.kwinxwaylandsettings).*

%global commit 7ea0e160275a3d660177c7b1f4a13057b9a6b2fb
#%%bcond_without  lang

Name:           kwinft
Version:        5.92.90
Release:        1
Summary:        Fast Track reboot of KWin
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://gitlab.com/kwinft/%{name}
Source:         %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.bz2
Patch1:         soversion.patch

BuildRequires:  fdupes
BuildRequires:  cmake(Catch2)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(KF6)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  libcap-utils
BuildRequires:  pkgconfig
BuildRequires:  cmake(Breeze)
BuildRequires:  cmake(KDecoration2)
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KScreenLocker)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaQuick)
BuildRequires:  cmake(QAccessibilityClient6)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:  cmake(Qt6Quick)
#BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6UiTools) 
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:  cmake(Wrapland)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxcvt)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-damage) 
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xwayland)
Requires:       breeze6-decoration
Requires:       kf6-kirigami-imports
Requires:       kglobalacceld6
Requires:       libkwinft6 = %{version}
# SECTION QML dependencies
Requires:       kf6-kdeclarative-imports
Requires:       kf6-kitemmodels-imports
Requires:       plasma6-framework-components
Requires:       qt6-declarative-imports
Requires:       qt6-multimedia-imports
Requires:       x11-server-xorg
# /SECTION
# For post and verifyscript
Requires(post): permissions
Requires(verify): permissions
# xorg-x11-server-wayland is required by plasma6-session-wayland, but not KWinFT itself
Recommends:     xorg-x11-server-wayland
Conflicts:      kwin5
Conflicts:      kwin5-lang
Provides:       kwin6
Conflicts:      kwin6
# /usr/share/kwin/tabbox/thumbnail_grid/metadata.json conflicts with plasma5-addons
Conflicts:      plasma5-addons
Conflicts:      plasma5-addons-lang
# Needed to show dialogs
Requires:       kdialog
# We can reuse kwin5’s localization and doc files
Recommends:     kwin6-doc
Recommends:     kwin6-lang
Provides:       qt6qmlimport(org.kde.kwin.3) = 0
Provides:       windowmanager

%description
KWinFT (KWin Fast Track) is an easy to use, but flexible, composited window manager for X.Org
windowing systems (Wayland, X11) on Linux.
The KWinFT project consists of the window manager KWinFT and the accompanying but
independent libwayland wrapping Qt/C++ library Wrapland.

%package -n libkwinft6
Summary:        KWinFT library
Conflicts:      libkwin6

%description -n libkwinft6
This package provides the kWinFT library.

%package -n x11
Summary:        KDE Window Manager for X11
Conflicts:      kwin5
Conflicts:      kwin6
Requires:       xorg-x11-server
Requires:       %{name} = %{version}

%description -n x11
KWinFT is Plasma window manager.
This package provides the X11 window manager.

%package -n wayland
Summary:        KDE Window Manager for X11
Conflicts:      kwin5
Conflicts:      kwin6
Requires:       xorg-x11-server
Requires:       %{name} = %{version}

%description -n wayland
KWinFT is Plasma window manager.
This package provides the X11 window manager.


%package -n devel
Summary:        KWinFT: Build Environment
Requires:       libkwinft6 = %{version}
Requires:       kdecoration6-devel
Requires:       pkgconfig(epoxy)
Conflicts:      kdebase4-workspace-devel
Conflicts:      kwin5-devel

%description -n devel
KWinFT (KWin Fast Track) is an easy to use, but flexible, composited window manager for X.Org
windowing systems (Wayland, X11) on Linux.
The KWinFT project consists of the window manager KWinFT and the accompanying but
independent libwayland wrapping Qt/C++ library Wrapland.

%prep
%autosetup -p1 -n %{name}-%{commit}

sed -i 's#env python3$#python3#' kconf_update/kwin-6.0-overview-activities-shortcuts.py

%build
export CC=gcc
export CXX=g++
# fix fatal error: wayland-server-core.h: No such file or directory
export CFLAGS="%{optflags} -I%{_includedir} -I%{_includedir}/wayland"
#export CXXFLAGS="${CFLAGS}"
%cmake -DBUILD_TESTING=OFF
%make_build

%install
%make_install -C build

# Just use upstream KWin's help files and translations
rm -rf %{buildroot}%{_kf6_sharedir}/doc
rm -rf %{buildroot}%{_kf6_sharedir}/locale

%preun -n wayland
%{systemd_user_preun plasma-kwin_wayland.service}

%post -n wayland
%set_permissions %{_kf6_bindir}/kwin_wayland
%{systemd_user_post plasma-kwin_wayland.service}

%postun -n wayland
%{systemd_user_postun plasma-kwin_wayland.service}

%preun -n x11
%{systemd_user_preun plasma-kwin_x11.service}

%post -n x11
%{systemd_user_post plasma-kwin_x11.service}

%postun -n x11
%{systemd_user_postun plasma-kwin_x11.service}

%files
%license LICENSE*
%doc %{_datadir}/doc/HTML/en/kcontrol/
%{_libexecdir}/kwin-applywindowdecoration
%{_libexecdir}/kwin_killer_helper
%{_datadir}/applications/kcm_kwin_effects.desktop
%{_datadir}/applications/kcm_kwin_scripts.desktop
%{_datadir}/applications/kcm_kwin_virtualdesktops.desktop
%{_datadir}/applications/kcm_kwindecoration.desktop
%{_datadir}/applications/kcm_kwinoptions.desktop
%{_datadir}/applications/kcm_kwinrules.desktop
%{_datadir}/applications/kcm_kwintabbox.desktop
%{_datadir}/applications/kwincompositing.desktop
%{_datadir}/config.kcfg/kwin_colorcorrect.kcfg
%{_datadir}/config.kcfg/kwindecorationsettings.kcfg
%{_datadir}/config.kcfg/virtualdesktopssettings.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.KWin.VirtualDesktopManager.xml
%{_datadir}/dbus-1/interfaces/org.kde.KWin.xml
%{_datadir}/dbus-1/interfaces/org.kde.kwin.ColorCorrect.xml
%{_datadir}/dbus-1/interfaces/org.kde.kwin.Compositing.xml
%{_datadir}/dbus-1/interfaces/org.kde.kwin.InputDevice.xml
%{_datadir}/dbus-1/interfaces/org.kde.kwin.VirtualKeyboard.xml
%{_datadir}/kconf_update/kwin-6.0-overview-activities-shortcuts.py
%{_datadir}/kconf_update/kwin.upd
%{_datadir}/knotifications6/kwin.notifyrc
%{_datadir}/knsrcfiles/
%{_datadir}/kwin/
%{_datadir}/qlogging-categories6/org_kde_kwin.categories
%{_iconsdir}/hicolor/*x*/apps/kwin.png
%{_iconsdir}/hicolor/scalable/apps/kwin.svgz

%files -n x11
%{_bindir}/kwin_x11
%{_userunitdir}/plasma-kwin_x11.service

%files -n wayland
%{_bindir}/kwin_wayland
%{_bindir}/kwin_wayland_wrapper
%{_userunitdir}/plasma-kwin_wayland.service

%files -n libkwinft6
%{_libdir}/kconf_update_bin/kwin5_update_default_rules
%{_libdir}/libbase-x11-backend.so
%{_libdir}/libkcmkwincommon.so.*
%{_libdir}/libkwinft*
%{_libdir}/plugins/kf6/packagestructure/
%{_libdir}/plugins/kwin/effects/
%{_libdir}/plugins/org.kde.kdecoration2.kcm/kcm_auroraedecoration.so
%{_libdir}/plugins/org.kde.kdecoration2/org.kde.kwin.aurorae.so
%{_libdir}/plugins/plasma/kcms/systemsettings*
%{_libdir}/qml/org/kde/kwin/

%files -n devel
%{_includedir}/kwinft/
%{_libdir}/cmake/KWinDBusInterface/KWinDBusInterfaceConfig.cmake
%{_libdir}/cmake/kwinft/
