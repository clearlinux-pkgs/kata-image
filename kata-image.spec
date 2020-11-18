Name     : kata-image
Version  : 1.10.8
Release  : 23
URL      : https://github.com/kata-containers/runtime
Source0  : https://github.com/kata-containers/runtime/releases/download/1.10.8/kata-static-1.10.8-x86_64.tar.xz
Summary  : Kata Containers image
Group    : Image
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause ISC MIT MPL-2.0-no-copyleft-exception

%define agent_commit 6c036c5e52
%define version 1.10.8

%description
Kata Containers image

%prep
%setup -c -n kata-containers

%install
ImageDir=%{buildroot}/usr/share/kata-containers

mkdir -p ${ImageDir}
install -p opt/kata/share/kata-containers/kata-containers-image_clearlinux_%{version}_agent_%{agent_commit}.img ${ImageDir}/kata-containers-image_clearlinux_%{version}_agent_%{agent_commit}.img
ln -sf kata-containers-image_clearlinux_%{version}_agent_%{agent_commit}.img ${ImageDir}/kata-containers.img
install -p opt/kata/share/kata-containers/kata-containers-initrd_alpine_%{version}_agent_%{agent_commit}.initrd ${ImageDir}/kata-containers-initrd_alpine_%{version}_agent_%{agent_commit}.initrd
ln -sf kata-containers-initrd_alpine_%{version}_agent_%{agent_commit}.initrd ${ImageDir}/kata-containers-initrd.img

%files
/usr/share/kata-containers/kata-containers.img
/usr/share/kata-containers/kata-containers-initrd.img
/usr/share/kata-containers/kata-containers-image_clearlinux_%{version}_agent_%{agent_commit}.img
/usr/share/kata-containers/kata-containers-initrd_alpine_%{version}_agent_%{agent_commit}.initrd
