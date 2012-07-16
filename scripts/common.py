#!/usr/bin/env python
# NOTE: requires python 2.7.

import os
import string
import subprocess

SCRIPT_BASE = os.path.dirname(__file__)

def run(script_name):
    subprocess.check_call(os.path.join(SCRIPT_BASE, script_name), shell=True)

class Config(object):
    def __init__(self):
        with open(os.path.join(SCRIPT_BASE, "..", "config")) as fh:
            for line in fh.readlines():
                key, _, value = line.strip().partition('=')
                setattr(self, key, value)

config = Config()

def write_conf(name, destination, owner="root", group="root", perms="0644"):
    with open(os.path.join(SCRIPT_BASE, "..", "conf", name)) as fh:
        template = string.Template(fh.read())

    with open(destination, 'w') as fh:
        fh.write(template.safe_substitute(config.__dict__))

    subprocess.check_call(["chown", "{0}.{1}".format(owner, group), destination])
    subprocess.check_call(["chmod", perms, destination])
