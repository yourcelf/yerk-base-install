#!/usr/bin/env python

from common import *

sh("""

apt-get install -y ufw

# Disable ufw while we configure it...
ufw disable

""")
