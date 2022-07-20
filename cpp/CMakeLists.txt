cmake_minimum_required(VERSION 3.22)
project(cpp)

set(CMAKE_CXX_STANDARD 17)

add_executable(E01A_pattern_count ch01/E01A_pattern_count.cpp utils.cpp)
add_executable(E01B_frequent_words ch01/E01A_pattern_count.cpp ch01/E01B_frequent_words.cpp utils.cpp)


