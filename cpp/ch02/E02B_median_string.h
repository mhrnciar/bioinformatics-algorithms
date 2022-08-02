//
// Created by Matej Hrnčiar on 28/07/2022.
//

#ifndef CPP_E02B_MEDIAN_STRING_H
#define CPP_E02B_MEDIAN_STRING_H

#include <cmath>

#include "../utils.h"
#include "../ch01/E01G_hamming_distance.h"
#include "../ch01/E01L_pattern_to_number.h"
#include "../ch01/E01M_number_to_pattern.h"
#include "../ch02/E02H_distance_pattern_strings.h"

int MinHammingDistance(const string &genome, const string &pattern, int k);

set<string> MedianString(const vector<string> &dna, int k);

string MedianStringVar(const vector<string> &dna, int k);

#endif //CPP_E02B_MEDIAN_STRING_H
