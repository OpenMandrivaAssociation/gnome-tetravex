%define _disable_rebuild_configure 1
%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-tetravex
Version:	3.38.2
Release:	8
Summary:	GNOME Tetravex game
License:	GPLv2+ and CC-BY-SA
Group:		Games/Puzzles
URL:		https://wiki.gnome.org/Tetravex
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
# Merge request (not merged yet) to fix compilation with meson 0.60+
Patch0:   https://gitlab.gnome.org/GNOME/gnome-tetravex/-/merge_requests/20.patch
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:	meson
BuildRequires:	itstool
BuildRequires:	vala-devel
BuildRequires:	libxml2-utils
Obsoletes:	gnotravex
# For help
Requires:	yelp

%description
A puzzle game where you have to match a grid of tiles together. The skill
level ranges from the simple two by two up to the seriously mind-bending six
by six grid.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/glib-2.0/schemas/org.gnome.Tetravex.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/org.gnome.Tetravex.desktop
%{_datadir}/dbus-1/services/org.gnome.Tetravex.service
%{_datadir}/locale/*/LC_MESSAGES/gnome-tetravex-gui.mo
