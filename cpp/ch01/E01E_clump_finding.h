//
// Created by Matej Hrnčiar on 21/07/2022.
//

#ifndef CPP_E01E_CLUMP_FINDING_H
#define CPP_E01E_CLUMP_FINDING_H

#include <iostream>
#include <string>
#include <set>
#include "E01A_pattern_count.h"
#include "../utils.h"

set<string> FindClumps(const string &genome, int k, int window_len, int threshold);

#endif //CPP_E01E_CLUMP_FINDING_H
