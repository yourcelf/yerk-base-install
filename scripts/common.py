#!/usr/bin/env python
# NOTE: requires python 2.7.

import os
import string
import subprocess
import sys

LOGGING = False
LOG_PATH = None
SCRIPT_BASE = os.path.dirname(__file__)

def run(*args):
    if LOGGING:
        log_file = open(LOG_PATH, "w")
    proc = subprocess.Popen(args, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    while True:
        data = proc.stdout.readline()
        if data == '':
            break
        sys.stdout.write(data)
        if LOGGING:
            log_file.write(data)
    proc.communicate()
    if LOGGING:
        log_file.close
    return proc.returncode

def sh(commands):
    return run('/bin/bash', '-c', commands)

def script(script_name):
    return sh(os.path.join(SCRIPT_BASE, script_name))

class Config(object):
    def __init__(self):
        # Obtain a list of local environment variables parsed from config file.
        var_list = subprocess.check_output(["bash", "-c",
            "source {0} ; (set -o posix ; set) | grep YERK | uniq".format(
                os.path.join(SCRIPT_BASE, "..", "config.py")
            )])
        for line in var_list.splitlines():
            if line.startswith("YERK"):
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
