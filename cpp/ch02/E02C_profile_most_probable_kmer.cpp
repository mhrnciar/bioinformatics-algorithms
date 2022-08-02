//
// Created by Matej Hrnčiar on 28/07/2022.
//

#include "E02C_profile_most_probable_kmer.h"

string MostProbableKmer(const string &genome, int k, vector< vector<float> > matrix) {
    if (matrix.empty()) {
        matrix = GenerateProbs(k);
    }

    list<float> probs;
    float max_prob = -1;
    string max_kmer;

    for (int i = 0; i < genome.size() - k; i++) {
        string substr = Text(genome, i, k);
        float total = 1;

        for (int j = 0; j < substr.size(); j++) {
            total *= matrix[symbol_key.find(substr[j])->second][j];
        }

        probs.push_back(total);

        if (total > max_prob) {
            max_prob = total;
            max_kmer = substr;
        }
    }

    return max_kmer;
}

/*
int main() {
    string _genome;
    int _k;
    vector< vector<float> > matrix;

    cout << "Genome: ";
    cin >> _genome;
    cout << "k: ";
    cin >> _k;

    cout << MostProbableKmer(_genome, _k, matrix);
}
*/
