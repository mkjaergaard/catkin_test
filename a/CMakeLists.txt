cmake_minimum_required(VERSION 2.8)
project(a)
find_package(catkin)

add_library(a SHARED lib.cpp)

install_cmake_infrastructure(a
  VERSION 0.0.1
  INCLUDE_DIRS include
  LIBRARIES a
  )