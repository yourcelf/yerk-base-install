#!/usr/bin/env python

import datetime
import grp
import pwd
import os
import string
import subprocess
import sys
import types

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import config

SCRIPT_BASE = os.path.dirname(__file__)

if config.LOGGING:
    LOG_PATH = "/tmp/yerk-install-%s.log" % datetime.datetime.now().strftime('%Y%m%d')
    LOG_FILE = open(LOG_PATH, "a+")

def log(data, append_newline=True):
    if append_newline:
        data = data + "\n"
    sys.stdout.write(data)
    sys.stdout.flush()
    if config.LOGGING:
        LOG_FILE.write(data)

def run(*args):
    proc = subprocess.Popen(args, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    while True:
        data = proc.stdout.readline()
        if data == '':
            break
        log(data, append_newline=False)
    proc.communicate()
    return proc.returncode

def sh(command, with_config=True, exit_on_error=True, print_commands=True, require_success=True):
    if with_config:
        command = interpolate(command)
    if print_commands:
        command = "set -x\n" + command
    if exit_on_error:
        command = "set -e\n" + command
    result = run('/bin/bash', '-c', command)
    if require_success and result != 0:
        log("Exiting on error %d\n" % result)
        sys.exit(result)
    else:
        return result

def script(script_name):
    log("+")
    log("+ Running script %s" % script_name)
    log("+")
    return sh(os.path.join(SCRIPT_BASE, script_name),
        with_config=False, print_commands=False)

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

def write_template(destination, source=None, source_host='common',
                                owner="root", group="root", perms=0644):
    if source is None:
        source = "%s%s" % (source_host, destination)
    log("+")
    log("+ Writing template %s" % source)
    log("+               to %s" % destination)
    log("+               as %s:%s %s" % (owner, group, oct(perms)))
    log("+")

    with open(os.path.join(SCRIPT_BASE, "..", "templates", source)) as fh:
        template = fh.read()

    with open(destination, 'w') as fh:
        os.chmod(destination, perms)
        uid = pwd.getpwnam(owner).pw_uid
        gid = grp.getgrnam(group).gr_gid
        os.chown(destination, uid, gid)
        fh.write(interpolate(template))

    return True
