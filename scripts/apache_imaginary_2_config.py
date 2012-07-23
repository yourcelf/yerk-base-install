#!/usr/bin/env python
from common import sh

sh("""

set -x
set -e

rm -rf /etc/apache2/sites-enabled/
rm -rf /etc/apache2/sites-available/
rm -rf /etc/apache2/sites-includes/

ln -s /yerk-data/etc/apache2/sites-enabled/ /etc/apache2/sites-enabled/
ln -s /yerk-data/etc/apache2/sites-available/ /etc/apache2/sites-available/
ln -s /yerk-data/etc/apache2/site-includes/ /etc/apache2/site-includes/

a2enmod headers
a2enmod ssl
a2enmod dav
a2enmod dav_fs
a2enmod proxy
a2enmod proxy_connect

/etc/init.d/apache2 restart
""")
