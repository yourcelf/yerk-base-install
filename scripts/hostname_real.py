#!/usr/bin/env python

from common import *

write_template("/etc/hosts", source_host="real")
sh("echo real > /etc/hostname")
sh("hostname real")
