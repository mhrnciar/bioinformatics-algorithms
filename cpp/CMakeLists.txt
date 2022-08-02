cmake_minimum_required(VERSION 3.22)
project(cpp)

set(CMAKE_CXX_STANDARD 17)

# ---------- TARGETS ----------
# CHAPTER 1
add_executable(E01A_pattern_count
        ch01/E01A_pattern_count.cpp
        utils.cpp)

add_executable(E01B_frequent_words
        ch01/E01A_pattern_count.cpp
        ch01/E01B_frequent_words.cpp
        ch01/E01K_frequency_array.cpp
        ch01/E01L_pattern_to_number.cpp
        ch01/E01M_number_to_pattern.cpp
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
        ch01/E01K_frequency_array.cpp
        ch01/E01L_pattern_to_number.cpp
        ch01/E01M_number_to_pattern.cpp
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

add_executable(E01I_frequent_words_mismatches
        ch01/E01I_frequent_words_mismatches.cpp
        ch01/E01G_hamming_distance.cpp
        ch01/E01L_pattern_to_number.cpp
        ch01/E01M_number_to_pattern.cpp
        ch01/E01N_d_neighborhood.cpp
        utils.cpp)

add_executable(E01J_frequent_words_mismatches_reverse_complements
        ch01/E01J_frequent_words_mismatches_reverse_complements.cpp
        ch01/E01C_reverse_complement.cpp
        ch01/E01G_hamming_distance.cpp
        utils.cpp)

add_executable(E01K_frequency_array
        ch01/E01K_frequency_array.cpp
        ch01/E01L_pattern_to_number.cpp
        utils.cpp)

add_executable(E01L_pattern_to_number
        ch01/E01L_pattern_to_number.cpp
        utils.cpp)

add_executable(E01M_number_to_pattern
        ch01/E01M_number_to_pattern.cpp
        utils.cpp)

add_executable(E01N_d_neighborhood
        ch01/E01N_d_neighborhood.cpp
        ch01/E01G_hamming_distance.cpp
        utils.cpp)

# CHAPTER 2
add_executable(E02A_motif_enumeration
        ch02/E02A_motif_enumeration.cpp
        ch01/E01N_d_neighborhood.cpp
        ch01/E01G_hamming_distance.cpp
        utils.cpp)

add_executable(E02B_median_string
        ch02/E02B_median_string.cpp
        ch01/E01G_hamming_distance.cpp
        ch01/E01L_pattern_to_number.cpp
        ch01/E01M_number_to_pattern.cpp
        ch02/E02H_distance_pattern_strings.cpp
        utils.cpp)

add_executable(E02C_profile_most_probable_kmer
        ch02/E02C_profile_most_probable_kmer.cpp
        utils.cpp)

add_executable(E02D_greedy_motif_search
        ch02/E02D_greedy_motif_search.cpp
        ch02/E02C_profile_most_probable_kmer.cpp
        utils.cpp)

add_executable(E02E_greedy_motif_search_pseudocounts
        ch02/E02E_greedy_motif_search_pseudocounts.cpp
        ch02/E02C_profile_most_probable_kmer.cpp
        utils.cpp)

add_executable(E02H_distance_pattern_strings
        ch02/E02H_distance_pattern_strings.cpp
        ch01/E01G_hamming_distance.cpp
        utils.cpp)

