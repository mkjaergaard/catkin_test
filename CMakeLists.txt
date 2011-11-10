project(catkin_test)
cmake_minimum_required(VERSION 2.8)
find_package(catkin)
find_package(genmsg)
find_package(std_msgs)
find_package(sensor_msgs)

foreach(subdir
    quux_msgs
    quux_user
    )
  message("catkin_test: ${subdir}")
  add_subdirectory(${subdir})
endforeach()

