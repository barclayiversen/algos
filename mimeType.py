# This algo kicked my ass and I never did finish it. From codingame this algo is supposed to take a list of files
# and return their mime types. 

import sys
import math
import os
import re
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())  # Number of elements which make up the association table.
q = int(raw_input())  # Number Q of file names to be analyzed.

mime_types = {}
for i in xrange(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = raw_input().split()

    mime_types[ext] = mt

# print mime_types

for i in xrange(q):
    unknown = 1
    fname = raw_input()  # One file name per line.
    print >> sys.stderr, 'fname = ', fname
    fname, extension = os.path.splitext(fname)
    print >> sys.stderr, 'EXTENSION =', extension
    extension = re.sub(r"\.",'', extension)
    # print >> sys.stderr, 'EXTENSION =', extension
    if(extension == ""):
        # print "UNKNOWN"
        unknown = 0
    for key, value in mime_types.items():
        if(key == extension):
            unknown = 0
            # print "value = ", value
            
    # if(unknown == 1):
    #     print "UNKNOWN"
# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
# print "UNKNOWN"
