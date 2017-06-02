#!/bin/bash

[ -d /usr/share/tripleo-image-elements/ ] || sudo yum install -y openstack-tripleo-image-elements

export SF_KEEP_RELEASE=1
export SF_RELEASE=master
export ELEMENTS_PATH=$(pwd)/elements/:/usr/share/tripleo-image-elements/

exec disk-image-create -a amd64 -t qcow2 \
    -o ~/sf-${SF_RELEASE}.qcow2 \
    centos-minimal vm cloud-init growroot openssh-server dhcp-all-interfaces \
    software-factory

#    os-apply-config os-cloud-config os-collect-config os-net-config os-refresh-config
