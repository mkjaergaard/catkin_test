from pexpect import *
from nose.tools import *
from os.path import *
import os

pwd = os.getcwd()
srcdir = os.path.join(pwd, 'src')
builddir = os.path.join(pwd, 'build')

def succeed(cmd, **kwargs):
    print ">>>", cmd, kwargs
    (out, r) = run(cmd, withexitstatus=True, **kwargs)
    print "<<<", out
    if r != 0:
        print "cmd failed: %s\n  result=%u\n  output=\n%s" % (cmd, r, out)
        assert r == 0
    return out

def has_cmakecache():
    assert isfile(builddir + "/CMakeCache.txt")

def cmake(**kwargs):
    args = ''
    for k, v in kwargs.items():
        args += " '-D%s=%s'" % (k,v)
    cmd = "cmake " + srcdir + " " + args
    o = succeed(cmd, cwd=builddir)
    assert isfile(builddir + "/CMakeCache.txt")
    assert isfile(builddir + "/Makefile")
    return o

