//
// Created by Matej Hrnčiar on 21/07/2022.
//

#include "E01F_minimum_skew.h"

tuple< int, list<int> > MinSkew(const string &genome) {
    int *graph = static_cast<int *>(calloc(genome.size(), sizeof(int)));
    int skew_value = 0, min_skew = 1;
    list<int> min_indices;

    for (int i = 0; i < genome.size(); i++) {
        if (genome[i] == 'C') {
            skew_value--;
        }
        else if (genome[i] == 'G') {
            skew_value++;
        }

        graph[i] = skew_value;

        if (skew_value == min_skew) {
            min_indices.push_back(i + 1);
        }
        else if (skew_value < min_skew) {
            min_skew = skew_value;
            min_indices.clear();
            min_indices.push_back(i + 1);
        }
    }

    return {min_skew, min_indices};
}

/*
int main() {
    string _genome;

    cout << "Genome: ";
    cin >> _genome;

    auto [_min_skew, _min_indices] = MinSkew(_genome);

    cout << "Minimum skew: " << _min_skew << endl;

    for (auto ind : _min_indices) {
        cout << ind << " ";
    }
}
 */
