//
// Created by Matej Hrnčiar on 20/07/2022.
//

#ifndef CPP_E01B_FREQUENT_WORDS_H
#define CPP_E01B_FREQUENT_WORDS_H

#include <iostream>
#include <string>
#include <set>
#include <cstdlib>
#include "../utils.h"
#include "E01A_pattern_count.h"

std::set<std::string> FrequentWords(const string &genome, int k, int limit);


#endif //CPP_E01B_FREQUENT_WORDS_H