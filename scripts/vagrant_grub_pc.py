#!/usr/bin/env python

import sys
import os.path
from common import *

# This is a hack to make grub-pc work with vagrant.

if not os.path.exists("/home/vagrant"):
    sys.exit(0)

sh("""

apt-get install -y debconf-utils
echo "grub-pc grub-pc/install_devices multiselect /dev/sda" | debconf-set-selections

""")

