//
// Created by Matej Hrnčiar on 21/07/2022.
//

#ifndef CPP_E01N_D_NEIGHBORHOOD_H
#define CPP_E01N_D_NEIGHBORHOOD_H

#include "E01G_hamming_distance.h"
#include "../utils.h"

set<string> ImmediateNeighbors(const string &pattern);

set<string> Neighbors(const string &pattern, int d);

#endif //CPP_E01N_D_NEIGHBORHOOD_H
