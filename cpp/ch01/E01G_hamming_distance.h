//
// Created by Matej Hrnčiar on 21/07/2022.
//

#ifndef CPP_E01G_HAMMING_DISTANCE_H
#define CPP_E01G_HAMMING_DISTANCE_H

#include <cstdlib>
#include "../utils.h"

int HammingDistance(const string &str1, const string &str2);

tuple< int, vector<char> > ApproximatePatternCount(const string &genome, const string &pattern, int threshold);

#endif //CPP_E01G_HAMMING_DISTANCE_H
