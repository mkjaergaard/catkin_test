cmake_minimum_required(VERSION 2.8)
project(quux_user)

# set(CMAKE_FIND_ROOT_PATH /tmp/sandbox)

find_package(quux_msgs)
include_directories(${quux_msgs_INCLUDE_DIRS})

find_package(rostime)
include_directories(${rostime_INCLUDE_DIRS})

find_package(cpp_common)
include_directories(${cpp_common_INCLUDE_DIRS})

find_package(roscpp_traits)
include_directories(${roscpp_traits_INCLUDE_DIRS})

find_package(roscpp_serialization)
include_directories(${roscpp_serialization_INCLUDE_DIRS})

find_package(sensor_msgs)
include_directories(${sensor_msgs_INCLUDE_DIRS})



# todo: will be set by find_package
include_directories(${std_msgs_INCLUDE_DIRS} ${quux_msgs_INCLUDE_DIRS})

add_executable(quux_user-exec
  src/main.cpp
  )

message(STATUS ${roscpp_serialization_LIBRARIES})

target_link_libraries(quux_user-exec ${roscpp_serialization_LIBRARIES} ${rostime_LIBRARIES})

#add_executable(quux_srv-exec
#  src/srv_test.cpp
#  )

#target_link_libraries(quux_srv-exec ${roscpp_serialization_LIBRARIES})
