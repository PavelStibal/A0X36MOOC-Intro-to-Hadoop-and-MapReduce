#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, id, user, time, timezone, method, path, head, status, size = data
        print "{0}\t{1}".format(ip, 1)

