#!/usr/bin/env python

from common import *

sh("""

adduser --system --no-create-home --disabled-login --shell /bin/false dnslog
adduser --system --no-create-home --disabled-login --shell /bin/false tinydns

""")
