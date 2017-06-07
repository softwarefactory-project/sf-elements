#!/usr/bin/env python

import argparse
import requests
import os
import tarfile


REQUEST_URL = "https://atlas.hashicorp.com/api/v1/box/%(box)s/version/%(version)s/provider/libvirt/upload?access_token=%(token)s"


def create_archive(img_path):
    pass


def check_version(token, box, version):
    pass


def upload_box(token, box, version):
    pass


def main(img_path, token, box, version):
    create_archive(img_path)
    check_version(token, box, version)
    upload_box(token, box, version)


if __name__ == "__main__":
    print "just a stub"
