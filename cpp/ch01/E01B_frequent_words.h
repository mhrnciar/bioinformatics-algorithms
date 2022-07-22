//
// Created by Matej Hrnčiar on 20/07/2022.
//

#ifndef CPP_E01B_FREQUENT_WORDS_H
#define CPP_E01B_FREQUENT_WORDS_H

#include <cstdlib>
#include "../utils.h"
#include "E01A_pattern_count.h"
#include "E01K_frequency_array.h"
#include "E01L_pattern_to_number.h"
#include "E01M_number_to_pattern.h"

set<string> FrequentWords(const string &genome, int k, int limit);

set<string> FastFrequentWords(const string &genome, int k, int limit);

set<string> FastFrequentWordsBySorting(const string &genome, int k, int limit);

#endif //CPP_E01B_FREQUENT_WORDS_H
