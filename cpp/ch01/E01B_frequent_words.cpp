//
// Created by Matej Hrnčiar on 20/07/2022.
//

#include "E01B_frequent_words.h"

set<string> FrequentWords(const string &genome, int k, int limit = -1) {
    set<string> freq_words;
    int *count = static_cast<int *>(calloc(genome.size(), sizeof(int)));

    for (int i = 0; i < genome.size() - k; i++) {
        string pattern = Text(genome, i, k);
        auto [cnt, ind] = PatternCount(genome, pattern);
        count[i] = cnt;
    }

    if (limit < 0) {
        int max_count = *max_element(count , count + genome.size());

        for (int i = 0; i < genome.size() - k; i++) {
            if (count[i] == max_count) {
                freq_words.insert(Text(genome, i, k));
            }
        }
    }
    else {
        for (int i = 0; i < genome.size() - k; i++) {
            if (count[i] == limit) {
                freq_words.insert(Text(genome, i, k));
            }
        }
    }

    return freq_words;
}

/*
int main() {
    string _genome;
    int _k;

    cout << "Genome: ";
    cin >> _genome;
    cout << "k: ";
    cin >> _k;

    auto freq_words = FrequentWords(_genome, _k);

    for (const auto& word : freq_words) {
        cout << word << endl;
    }
}
 */
