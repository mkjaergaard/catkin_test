project(catkin_test)
cmake_minimum_required(VERSION 2.8)
find_package(catkin REQUIRED)
find_package(genmsg REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)

foreach(subdir
    quux_msgs
    quux_user
    a
    b
    )
  add_subdirectory(${subdir})
endforeach()

