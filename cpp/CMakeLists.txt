cmake_minimum_required(VERSION 3.22)
project(cpp)

set(CMAKE_CXX_STANDARD 17)

# ---------- EXERCISES ----------
# CHAPTER 1
add_executable(E01A_pattern_count
        ch01/E01A_pattern_count.cpp
        utils.cpp)

add_executable(E01B_frequent_words
        ch01/E01B_frequent_words.cpp
        ch01/E01A_pattern_count.cpp
        utils.cpp)

add_executable(E01C_reverse_complement
        ch01/E01C_reverse_complement.cpp
        utils.cpp)

add_executable(E01D_pattern_matching
        ch01/E01D_pattern_matching.cpp
        ch01/E01A_pattern_count.cpp
        ch01/E01C_reverse_complement.cpp
        utils.cpp)

add_executable(E01E_clump_finding
        ch01/E01E_clump_finding.cpp
        ch01/E01A_pattern_count.cpp
        utils.cpp)

add_executable(E01F_minimum_skew
        ch01/E01F_minimum_skew.cpp
        utils.cpp)

add_executable(E01G_hamming_distance
        ch01/E01G_hamming_distance.cpp
        utils.cpp)

add_executable(E01H_approximate_pattern_matching
        ch01/E01H_approximate_pattern_matching.cpp
        ch01/E01G_hamming_distance.cpp
        ch01/E01C_reverse_complement.cpp
        utils.cpp)



