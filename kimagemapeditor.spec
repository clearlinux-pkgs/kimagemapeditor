#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kimagemapeditor
Version  : 18.08.0
Release  : 1
URL      : https://download.kde.org/stable/applications/18.08.0/src/kimagemapeditor-18.08.0.tar.xz
Source0  : https://download.kde.org/stable/applications/18.08.0/src/kimagemapeditor-18.08.0.tar.xz
Source99 : https://download.kde.org/stable/applications/18.08.0/src/kimagemapeditor-18.08.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: kimagemapeditor-bin
Requires: kimagemapeditor-lib
Requires: kimagemapeditor-data
Requires: kimagemapeditor-license
Requires: kimagemapeditor-locales
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : khtml-dev
BuildRequires : kjs-dev

%description
---------------------------------
KImageMapEditor
An HTML image map editor
Jan SchÃ¤fer

%package bin
Summary: bin components for the kimagemapeditor package.
Group: Binaries
Requires: kimagemapeditor-data
Requires: kimagemapeditor-license

%description bin
bin components for the kimagemapeditor package.


%package data
Summary: data components for the kimagemapeditor package.
Group: Data

%description data
data components for the kimagemapeditor package.


%package doc
Summary: doc components for the kimagemapeditor package.
Group: Documentation

%description doc
doc components for the kimagemapeditor package.


%package lib
Summary: lib components for the kimagemapeditor package.
Group: Libraries
Requires: kimagemapeditor-data
Requires: kimagemapeditor-license

%description lib
lib components for the kimagemapeditor package.


%package license
Summary: license components for the kimagemapeditor package.
Group: Default

%description license
license components for the kimagemapeditor package.


%package locales
Summary: locales components for the kimagemapeditor package.
Group: Default

%description locales
locales components for the kimagemapeditor package.


%prep
%setup -q -n kimagemapeditor-18.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535198276
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535198276
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kimagemapeditor
cp COPYING %{buildroot}/usr/share/doc/kimagemapeditor/COPYING
pushd clr-build
%make_install
popd
%find_lang kimagemapeditor

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kimagemapeditor

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kimagemapeditor.desktop
/usr/share/icons/hicolor/16x16/apps/kimagemapeditor.png
/usr/share/icons/hicolor/22x22/actions/addpoint.png
/usr/share/icons/hicolor/22x22/actions/arrow.png
/usr/share/icons/hicolor/22x22/actions/circle.png
/usr/share/icons/hicolor/22x22/actions/circle2.png
/usr/share/icons/hicolor/22x22/actions/freehand.png
/usr/share/icons/hicolor/22x22/actions/lower.png
/usr/share/icons/hicolor/22x22/actions/polygon.png
/usr/share/icons/hicolor/22x22/actions/raise.png
/usr/share/icons/hicolor/22x22/actions/rectangle.png
/usr/share/icons/hicolor/22x22/actions/removepoint.png
/usr/share/icons/hicolor/32x32/apps/kimagemapeditor.png
/usr/share/icons/hicolor/48x48/apps/kimagemapeditor.png
/usr/share/kimagemapeditor/addpointcursor.png
/usr/share/kimagemapeditor/freehandcursor.png
/usr/share/kimagemapeditor/polygoncursor.png
/usr/share/kimagemapeditor/removepointcursor.png
/usr/share/kservices5/kimagemapeditorpart.desktop
/usr/share/kxmlgui5/kimagemapeditor/kimagemapeditorpartui.rc
/usr/share/kxmlgui5/kimagemapeditor/kimagemapeditorui.rc
/usr/share/metainfo/org.kde.kimagemapeditor.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kimagemapeditor/configure.png
/usr/share/doc/HTML/ca/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/ca/kimagemapeditor/index.docbook
/usr/share/doc/HTML/de/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/de/kimagemapeditor/index.docbook
/usr/share/doc/HTML/en/kimagemapeditor/configure.png
/usr/share/doc/HTML/en/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/en/kimagemapeditor/index.docbook
/usr/share/doc/HTML/en/kimagemapeditor/mainwindow.png
/usr/share/doc/HTML/es/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/es/kimagemapeditor/index.docbook
/usr/share/doc/HTML/et/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/et/kimagemapeditor/index.docbook
/usr/share/doc/HTML/fr/kimagemapeditor/configure.png
/usr/share/doc/HTML/fr/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/fr/kimagemapeditor/index.docbook
/usr/share/doc/HTML/fr/kimagemapeditor/mainwindow.png
/usr/share/doc/HTML/it/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/it/kimagemapeditor/index.docbook
/usr/share/doc/HTML/nl/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/nl/kimagemapeditor/index.docbook
/usr/share/doc/HTML/pl/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/pl/kimagemapeditor/index.docbook
/usr/share/doc/HTML/pt/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/pt/kimagemapeditor/index.docbook
/usr/share/doc/HTML/pt_BR/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kimagemapeditor/index.docbook
/usr/share/doc/HTML/sv/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/sv/kimagemapeditor/index.docbook
/usr/share/doc/HTML/uk/kimagemapeditor/configure.png
/usr/share/doc/HTML/uk/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/uk/kimagemapeditor/index.docbook
/usr/share/doc/HTML/uk/kimagemapeditor/mainwindow.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kimagemapeditor.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/kimagemapeditor/COPYING

%files locales -f kimagemapeditor.lang
%defattr(-,root,root,-)

