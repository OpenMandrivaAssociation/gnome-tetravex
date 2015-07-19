%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define debug_package %{nil}

Name:		gnome-tetravex
Version:	3.16.0
Release:	2
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
%{_iconsdir}/*/*/apps/%{name}.*
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Tue Feb 17 2015 wally <wally> 3.14.0-3.mga5
+ Revision: 815343
- require yelp for showing help

* Wed Oct 15 2014 umeabot <umeabot> 3.14.0-2.mga5
+ Revision: 741366
- Second Mageia 5 Mass Rebuild

* Mon Sep 29 2014 wally <wally> 3.14.0-1.mga5
+ Revision: 731698
- new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.92-2.mga5
+ Revision: 679778
- Mageia 5 Mass Rebuild

* Tue Sep 16 2014 ovitters <ovitters> 3.13.92-1.mga5
+ Revision: 676942
- new version 3.13.92

* Tue Sep 02 2014 ovitters <ovitters> 3.13.91-1.mga5
+ Revision: 670808
- new version 3.13.91

* Tue Aug 19 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 665290
- new version 3.13.90

* Mon Jul 21 2014 ovitters <ovitters> 3.13.4-1.mga5
+ Revision: 655267
- new version 3.13.4

* Thu May 29 2014 ovitters <ovitters> 3.13.1-1.mga5
+ Revision: 627592
- new version 3.13.1

* Mon May 12 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622278
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 614226
- new version 3.12.1

* Sun Mar 23 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 606976
- new version 3.12.0

* Mon Mar 17 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604627
- new version 3.11.92

* Mon Mar 03 2014 ovitters <ovitters> 3.11.91-1.mga5
+ Revision: 599035
- new version 3.11.91

* Mon Feb 17 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 593863
- new version 3.11.90

* Wed Feb 05 2014 dams <dams> 3.11.5-1.mga5
+ Revision: 583038
- new version 3.11.5

* Wed Feb 05 2014 dams <dams> 3.11.2-1.mga5
+ Revision: 582988
- update %%file
- new version 3.11.2

* Sat Nov 09 2013 ovitters <ovitters> 3.10.1-3.mga4
+ Revision: 550170
- fix url

* Tue Oct 22 2013 umeabot <umeabot> 3.10.1-2.mga4
+ Revision: 542410
- Mageia 4 Mass Rebuild

* Mon Oct 14 2013 ovitters <ovitters> 3.10.1-1.mga4
+ Revision: 497547
- new version 3.10.1

* Mon Sep 23 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 484281
- new version 3.10.0

* Tue Sep 17 2013 ovitters <ovitters> 3.9.92-1.mga4
+ Revision: 480546
- new version 3.9.92

* Wed Aug 21 2013 fwang <fwang> 3.9.90-1.mga4
+ Revision: 468745
- new version 3.9.90
- cleanup spec

* Sun Jun 09 2013 dams <dams> 3.8.1-1.mga4
+ Revision: 440890
- imported package gnome-tetravex

