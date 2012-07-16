#!/usr/bin/env python

from common import *

script("system_update.py")

script("install_firewall.py")
script("configure_firewall_real.py")
script("finalize_firewall.py")
