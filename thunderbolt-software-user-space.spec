#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : thunderbolt-software-user-space
Version  : 0.9.3
Release  : 15
URL      : https://github.com/intel/thunderbolt-software-user-space/archive/v0.9.3.tar.gz
Source0  : https://github.com/intel/thunderbolt-software-user-space/archive/v0.9.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: thunderbolt-software-user-space-bin = %{version}-%{release}
Requires: thunderbolt-software-user-space-config = %{version}-%{release}
Requires: thunderbolt-software-user-space-data = %{version}-%{release}
Requires: thunderbolt-software-user-space-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : pkgconfig(udev)
Patch1: build.patch

%description
Provides user-space components that implement device approval support:
1. Easier interaction with the kernel module for approving connected devices.
2. ACL for auto-approving devices white-listed by the user.

%package bin
Summary: bin components for the thunderbolt-software-user-space package.
Group: Binaries
Requires: thunderbolt-software-user-space-data = %{version}-%{release}
Requires: thunderbolt-software-user-space-config = %{version}-%{release}
Requires: thunderbolt-software-user-space-license = %{version}-%{release}

%description bin
bin components for the thunderbolt-software-user-space package.


%package config
Summary: config components for the thunderbolt-software-user-space package.
Group: Default

%description config
config components for the thunderbolt-software-user-space package.


%package data
Summary: data components for the thunderbolt-software-user-space package.
Group: Data

%description data
data components for the thunderbolt-software-user-space package.


%package doc
Summary: doc components for the thunderbolt-software-user-space package.
Group: Documentation

%description doc
doc components for the thunderbolt-software-user-space package.


%package license
Summary: license components for the thunderbolt-software-user-space package.
Group: Default

%description license
license components for the thunderbolt-software-user-space package.


%prep
%setup -q -n thunderbolt-software-user-space-0.9.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545592362
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1545592362
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/thunderbolt-software-user-space
cp COPYING %{buildroot}/usr/share/package-licenses/thunderbolt-software-user-space/COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib/udev/tbtacl
/usr/lib/udev/tbtacl-write
/usr/lib/udev/tbtxdomain

%files bin
%defattr(-,root,root,-)
/usr/bin/tbtadm

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/60-tbtacl.rules
/usr/lib/udev/rules.d/60-tbtxdomain.rules

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/tbtadm

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/thunderbolt-user-space/copyright

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/thunderbolt-software-user-space/COPYING
