#!/usr/bin/env python

from common import *

sh("""

set -e
set -x

apt-get install -y apache2 php5 libapache2-mod-php5
""")
