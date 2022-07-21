//
// Created by Matej Hrnčiar on 21/07/2022.
//

#ifndef CPP_E01D_PATTERN_MATCHING_H
#define CPP_E01D_PATTERN_MATCHING_H

#include <iostream>
#include <string>
#include <list>
#include "../utils.h"
#include "E01A_pattern_count.h"
#include "E01C_reverse_complement.h"

tuple<int, list<int> > PatternMatch(const string &genome, const string &pattern, bool complement = false);

#endif //CPP_E01D_PATTERN_MATCHING_H
