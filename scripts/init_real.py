#!/usr/bin/env python

from common import *

script("ssh.py")
script("hostname_real.py")
script("system_datetime.py")

script("firewall_1_install.py")
script("firewall_2_prepare.py")
script("firewall_3_configure_real.py")
script("firewall_5_finalize.py")

script("vagrant_grub_pc.py")
script("system_update.py")
script("unattended_upgrades.py")

script("sudoers.py")

script("dns_1_install.py")
script("dns_2_prepare.py")
script("dns_3_configure.py")

script("ssl_real.py")

script("postgres_1_install.py")
script("postgres_2_configure.py")

script("apache_real_1_install.py")
script("apache_real_2_configure.py")
