#!/usr/bin/env python

from common import *

write_template("/etc/hosts", source_host="imaginary")
sh("echo imaginary > /etc/hostname")
sh("hostname imaginary")
