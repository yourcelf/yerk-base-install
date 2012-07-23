#!/usr/bin/env python

from common import *

sh("""

set -e
set -x

apt-get install -y postgresql
""")
