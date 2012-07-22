#!/usr/bin/env python

from common import *

sh("""

# --force disables prompting if on an ssh session
ufw --force enable

""")
