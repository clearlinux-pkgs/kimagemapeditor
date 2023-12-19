#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kimagemapeditor
Version  : 23.08.4
Release  : 64
URL      : https://download.kde.org/stable/release-service/23.08.4/src/kimagemapeditor-23.08.4.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.4/src/kimagemapeditor-23.08.4.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.4/src/kimagemapeditor-23.08.4.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: kimagemapeditor-bin = %{version}-%{release}
Requires: kimagemapeditor-data = %{version}-%{release}
Requires: kimagemapeditor-lib = %{version}-%{release}
Requires: kimagemapeditor-license = %{version}-%{release}
Requires: kimagemapeditor-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qtwebengine-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
---------------------------------
KImageMapEditor
An HTML image map editor
Jan Schäfer

%package bin
Summary: bin components for the kimagemapeditor package.
Group: Binaries
Requires: kimagemapeditor-data = %{version}-%{release}
Requires: kimagemapeditor-license = %{version}-%{release}

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
Requires: kimagemapeditor-data = %{version}-%{release}
Requires: kimagemapeditor-license = %{version}-%{release}

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
%setup -q -n kimagemapeditor-23.08.4
cd %{_builddir}/kimagemapeditor-23.08.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702968963
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1702968963
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kimagemapeditor
cp %{_builddir}/kimagemapeditor-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kimagemapeditor/2d69f4c601571117df29fd61c2ce9117b0879da7 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kimagemapeditor
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kimagemapeditor
/usr/bin/kimagemapeditor

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kimagemapeditor.desktop
/usr/share/icons/hicolor/128x128/apps/kimagemapeditor.png
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
/usr/share/icons/hicolor/22x22/apps/kimagemapeditor.png
/usr/share/icons/hicolor/32x32/apps/kimagemapeditor.png
/usr/share/icons/hicolor/48x48/apps/kimagemapeditor.png
/usr/share/icons/hicolor/64x64/apps/kimagemapeditor.png
/usr/share/icons/hicolor/scalable/apps/kimagemapeditor.svgz
/usr/share/kimagemapeditor/addpointcursor.png
/usr/share/kimagemapeditor/freehandcursor.png
/usr/share/kimagemapeditor/polygoncursor.png
/usr/share/kimagemapeditor/removepointcursor.png
/usr/share/kservices5/kimagemapeditorpart.desktop
/usr/share/metainfo/org.kde.kimagemapeditor.appdata.xml
/usr/share/qlogging-categories5/kimagemapeditor.categories

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
/usr/share/doc/HTML/ko/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/ko/kimagemapeditor/index.docbook
/usr/share/doc/HTML/nl/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/nl/kimagemapeditor/index.docbook
/usr/share/doc/HTML/pl/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/pl/kimagemapeditor/index.docbook
/usr/share/doc/HTML/pt/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/pt/kimagemapeditor/index.docbook
/usr/share/doc/HTML/pt_BR/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kimagemapeditor/index.docbook
/usr/share/doc/HTML/ru/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/ru/kimagemapeditor/index.docbook
/usr/share/doc/HTML/sv/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/sv/kimagemapeditor/index.docbook
/usr/share/doc/HTML/uk/kimagemapeditor/configure.png
/usr/share/doc/HTML/uk/kimagemapeditor/index.cache.bz2
/usr/share/doc/HTML/uk/kimagemapeditor/index.docbook
/usr/share/doc/HTML/uk/kimagemapeditor/mainwindow.png

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt5/plugins/kf5/parts/kimagemapeditorpart.so
/usr/lib64/qt5/plugins/kf5/parts/kimagemapeditorpart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kimagemapeditor/2d69f4c601571117df29fd61c2ce9117b0879da7

%files locales -f kimagemapeditor.lang
%defattr(-,root,root,-)

