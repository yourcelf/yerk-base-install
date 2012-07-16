#!/usr/bin/env python

from common import write_conf, run

script("hello")
script("hello.py")
write_conf("hello.conf", "/tmp/hello_there.pardner")
