from pexpect import *
from nose.tools import *
from nose.plugins.attrib import attr
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
    this_builddir = builddir
    this_srcdir = builddir
    for k, v in kwargs.items():
        if k == 'cwd':
            this_builddir = v
        elif k == 'srcdir':
            this_srcdir = v
        else:
            args += " '-D%s=%s'" % (k,v)

    cmd = "cmake " + this_srcdir + " " + args
    o = succeed(cmd, cwd=this_builddir)
    assert isfile(this_builddir + "/CMakeCache.txt")
    assert isfile(this_builddir + "/Makefile")
    return o

def assert_exists(prefix, *args):
    for arg in args:
        p = os.path.join(prefix, arg)
        print "Checking for", p
        assert exists(p)

