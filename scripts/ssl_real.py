#!/usr/bin/env python

from common import *

write_template("/etc/ssl/certs/positive-ssl-chain.crt")
write_template("/etc/ssl/certs/mail.yerk.org.crt")
write_template("/etc/ssl/private/mail.yerk.org.key", perms="0600")

sh("""

cd /etc/ssl/certs
cat mail.yerk.org.crt positive-ssl-chain.crt > mail.yerk.org-with-chain.crt

""")
