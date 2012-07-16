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
        # Obtain a list of local environment variables parsed from config file.
        var_list = subprocess.check_output(["bash", "-c",
            "source {0} ; (set -o posix ; set) | grep YERK | uniq".format(
                os.path.join(SCRIPT_BASE, "..", "config")
            )])
        for line in var_list.splitlines():
            if key.startswith("YERK"):
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
