#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-hyperscan-soname4
Version  : 4.7.0
Release  : 4
URL      : https://github.com/intel/hyperscan/archive/v4.7.0.tar.gz
Source0  : https://github.com/intel/hyperscan/archive/v4.7.0.tar.gz
Summary  : Intel(R) Hyperscan Library
Group    : Development/Tools
License  : BSD-3-Clause Intel
Requires: compat-hyperscan-soname4-lib
Requires: compat-hyperscan-soname4-license
BuildRequires : Sphinx
BuildRequires : boost-dev
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : python3-dev
BuildRequires : ragel
BuildRequires : sqlite-autoconf-dev

%description
# Hyperscan
Hyperscan is a high-performance multiple regex matching library. It follows the
regular expression syntax of the commonly-used libpcre library, but is a
standalone library with its own C API.

%package dev
Summary: dev components for the compat-hyperscan-soname4 package.
Group: Development
Requires: compat-hyperscan-soname4-lib
Provides: compat-hyperscan-soname4-devel

%description dev
dev components for the compat-hyperscan-soname4 package.


%package doc
Summary: doc components for the compat-hyperscan-soname4 package.
Group: Documentation

%description doc
doc components for the compat-hyperscan-soname4 package.


%package lib
Summary: lib components for the compat-hyperscan-soname4 package.
Group: Libraries
Requires: compat-hyperscan-soname4-license

%description lib
lib components for the compat-hyperscan-soname4 package.


%package license
Summary: license components for the compat-hyperscan-soname4 package.
Group: Default

%description license
license components for the compat-hyperscan-soname4 package.


%prep
%setup -q -n hyperscan-4.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531148703
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1531148703
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/compat-hyperscan-soname4
cp LICENSE %{buildroot}/usr/share/doc/compat-hyperscan-soname4/LICENSE
cp COPYING %{buildroot}/usr/share/doc/compat-hyperscan-soname4/COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/hs/hs.h
%exclude /usr/include/hs/hs_common.h
%exclude /usr/include/hs/hs_compile.h
%exclude /usr/include/hs/hs_runtime.h
%exclude /usr/lib64/libhs.so
%exclude /usr/lib64/libhs_runtime.so
%exclude /usr/lib64/pkgconfig/libhs.pc

%files doc
%defattr(0644,root,root,0755)
%exclude /usr/share/doc/hyperscan/examples/README.md
%exclude /usr/share/doc/hyperscan/examples/patbench.cc
%exclude /usr/share/doc/hyperscan/examples/pcapscan.cc
%exclude /usr/share/doc/hyperscan/examples/simplegrep.c

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhs.so.4
/usr/lib64/libhs.so.4.7.0
/usr/lib64/libhs_runtime.so.4
/usr/lib64/libhs_runtime.so.4.7.0

%files license
%defattr(-,root,root,-)
%exclude /usr/share/doc/compat-hyperscan-soname4/COPYING
%exclude /usr/share/doc/compat-hyperscan-soname4/LICENSE
