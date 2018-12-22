Name     : kata-image
Version  : 1.5.0.rc2
Release  : 10
URL      : https://github.com/kata-containers/agent
Source0  : https://github.com/kata-containers/agent/releases/download/1.5.0-rc2/kata-containers-1.5.0-rc2-91a87bc7176-x86_64.tar.gz
Summary  : Kata Containers image
Group    : Image
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause ISC MIT MPL-2.0-no-copyleft-exception

%define agent_commit 91a87bc7176
%define version 1.5.0-rc2

%description
Kata Containers image

%prep
%setup -c -n kata-containers

%install
ImageDir=%{buildroot}/usr/share/kata-containers

mkdir -p ${ImageDir}
install -p kata-containers-image_clearlinux_%{version}_agent_%{agent_commit}.img ${ImageDir}/kata-containers-image_clearlinux_%{version}_agent_%{agent_commit}.img
ln -sf kata-containers-image_clearlinux_%{version}_agent_%{agent_commit}.img ${ImageDir}/kata-containers.img
install -p kata-containers-initrd_alpine_%{version}_agent_%{agent_commit}.initrd ${ImageDir}/kata-containers-initrd_alpine_%{version}_agent_%{agent_commit}.initrd
ln -sf kata-containers-initrd_alpine_%{version}_agent_%{agent_commit}.initrd ${ImageDir}/kata-containers-initrd.img

%files
/usr/share/kata-containers/kata-containers.img
/usr/share/kata-containers/kata-containers-initrd.img
/usr/share/kata-containers/kata-containers-image_clearlinux_%{version}_agent_%{agent_commit}.img
/usr/share/kata-containers/kata-containers-initrd_alpine_%{version}_agent_%{agent_commit}.initrd
