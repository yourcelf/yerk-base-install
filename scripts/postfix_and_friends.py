#!/usr/bin/env python

from common import *

sh("""

apt-get install postfix dovecot-imapd dovecot-pop3 maildrop libsas12-modules libsas12-modules-sql libmail-spf-query-perl

# TODO: configure postgrey, ala /wiki/HowTo/SetupSpamProtection

""")
