cmake_minimum_required(VERSION 2.8)
project(b)

find_package(catkin)
find_package(a)
include_directories(${a_INCLUDE_DIRS})

add_library(b SHARED lib.cpp)
target_link_libraries(b ${a_LIBRARIES})

install_cmake_infrastructure(b
  VERSION 0.0.1
  INCLUDE_DIRS include
  LIBRARIES b
  )