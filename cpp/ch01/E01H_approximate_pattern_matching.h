//
// Created by Matej Hrnčiar on 21/07/2022.
//

#ifndef CPP_E01H_APPROXIMATE_PATTERN_MATCHING_H
#define CPP_E01H_APPROXIMATE_PATTERN_MATCHING_H

#include "../utils.h"
#include "E01C_reverse_complement.h"
#include "E01G_hamming_distance.h"

tuple<int, list<int> > ApproximatePatternMatch(const string &genome, const string &pattern,
                                               int threshold, bool complement = false);

#endif //CPP_E01H_APPROXIMATE_PATTERN_MATCHING_H
