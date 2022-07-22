//
// Created by Matej Hrnčiar on 21/07/2022.
//

#ifndef CPP_E01I_FREQUENT_WORDS_MISMATCHES_H
#define CPP_E01I_FREQUENT_WORDS_MISMATCHES_H

#include <cmath>
#include "../utils.h"
#include "E01G_hamming_distance.h"
#include "E01L_pattern_to_number.h"
#include "E01M_number_to_pattern.h"
#include "E01N_d_neighborhood.h"

set<string> MismatchFrequentWords(const string &genome, int k, int threshold);

set<string> MismatchFrequentWordsBySorting(const string &genome, int k, int threshold);

#endif //CPP_E01I_FREQUENT_WORDS_MISMATCHES_H
