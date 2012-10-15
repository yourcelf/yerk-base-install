#!/usr/bin/env python

from common import *

sh("apt-get install -y unattended-upgrades")
write_template("/etc/apt/apt.conf.d/20auto-upgrades")
write_template("/etc/apt/apt.conf.d/50unattended-upgrades")
