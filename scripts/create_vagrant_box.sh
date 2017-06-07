#!/bin/bash

if [ ! -d /usr/share/tripleo-image-elements/ ] || ! which disk-image-create; then
    echo "Please install diskimage-builder openstack-tripleo-image-elements"
    exit 1
fi

export SF_KEEP_RELEASE=1
export SF_RELEASE=${SF_RELEASE:-master}
export ELEMENTS_PATH=$(pwd)/elements/:/usr/share/tripleo-image-elements/
# Allow ssh auth via password
export DIB_CLOUD_INIT_ALLOW_SSH_PWAUTH=true

exec disk-image-create -a amd64 -t qcow2 \
    -o $(pwd)/vagrant-${SF_RELEASE}.qcow2 \
    centos-minimal vm cloud-init growroot openssh-server dhcp-all-interfaces selinux-permissive\
    software-factory sf-ci-packages vagrant
