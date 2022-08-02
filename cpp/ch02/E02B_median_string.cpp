//
// Created by Matej Hrnčiar on 28/07/2022.
//

#include "E02B_median_string.h"

int MinHammingDistance(const string &genome, const string &pattern, int k) {
    int minDistance = k;

    for (int i = 0; i < genome.size() - k + 1; i++) {
        int distance = HammingDistance(Text(genome, i, k), pattern);

        minDistance = distance < minDistance ? distance : minDistance;
    }

    return minDistance;
}

set<string> MedianString(const vector<string> &dna, int k) {
    vector<string> patterns;
    patterns = GeneratePatterns(k, patterns);

    map<string, int> distancePatternDna;
    int minString =  10000000;
    set<string> medians;

    for (auto &pattern : patterns) {
        int sumDistance = 0;

        for (auto &string : dna) {
            sumDistance += MinHammingDistance(string, pattern, k);
        }

        distancePatternDna.find(pattern)->second = sumDistance;

        minString = sumDistance < minString ? sumDistance : minString;
    }

    for (const auto &vals : distancePatternDna) {
        if (vals.second == minString) {
            medians.insert(vals.first);
        }
    }

    return medians;
}

string MedianStringVar(const vector<string>& dna, int k) {
    int distance = 10000000;
    string median;

    for (int i = 0; i < pow(4, k) - 1; i++) {
        auto pattern = NumberToPattern(i, k);
        auto n_distance = DistanceBetweenPatternsStrings(dna, pattern);

        if (distance > n_distance) {
            distance = n_distance;
            median = pattern;
        }
    }

    return median;
}

/*
int main() {
    vector<string> _dna;
    int _k;

    cout << "k: ";
    cin >> _k;

    _dna = ReadLines();

    cout << MedianStringVar(_dna, _k);
}
*/
