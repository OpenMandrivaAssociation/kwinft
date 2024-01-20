# Internal QML imports
%global __requires_exclude qt6qmlimport\\(org\\.kde\\.kwin\\.3.*
# %%global __requires_exclude qmlimport\\((org\\.kde\\.private\\.kcms\\.kwin\\.effects|org\\.kde\\.kcms\\.kwinrules|org\\.kde\\.kwin\\.private\\.overview|org\\.kde.kwin\\.private\\.desktopgrid|org\\.kde\\.KWin\\.Effect\\.WindowView|org\\.kde\\.kwin\\.kwinxwaylandsettings).*

%global commit 7ea0e160275a3d660177c7b1f4a13057b9a6b2fb
%global kf6_version 5.240.0
%define qt6_version 6.5.0
#%%bcond_without  lang

Name:           kwinft
Version:        5.92.90
Release:        0
Summary:        Fast Track reboot of KWin
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://gitlab.com/kwinft/%{name}
Source:         %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.bz2
# Patch0:         291.diff
Patch1:         soversion.patch
Patch2:         path.patch
# Patch3:         new_virtuals.patch
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libcap-devel
BuildRequires:  libcap-progs
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel >= %{qt6_version}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(Breeze) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KDecoration2) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Declarative) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami2) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KScreenLocker) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(QAccessibilityClient6)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Wrapland)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm) >= 2.4.112
BuildRequires:  pkgconfig(libinput) >= 1.9
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.29
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxcvt)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots) >= 0.18.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb) >= 1.10
BuildRequires:  pkgconfig(xcb-composite) >= 1.10
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-damage) >= 1.10
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-glx) >= 1.10
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-randr) >= 1.10
BuildRequires:  pkgconfig(xcb-render) >= 1.10
BuildRequires:  pkgconfig(xcb-shape) >= 1.10
BuildRequires:  pkgconfig(xcb-shm) >= 1.10
BuildRequires:  pkgconfig(xcb-sync) >= 1.10
BuildRequires:  pkgconfig(xcb-xfixes) >= 1.10
BuildRequires:  pkgconfig(xcb-xkb) >= 0.7.0
BuildRequires:  pkgconfig(xkbcommon) >= 0.7.0
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xwayland)
Requires:       breeze6-decoration >= %{_plasma6_bugfix}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kglobalacceld6  >= %{_plasma6_bugfix}
Requires:       libkwinft6 = %{version}
# SECTION QML dependencies
Requires:       kf6-kdeclarative-imports >= %{kf6_version}
Requires:       kf6-kitemmodels-imports >= %{kf6_version}
Requires:       plasma6-framework-components >= %{_plasma6_bugfix}
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       qt6-multimedia-imports >= %{qt6_version}
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

%package x11
Summary:        KDE Window Manager for X11
Conflicts:      kwin5
Conflicts:      kwin6
Requires:       xorg-x11-server
Requires:       %{name} = %{version}

%description x11
KWinFT is Plasma window manager.
This package provides the X11 window manager.

%package -n libkwinft6
Summary:        KWinFT library
Conflicts:      libkwin6

%description -n libkwinft6
This package provides the kWinFT library.

%package devel
Summary:        KWinFT: Build Environment
Requires:       libkwinft6 = %{version}
Requires:       kdecoration6-devel >= %{_plasma6_bugfix}
Requires:       pkgconfig(epoxy)
Conflicts:      kdebase4-workspace-devel
Conflicts:      kwin5-devel

%description devel
KWinFT (KWin Fast Track) is an easy to use, but flexible, composited window manager for X.Org
windowing systems (Wayland, X11) on Linux.
The KWinFT project consists of the window manager KWinFT and the accompanying but
independent libwayland wrapping Qt/C++ library Wrapland.

%prep
%autosetup -p1 -n %{name}-%{commit}

sed -i 's#env python3$#python3#' kconf_update/kwin-6.0-overview-activities-shortcuts.py

%build
# fix fatal error: wayland-server-core.h: No such file or directory
#export CFLAGS="%%{optflags} -I%%{_includedir} -I%%{_includedir}/wayland"
#export CXXFLAGS="${CFLAGS}"
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}%{_kf6_libdir}
%fdupes %{buildroot}%{_kf6_sharedir}

# Just use upstream KWin's help files and translations
rm -rf %{buildroot}%{_kf6_sharedir}/doc
rm -rf %{buildroot}%{_kf6_sharedir}/locale

