#!/usr/bin/env python

import sys
from catkintest import *

def setup():
    print "***************************************************************\n"*8
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

bt = with_setup(startbuild, endbuild)


@bt
# @attr('this')
def test_00():
    out = cmake(CMAKE_INSTALL_PREFIX=cmake_install_prefix)
    assert exists(builddir + "/catkin_test_nolangs")
    assert exists(builddir + "/genmsg")
    assert exists(builddir + "/common_msgs")
    out = succeed("make", cwd=builddir)
    assert exists(builddir + "/catkin_test_nolangs/catkin_test_nolangs_exec")

    out = succeed("make install DESTDIR=%s" % destdir, cwd=builddir)
    prefix = "%s/%s/%s" % (builddir, destdir, cmake_install_prefix)

    assert_exists(diskprefix,
                  "bin/catkin_test_nolangs_exec",
                  "include/std_msgs/String.h",
                  "lib/python/sensor_msgs/_PointCloud2.py",
                  "share/msg/std_msgs/String.msg",
                  "share/cmake/std_msgs/std_msgs-config.cmake",
                  "share/cmake/std_msgs/std_msgs-config-version.cmake",
                  "lib/libcpp_common.so"
                  )

@bt
def test_01():
    out = cmake(CATKIN_BUILD_PROJECTS='catkin_test_nolangs',
                CMAKE_INSTALL_PREFIX=cmake_install_prefix)
    assert exists(builddir + "/catkin_test_nolangs")
    assert not exists(builddir + "/std_msgs")
    assert not exists(builddir + "/genmsg")
    out = succeed("make", cwd=builddir)
    assert exists(builddir + "/catkin_test_nolangs/catkin_test_nolangs_exec")
    out = succeed("make install DESTDIR=%s" % destdir, cwd=builddir)

    assert_exists(diskprefix,
                  "bin/catkin_test_nolangs_exec",
                  "share/cmake/catkin_test_nolangs/catkin_test_nolangs-config.cmake")


#
# This one needs love:  catkin looks in wrong directory for buildable projects
#
#@attr('this')
#def test_as_subdirectory():
#    succeed("rosinstall -n subdir_src/src test.rosinstall")
#    succeed("rm -rf subdir_build")
#    succeed("mkdir subdir_build")
#    cmake(this_srcdir="subdir_src", cwd="subdir_build")





# @with_setup(startbuild, endbuild)
# def test_01():
#     out = cmake()
#
#     out = succeed("make", cwd=builddir)
#     print "OUT=", out
#     assert exists(builddir + "/catkin_test_nolangs/catkin_test_nolangs_exec")



