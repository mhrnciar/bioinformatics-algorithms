//
// Created by Matej Hrnčiar on 28/07/2022.
//

#include "E02E_greedy_motif_search_pseudocounts.h"

vector<string> GreedyMotifSearchPseudocounts(const vector<string> &dna, int k, int t) {
    vector<string> bestMotifs, kmers;

    for (auto &str : dna) {
        bestMotifs.push_back(str.substr(0, k));
    }

    for (int i = 0; i < dna[0].size() - k + 1; i++) {
        kmers.push_back(Text(dna[0], i, k));
    }

    for (auto &kmer : kmers) {
        vector<string> motifs;
        motifs.push_back(kmer);

        for (int i = 1; i < t; i++) {
            vector<string> _motifs;
            vector< vector<float> > matrix;

            for (int j = 0; j < i; j++) {
                _motifs.push_back(motifs[j]);
            }

            for (auto &base : bases) {
                vector<float> mat;

                for (int j = 0; j < k; j++) {
                    vector<string> mm;
                    for (auto &m : _motifs) {
                        mm.push_back(m.substr(j, 1));
                    }

                    float total = 0;
                    for (auto &temp : mm) {
                        if (base == temp)
                            total++;
                    }

                    mat.push_back((total + 1) / (float) (_motifs.size() + 4));
                }

                matrix.push_back(mat);
            }

            motifs.push_back(MostProbableKmer(dna[i], k, matrix));
        }

        if (Score(motifs) < Score(bestMotifs)) {
            bestMotifs = motifs;
        }
    }

    return bestMotifs;
}

int main() {
    vector<string> _dna;
    string _temp;
    int _k, _t;

    cout << "k: ";
    cin >> _k;
    cout << "t: ";
    cin >> _t;

    _dna = ReadLines();

    auto _motifs = GreedyMotifSearchPseudocounts(_dna, _k, _t);

    for (const auto &word : _motifs) {
        cout << word << endl;
    }
}
