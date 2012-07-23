#!/usr/bin/env python

from common import *

sh("""

rsync -avz -e 'ssh -i yerker' \
    yerker@$YERK_DATA_HOST:/home/yerker/yerk-data/ \
    /yerk-data

""")
