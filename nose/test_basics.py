#!/usr/bin/env python

import sys
from catkintest import *

pwd = os.getcwd()
srcdir = os.path.join(pwd, 'src')
builddir = os.path.join(pwd, 'build')

def setup():
    succeed("rosinstall -n %s test.rosinstall" % srcdir)
    assert exists(srcdir + "/catkin/toplevel.cmake")
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
    out = succeed("cmake %s '-DCATKIN_BUILD_PROJECTS=catkin_test_nolangs' -DCATKIN_LOG=9" % srcdir, cwd=builddir)
    out = succeed("make", cwd=builddir)
    assert exists(builddir + "/catkin_test_nolangs/catkin_test_nolangs_exec")

    
    
