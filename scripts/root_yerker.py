#!/usr/bin/env python

from common import *

sh("mkdir -p -m 700 /root/.ssh")

write_template("/root/.ssh/yerker", perms=0600)
write_template("/root/.ssh/yerker.pub")
