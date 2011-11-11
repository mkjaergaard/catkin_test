#!/usr/bin/env python

import sys
from catkintest import *

def setup():
    succeed("rosinstall -n %s test.rosinstall" % srcdir)
    assert exists(srcdir + "/catkin/toplevel.cmake")
    succeed("rm -f CMakeLists.txt", cwd=srcdir)
    succeed("ln -s catkin/toplevel.cmake CMakeLists.txt", cwd=srcdir)

def startbuild():
    succeed("rm -rf %s" % builddir)
    succeed("mkdir %s" % builddir)

def endbuild():
    pass

def teardown():
    #res = run("rm -rf sandbox")
    pass
    
@with_setup(startbuild, endbuild)
def test_00():
    out = cmake(CATKIN_BUILD_PROJECTS='catkin_test_nolangs')
    assert exists(builddir + "/catkin_test_nolangs")
    out = succeed("make", cwd=builddir)
    assert exists(builddir + "/catkin_test_nolangs/catkin_test_nolangs_exec")

@with_setup(startbuild, endbuild)
def test_01():
    out = cmake()
    
    out = succeed("make", cwd=builddir)
    print "OUT=", out
    assert exists(builddir + "/catkin_test_nolangs/catkin_test_nolangs_exec")

    
    
