//
// Created by Matej Hrnčiar on 21/07/2022.
//

#ifndef CPP_E01J_FREQUENT_WORDS_MISMATCHES_REVERSE_COMPLEMENTS_H
#define CPP_E01J_FREQUENT_WORDS_MISMATCHES_REVERSE_COMPLEMENTS_H

#include "../utils.h"
#include "E01C_reverse_complement.h"
#include "E01G_hamming_distance.h"
#include "E01I_frequent_words_mismatches.h"

tuple<int, list<int> > MismatchFrequentWordsWithRevComps(const string &genome, int k,
                                                         int threshold, bool complement = false);

#endif //CPP_E01J_FREQUENT_WORDS_MISMATCHES_REVERSE_COMPLEMENTS_H
