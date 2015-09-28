#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fuse
Version  : 2.9.4
Release  : 13
URL      : http://downloads.sourceforge.net/fuse/fuse-2.9.4.tar.gz
Source0  : http://downloads.sourceforge.net/fuse/fuse-2.9.4.tar.gz
Summary  : Filesystem in Userspace
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: fuse-bin
Requires: fuse-config
Requires: fuse-lib
Requires: fuse-doc
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
Patch1: stateless.patch

%description
General Information
===================
FUSE (Filesystem in Userspace) is a simple interface for userspace
programs to export a virtual filesystem to the Linux kernel.  FUSE
also aims to provide a secure method for non privileged users to
create and mount their own filesystem implementations.

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
%setup -q -n fuse-2.9.4
%patch1 -p1

%build
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fusermount
/usr/bin/mount.fuse
/usr/bin/ulockmgr_server

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/99-fuse.rules

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/fuse/cuse_lowlevel.h
/usr/include/fuse/fuse.h
/usr/include/fuse/fuse_common.h
/usr/include/fuse/fuse_common_compat.h
/usr/include/fuse/fuse_compat.h
/usr/include/fuse/fuse_lowlevel.h
/usr/include/fuse/fuse_lowlevel_compat.h
/usr/include/fuse/fuse_opt.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
