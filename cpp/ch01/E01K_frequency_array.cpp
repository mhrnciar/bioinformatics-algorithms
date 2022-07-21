//
// Created by Matej Hrnčiar on 21/07/2022.
//

#include "E01K_frequency_array.h"

int *ComputeFrequencies(const string &genome, int k) {
    int *freq_arr = static_cast<int *>(calloc(pow(4, k), sizeof(int)));

    for (int i = 0; i < genome.size() - k + 1; i++) {
        string pattern = Text(genome, i, k);
        int j = PatternToNumber(pattern);

        freq_arr[j]++;
    }

    return freq_arr;
}

/*
int main() {
    string _genome;
    int _k;

    cout << "Genome: ";
    cin >> _genome;
    cout << "k: ";
    cin >> _k;

    auto arr = ComputeFrequencies(_genome, _k);

    for (int i = 0; i < pow(4, _k); i++) {
        cout << arr[i] << " ";
    }
}
 */
