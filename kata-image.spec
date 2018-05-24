Name     : kata-image
Version  : 0.3.0
Release  : 1
URL      : https://github.com/kata-containers/agent
Source0  : https://github.com/kata-containers/agent/releases/download/0.3.0/kata-containers.tar.gz
Summary  : Kata Containers image
Group    : Image
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause ISC MIT MPL-2.0-no-copyleft-exception

%description
Kata Containers image

%prep
%setup -c -n kata-containers

%install
ImageDir=%{buildroot}/usr/share/kata-containers

mkdir -p ${ImageDir}
install -p kata-containers-image_clearlinux_agent_e444fe2.img ${ImageDir}/kata-containers-image_clearlinux_agent_e444fe2.img
ln -sf kata-containers-image_clearlinux_agent_e444fe2.img ${ImageDir}/kata-containers.img
install -p kata-containers-initrd_alpine_agent_e444fe2.initrd ${ImageDir}/kata-containers-initrd_alpine_agent_e444fe2.initrd
ln -sf kata-containers-initrd_alpine_agent_e444fe2.initrd ${ImageDir}/kata-containers-initrd.img

%files
/usr/share/kata-containers/kata-containers.img
/usr/share/kata-containers/kata-containers-initrd.img
/usr/share/kata-containers/kata-containers-image_clearlinux_agent_e444fe2.img
/usr/share/kata-containers/kata-containers-initrd_alpine_agent_e444fe2.initrd
