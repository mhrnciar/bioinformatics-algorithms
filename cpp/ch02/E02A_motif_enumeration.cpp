//
// Created by Matej Hrnčiar on 28/07/2022.
//

#include "E02A_motif_enumeration.h"

set<string> MotifEnumeration(const vector<string> &dna, int k, int d) {
    list<string> motifs;
    set<string> motif_pattern;

    for (auto &pattern : dna) {
        set<string> temp;

        for (int i = 0; i < pattern.size() - k + 1; i++) {
            auto neighbors = Neighbors(Text(pattern, i, k), d);

            for (const auto &word : neighbors) {
                temp.insert(word);
            }
        }

        for (auto &motif : temp) {
            motifs.push_back(motif);
        }
    }

    for (auto &element : motifs) {
        int total = 0;
        for (auto &temp : motifs) {
            if (element == temp)
                total++;
        }

        if (total == dna.size()) {
            motif_pattern.insert(element);
        }
    }

    return motif_pattern;
}

int main() {
    vector<string> _dna;
    string _temp;
    int _k, _d;

    cout << "k: ";
    cin >> _k;
    cout << "d: ";
    cin >> _d;

    _dna = ReadLines();

    auto _motifs = MotifEnumeration(_dna, _k, _d);

    for (const auto &word : _motifs) {
        cout << word << endl;
    }
}
