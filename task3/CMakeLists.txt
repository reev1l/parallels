cmake_minimum_required(VERSION 3.15)

project(task3)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Threads REQUIRED)

add_executable(task3_1)
add_executable(task3_2)

target_sources(task3_1 PRIVATE task3_1/task3_1.cpp)

target_sources(task3_2 PRIVATE task3_2/task3_2.cpp)

target_link_libraries(task3_1 PRIVATE Threads::Threads)
target_link_libraries(task3_2 PRIVATE Threads::Threads)