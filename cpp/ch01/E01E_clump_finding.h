//
// Created by Matej Hrnčiar on 21/07/2022.
//

#ifndef CPP_E01E_CLUMP_FINDING_H
#define CPP_E01E_CLUMP_FINDING_H

#include "../utils.h"
#include "E01A_pattern_count.h"
#include "E01K_frequency_array.h"
#include "E01L_pattern_to_number.h"
#include "E01M_number_to_pattern.h"

set<string> FindClumps(const string &genome, int k, int window_len, int threshold);

set<string> FindClumpsWithFrequencies(const string &genome, int k, int window_len, int threshold);

set<string> FastFindClumps(const string &genome, int k, int window_len, int threshold);

#endif //CPP_E01E_CLUMP_FINDING_H
