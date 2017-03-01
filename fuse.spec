#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fuse
Version  : 3.0.0
Release  : 16
URL      : https://github.com/libfuse/libfuse/releases/download/fuse-3.0.0/fuse-3.0.0.tar.gz
Source0  : https://github.com/libfuse/libfuse/releases/download/fuse-3.0.0/fuse-3.0.0.tar.gz
Summary  : Filesystem in Userspace
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
Patch1: stateless.patch

%description
libfuse
=======
Warning: unresolved security issue
----------------------------------

%prep
%setup -q -n fuse-3.0.0
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488410456
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1488410456
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
