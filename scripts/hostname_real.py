#!/usr/bin/env python

from common import *

write_conf("real/etc/hosts", "/etc/hosts")
sh("echo real > /etc/hostname")
sh("hostname real")
