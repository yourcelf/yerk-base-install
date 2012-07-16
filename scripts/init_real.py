#!/usr/bin/env python

from common import *

sh('echo "$YERK_HELLO"')
script("hello.py")
write_conf("hello.conf", "/tmp/hello_there.pardner")
