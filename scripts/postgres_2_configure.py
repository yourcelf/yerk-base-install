#!/usr/bin/env python
from common import *

write_template("/etc/postgresql/9.1/main/pg_hba.conf", owner="postgres", group="postgres", perms="0640")
