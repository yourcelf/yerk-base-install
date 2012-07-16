#!/usr/bin/env python

import os
import string
import subprocess
import sys
import types

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import config

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
        sys.stdout.flush()
        if LOGGING:
            log_file.write(data)
            log_file.flush()
    proc.communicate()

    if LOGGING:
        log_file.close
    return proc.returncode

def sh(command, with_config=True):
    if with_config:
        command = interpolate(command)
    return run('/bin/bash', '-c', command)

def script(script_name):
    return sh(os.path.join(SCRIPT_BASE, script_name), with_config=False)

def config_dict():
    dct = {}
    for name in dir(config):
        if not name.startswith("_"):
            value = getattr(config, name)
            if type(value) != types.ModuleType:
                dct[name] = value
    return dct

def interpolate(template):
    return string.Template(template).safe_substitute(config_dict())

def write_conf(name, destination, owner="root", group="root", perms="0644"):
    with open(os.path.join(SCRIPT_BASE, "..", "templates", name)) as fh:
        template = fh.read()

    with open(destination, 'w') as fh:
        fh.write(interpolate(template))

    subprocess.check_call(["chown", "{0}.{1}".format(owner, group), destination])
    subprocess.check_call(["chmod", perms, destination])
