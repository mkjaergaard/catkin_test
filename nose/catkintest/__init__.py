from pexpect import *
from nose.tools import *
from os.path import *
import os

def succeed(cmd, **kwargs):
    print ">>>", cmd, kwargs
    (out, r) = run(cmd, withexitstatus=True, **kwargs)
    if r != 0:
        print "cmd failed: %s\n  result=%u\n  xoutput=%s" % (cmd, r, out)
    return out

