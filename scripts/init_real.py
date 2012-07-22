#!/usr/bin/env python

from common import *

script("system_update.py")

script("firewall_1_install.py")
script("firewall_3_configure_real.py")
script("firewall_5_finalize.py")
