#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fuse
Version  : 3.2.0
Release  : 18
URL      : https://github.com/libfuse/libfuse/releases/download/fuse-3.2.0/fuse-3.2.0.tar.xzhttps://github.com/libfuse/libfuse/releases/download/fuse-3.2.0/fuse-3.2.0.tar.xz
Source0  : https://github.com/libfuse/libfuse/releases/download/fuse-3.2.0/fuse-3.2.0.tar.xzhttps://github.com/libfuse/libfuse/releases/download/fuse-3.2.0/fuse-3.2.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: fuse-bin
Requires: fuse-config
Requires: fuse-lib
Requires: fuse-doc
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pkgconfig(udev)
BuildRequires : python3
Patch1: build.patch

%description
libfuse
=======
About
-----
FUSE (Filesystem in Userspace) is an interface for userspace programs
to export a filesystem to the Linux kernel. The FUSE project consists
of two components: the *fuse* kernel module (maintained in the regular
kernel repositories) and the *libfuse* userspace library (maintained
in this repository). libfuse provides the reference implementation
for communicating with the FUSE kernel module.

%package bin
Summary: bin components for the fuse package.
Group: Binaries
Requires: fuse-config

%description bin
bin components for the fuse package.


%package config
Summary: config components for the fuse package.
Group: Default

%description config
config components for the fuse package.


%package dev
Summary: dev components for the fuse package.
Group: Development
Requires: fuse-lib
Requires: fuse-bin
Provides: fuse-devel

%description dev
dev components for the fuse package.


%package doc
Summary: doc components for the fuse package.
Group: Documentation

%description doc
doc components for the fuse package.


%package lib
Summary: lib components for the fuse package.
Group: Libraries
Requires: fuse-config

%description lib
lib components for the fuse package.


%prep
%setup -q -n fuse-3.2.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505676350
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain  builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fusermount3
/usr/sbin/mount.fuse3

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/99-fuse3.rules

%files dev
%defattr(-,root,root,-)
/usr/include/fuse3/cuse_lowlevel.h
/usr/include/fuse3/fuse.h
/usr/include/fuse3/fuse_common.h
/usr/include/fuse3/fuse_lowlevel.h
/usr/include/fuse3/fuse_opt.h
/usr/lib64/libfuse3.so
/usr/lib64/pkgconfig/fuse3.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfuse3.so.3
/usr/lib64/libfuse3.so.3.2.0
