#!/usr/bin/env python

from common import *

sh("""

# IMPORTANT! Do not remove and put above default rule.
ufw allow proto tcp to any port ssh

# Deny by default
ufw default deny

# Allow
ufw allow to any port domain
ufw allow proto tcp to any port http
ufw allow proto tcp to any port https
ufw allow proto tcp to any port smtp
ufw allow proto tcp to any port smtps
ufw allow proto tcp to any port submission
ufw allow proto tcp to any port imaps
ufw allow proto tcp to any port pop3s
ufw allow proto tcp from 18.85.35.209 to any port nrpe
ufw allow proto tcp from 18.85.35.209 to any port munin

# Explicit rejects to be nicer to clients
ufw reject proto tcp to any port imap
ufw reject proto tcp to any port pop3
ufw reject proto tcp to any port ident

""")
