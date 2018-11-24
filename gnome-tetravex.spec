%define _disable_rebuild_configure 1
%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define debug_package %{nil}

Name:		gnome-tetravex
Version:	3.22.0
Release:	1
Summary:	GNOME Tetravex game
License:	GPLv2+ and CC-BY-SA
Group:		Games/Puzzles
URL:		https://wiki.gnome.org/Tetravex
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
Obsoletes:	gnotravex
# For help
Requires:	yelp

%description
A puzzle game where you have to match a grid of tiles together. The skill
level ranges from the simple two by two up to the seriously mind-bending six
by six grid.

%prep
%setup -q

%build
%configure CFLAGS='-Wno-error'
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.tetravex.gschema.xml
%{_iconsdir}/*/*/apps/%{name}*.*
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml


