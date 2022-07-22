//
// Created by Matej Hrnčiar on 20/07/2022.
//

#ifndef CPP_UTIL_H
#define CPP_UTIL_H

#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>

using namespace std;

static map<char, char> complement_key = {
        { 'A', 'T' },
        { 'T', 'A' },
        { 'C', 'G' },
        { 'G', 'C' }
};

static map<char, int> symbol_key = {
        { 'A', 0 },
        { 'C', 1 },
        { 'G', 2 },
        { 'T', 3 }
};

static map<int, char> number_key = {
        { 0, 'A' },
        { 1, 'C' },
        { 2, 'G' },
        { 3, 'T' }
};

static vector<string> bases = {"C", "G", "A", "T"};

string Text(const string &genome, unsigned long i, unsigned long pattern_len);

#endif //CPP_UTIL_H
