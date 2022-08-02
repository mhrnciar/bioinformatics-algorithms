//
// Created by Matej Hrnčiar on 20/07/2022.
//

#ifndef CPP_UTIL_H
#define CPP_UTIL_H

#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>

#include "ch01/E01A_pattern_count.h"

using namespace std;

static map<char, char> complement_key = {
        { 'A', 'T' },
        { 'C', 'G' },
        { 'G', 'C' },
        { 'T', 'A' }
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

static vector<string> bases = {"A", "C", "G", "T"};

string Text(const string &genome, unsigned long i, unsigned long pattern_len);

vector<string> ReadLines(const string& prompt = "DNA strings separated with newlines, end with enter:");

vector<string> GeneratePatterns(int k, vector<string> arr, const string &prefix = "");

vector< vector<float> > GenerateProbs(int n);

int Score(const vector<string> &motifs);

#endif //CPP_UTIL_H
