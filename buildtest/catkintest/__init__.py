from pexpect import *
from nose.tools import *
from nose.plugins.attrib import attr
from os.path import *
import os
import shutil

pwd = os.getcwd()
srcdir = os.path.join(pwd, 'src/test.rosinstall')
builddir = os.path.join(pwd, 'build/test.rosinstall')
destdir='DESTDIR'
cmake_install_prefix='/CMAKE_INSTALL_PREFIX'
diskprefix="%s/%s/%s" % (builddir, destdir, cmake_install_prefix)

def succeed(cmd, **kwargs):
    print ">>>", cmd, kwargs
    (out, r) = run(cmd, withexitstatus=True, **kwargs)
    print "<<<", out
    if r != 0:
        print "cmd failed: %s\n  result=%u\n  output=\n%s" % (cmd, r, out)
        assert r == 0
    return out

def fail(cmd, **kwargs):
    print ">>>", cmd, kwargs
    (out, r) = run(cmd, withexitstatus=True, **kwargs)
    print "<<<", out
    if r == 0:
        print "cmd failed: %s\n  result=%u\n  output=\n%s" % (cmd, r, out)
        assert r != 0
    return out

def has_cmakecache():
    assert isfile(builddir + "/CMakeCache.txt")

def cmake(**kwargs):
    args = ''
    this_builddir = builddir
    this_srcdir = srcdir
    expect = succeed
    print "v~_", this_builddir, this_srcdir
    for k, v in kwargs.items():
        print "~v^v~", k, v
        if k == 'cwd':
            this_builddir = v
        elif k == 'srcdir':
            this_srcdir = v
        elif k == 'expect':
            print "USING EXPECT=", v
            expect = v
        else:
            args += " '-D%s=%s'" % (k,v)

    if not isdir(this_builddir):
        os.makedirs(this_builddir)
    cmd = "cmake " + this_srcdir + " " + args
    o = expect(cmd, cwd=this_builddir)
    if (expect == succeed):
        assert isfile(this_builddir + "/CMakeCache.txt")
        assert isfile(this_builddir + "/Makefile")
    return o

def assert_exists(prefix, *args):
    for arg in args:
        p = os.path.join(prefix, arg)
        print "Checking for", p
        assert exists(p), "%s doesn't exist" % p


