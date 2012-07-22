#!/usr/bin/env python

from common import *

write_conf("imaginary/etc/hosts", "/etc/hosts")
sh("echo imaginary > /etc/hostname")
sh("hostname imaginary")
