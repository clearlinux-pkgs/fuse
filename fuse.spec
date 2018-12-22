#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD113FCAC3C4E599F (Nikolaus@rath.org)
#
Name     : fuse
Version  : 3.4.1
Release  : 29
URL      : https://github.com/libfuse/libfuse/releases/download/fuse-3.4.1/fuse-3.4.1.tar.xz
Source0  : https://github.com/libfuse/libfuse/releases/download/fuse-3.4.1/fuse-3.4.1.tar.xz
Source99 : https://github.com/libfuse/libfuse/releases/download/fuse-3.4.1/fuse-3.4.1.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: fuse-bin = %{version}-%{release}
Requires: fuse-config = %{version}-%{release}
Requires: fuse-lib = %{version}-%{release}
Requires: fuse-license = %{version}-%{release}
Requires: fuse-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : systemd-dev
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
Requires: fuse-config = %{version}-%{release}
Requires: fuse-license = %{version}-%{release}
Requires: fuse-man = %{version}-%{release}

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
Requires: fuse-lib = %{version}-%{release}
Requires: fuse-bin = %{version}-%{release}
Provides: fuse-devel = %{version}-%{release}

%description dev
dev components for the fuse package.


%package lib
Summary: lib components for the fuse package.
Group: Libraries
Requires: fuse-license = %{version}-%{release}

%description lib
lib components for the fuse package.


%package license
Summary: license components for the fuse package.
Group: Default

%description license
license components for the fuse package.


%package man
Summary: man components for the fuse package.
Group: Default

%description man
man components for the fuse package.


%prep
%setup -q -n fuse-3.4.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545507664
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/fuse
cp GPL2.txt %{buildroot}/usr/share/package-licenses/fuse/GPL2.txt
DESTDIR=%{buildroot} ninja -C builddir install
## install_append content
ln -s /usr/bin/fusermount3 %{buildroot}/usr/bin/fusermount
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fusermount
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfuse3.so.3
/usr/lib64/libfuse3.so.3.4.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fuse/GPL2.txt

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fusermount3.1
/usr/share/man/man8/mount.fuse3.8
