//
// Created by Matej Hrnčiar on 21/07/2022.
//

#include "E01N_d_neighborhood.h"

set<string> ImmediateNeighbors(const string &pattern) {
    set<string> neighborhood;

    for (int i = 0; i < pattern.size(); i++) {
        for (auto base : bases) {
            string temp = pattern;
            temp[i] = base;

            neighborhood.insert(temp);
        }
    }

    return neighborhood;
}

set<string> Neighbors(const string &pattern, int d) {
    if (d == 0) {
        return {pattern};
    }

    if (pattern.size() == 1) {
        return {string(1, bases[0]), string(1, bases[1]),
                string(1, bases[2]), string(1, bases[3])};
    }

    set<string> neighborhood;
    auto suffix_neighbors = Neighbors(pattern.substr(1, pattern.size()), d);

    for (const string &text : suffix_neighbors) {
        if (HammingDistance(pattern.substr(1, pattern.size()), text) < d) {
            for (auto base : bases) {
                auto temp = text;
                neighborhood.insert(temp.insert(0, 1, base));
            }
        }
        else {
            auto temp = text;
            neighborhood.insert(temp.insert(0, 1, pattern[0]));
        }
    }

    return neighborhood;
}

/*
int main() {
    string _pattern;
    int _d;

    cout << "Pattern: ";
    cin >> _pattern;
    cout << "d: ";
    cin >> _d;

    auto neighborhood = Neighbors(_pattern, _d);

    for (const auto &word : neighborhood) {
        cout << word << endl;
    }
}
 */
