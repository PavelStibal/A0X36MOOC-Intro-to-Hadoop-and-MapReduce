#!/usr/bin/python

import sys
from urlparse import urlparse

for line in sys.stdin:
    data = line.strip()
    index1 = data.find("\"")
    index2 = data.rfind("\"")
    if(index1 > 1 and index2 > 2):
        request = line[index1 + 1 : index2]
        url = request.split(" ")[1]
        name = urlparse(url)
        print "{0}\t{1}".format(name.path, 1)