%preun
%{systemd_user_preun plasma-kwin_wayland.service}

%post
%ldconfig
%ldconfig -n libkwinft6
%set_permissions %{_kf6_bindir}/kwin_wayland
%{systemd_user_post plasma-kwin_wayland.service}

%postun
%ldconfig
%ldconfig -n libkwin6
%{systemd_user_postun plasma-kwin_wayland.service}

%ldconfig_scriptlets -n libkwinft6

%preun x11
%{systemd_user_preun plasma-kwin_x11.service}

%post x11
%{systemd_user_post plasma-kwin_x11.service}

%postun x11
%{systemd_user_postun plasma-kwin_x11.service}

%verifyscript
%verify_permissions -e %{_kf6_bindir}/kwin_wayland

%files
%verify(not caps) %{_kf6_bindir}/kwin_wayland
%license LICENSE*
%{_kf6_bindir}/kwin_wayland_wrapper
%{_kf6_applicationsdir}/*.desktop
%{_kf6_debugdir}/org_kde_kwin.categories
%{_kf6_knsrcfilesdir}/*.knsrc
%{_kf6_libdir}/kconf_update_bin/
%{_kf6_libdir}/libbase-x11-backend.so
%{_kf6_libdir}/libkcmkwincommon.*
%{_kf6_notificationsdir}/kwin.notifyrc
%dir %{_kf6_plugindir}/kwin
%dir %{_kf6_plugindir}/kwin/effects
%dir %{_kf6_plugindir}/kwin/effects/configs
%dir %{_kf6_plugindir}/kf6
%dir %{_kf6_plugindir}/kf6/packagestructure
%dir %{_kf6_plugindir}/org.kde.kdecoration2
%dir %{_kf6_plugindir}/org.kde.kdecoration2.kcm
%dir %{_kf6_plugindir}/plasma
%dir %{_kf6_plugindir}/plasma/kcms
%dir %{_kf6_plugindir}/plasma/kcms/systemsettings
%dir %{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets
%{_kf6_plugindir}/kf6/packagestructure/kwin_aurorae.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_decoration.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_effect.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_scripts.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_windowswitcher.so
%{_kf6_plugindir}/kwin/effects/configs/kcm_kwin4_genericscripted.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_blur_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_colorblindnesscorrection_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_cube_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_cubeslide_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_diminactive_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_glide_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_invert_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_lookingglass_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_magiclamp_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_magnifier_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_mouseclick_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_mousemark_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_resize_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_showpaint_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_slide_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_thumbnailaside_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_trackmouse_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_windowview_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_wobblywindows_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_zoom_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_overview_config.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm*.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kwin*.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kwincompositing.so
%{_kf6_plugindir}/org.kde.kdecoration2/org.kde.kwin.aurorae.so
%{_kf6_plugindir}/org.kde.kdecoration2.kcm/kcm_auroraedecoration.so

%dir %{_kf6_qmldir}/org/
%dir %{_kf6_qmldir}/org/kde/
%dir %{_kf6_qmldir}/org/kde/kwin/
%{_kf6_qmldir}/org/kde/kwin/decoration/
%{_kf6_qmldir}/org/kde/kwin/decorations/
%{_kf6_qmldir}/org/kde/kwin/private/

%{_kf6_sharedir}/config.kcfg/
%{_kf6_sharedir}/icons/hicolor/*/apps/kwin.png
%{_kf6_sharedir}/icons/hicolor/scalable/apps/kwin.svgz
%{_kf6_sharedir}/kwin/
%{_kf6_sharedir}/kconf_update/
%{_libexecdir}/kwin-applywindowdecoration
%{_libexecdir}/kwin_killer_helper
%{_userunitdir}/plasma-kwin_wayland.service

%files x11
%{_kf6_bindir}/kwin_x11
%{_userunitdir}/plasma-kwin_x11.service

%files -n libkwinft6
%{_kf6_libdir}/libkwinft-*.so.6
%{_kf6_libdir}/libkwinft-*.so.5.*

%files devel
%{_includedir}/kwinft/
%{_kf6_cmakedir}/KWinDBusInterface/
%{_kf6_cmakedir}/kwinft/
%{_kf6_dbusinterfacesdir}/org.kde.kwin.*
%{_kf6_dbusinterfacesdir}/org.kde.KWin.*
