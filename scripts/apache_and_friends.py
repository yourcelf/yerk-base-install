#!/usr/bin/env python

from common import *

sh("""

set -e
set -x

apt-get install apache2 php5 libapache2-mod-php5 libapache2-mod-wsgi postgresql

# TODO: fix pg_hba.conf to allow password auth.

""")
