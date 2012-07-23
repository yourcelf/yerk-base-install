#!/usr/bin/env python

from common import *

sh("""

adduser --system --no-create-home --disabled-login --shell /bin/false dnslog
adduser --system --no-create-home --disabled-login --shell /bin/false tinydns

rm -rf /etc/tinydns
tinydns-conf tinydns dnslog /etc/tinydns $REAL_IP_ADDRESS
rm -rf /var/log/tinydns
mv /etc/tinydns/log /var/log/tinydns
ln -s /var/log/tinydns /etc/tinydns/log
ln -sf /etc/tinydns /etc/service/tinydns

""")
