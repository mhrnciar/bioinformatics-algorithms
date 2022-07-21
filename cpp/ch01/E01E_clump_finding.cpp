//
// Created by Matej Hrnčiar on 21/07/2022.
//

#include "E01E_clump_finding.h"

set<string> FindClumps(const string &genome, int k, int window_len, int threshold) {
    set<string> freq_patterns;

    for (int i = 0; i < genome.size() - window_len + 1; i++) {
        for (int j = i; j < i + window_len - k; j++) {
            string pattern = Text(genome, j, k);

            auto [count, indices] = PatternCount(Text(genome, i, window_len), pattern);

            if (count == threshold) {
                freq_patterns.insert(pattern);
            }
        }
    }

    return freq_patterns;
}

/*
int main() {
    string _genome;
    int _k, _window_len, _threshold;

    cout << "Genome: ";
    cin >> _genome;

    cout << "k: ";
    cin >> _k;
    cout << "L: ";
    cin >> _window_len;
    cout << "t: ";
    cin >> _threshold;

    auto _patterns = FindClumps(_genome, _k, _window_len, _threshold);

    for (const auto &word : _patterns) {
        cout << word << " ";
    }
}
 */
