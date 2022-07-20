//
// Created by Matej Hrnčiar on 20/07/2022.
//

#include "utils.h"

string Text(const string &genome, unsigned long i, unsigned long pattern_len) {
    return genome.substr(i, pattern_len);
}

