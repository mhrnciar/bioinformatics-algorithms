//
// Created by Matej Hrnčiar on 20/07/2022.
//

#include "E01B_frequent_words.h"

set<string> FrequentWords(const string &genome, int k, int limit = -1) {
    set<string> freqPatterns;
    int *count = static_cast<int *>(calloc(genome.size(), sizeof(int)));

    for (int i = 0; i < genome.size() - k; i++) {
        string pattern = Text(genome, i, k);
        auto [cnt, ind] = PatternCount(genome, pattern);
        count[i] = cnt;
    }

    if (limit < 1) {
        int max_count = *max_element(count , count + genome.size());

        for (int i = 0; i < genome.size() - k; i++) {
            if (count[i] == max_count) {
                freqPatterns.insert(Text(genome, i, k));
            }
        }
    }
    else {
        for (int i = 0; i < genome.size() - k; i++) {
            if (count[i] == limit) {
                freqPatterns.insert(Text(genome, i, k));
            }
        }
    }

    return freqPatterns;
}

set<string> FastFrequentWords(const string &genome, int k, int limit = -1) {
    set<string> freqPatterns;
    int *freqArr = ComputeFrequencies(genome, k);

    int max_count = *max_element(freqArr , freqArr + static_cast<int>(pow(4, k)));

    if (limit < 1) {
        for (int i = 0; i < pow(4, k); i++) {
            if (freqArr[i] == max_count) {
                string pattern = NumberToPattern(i, k);
                freqPatterns.insert(pattern);
            }
        }
    }
    else {
        for (int i = 0; i < pow(4, k); i++) {
            if (freqArr[i] == limit) {
                string pattern = NumberToPattern(i, k);
                freqPatterns.insert(pattern);
            }
        }
    }

    return freqPatterns;
}

set<string> FastFrequentWordsBySorting(const string &genome, int k, int limit = -1) {
    set<string> freqPatterns;
    int *index = static_cast<int*>(calloc(genome.size() - k, sizeof(int)));
    int *count = static_cast<int*>(calloc(genome.size() - k, sizeof(int)));

    for (int i = 0; i < genome.size() - k; i++) {
        string pattern = Text(genome, i, k);
        index[i] = PatternToNumber(pattern);
        count[i] = 1;
    }

    std::sort(index, index + genome.size() - k);

    for (int i = 1; i < genome.size() - k; i++) {
        if (index[i] == index[i-1]) {
            count[i] = count[i-1] + 1;
        }
    }

    if (limit < 1) {
        int max_count = *max_element(count , count + genome.size());

        for (int i = 0; i < genome.size() - k; i++) {
            if (count[i] == max_count) {
                string pattern = NumberToPattern(index[i], k);
                freqPatterns.insert(pattern);
            }
        }
    }
    else {
        for (int i = 0; i < genome.size() - k; i++) {
            if (count[i] == limit) {
                string pattern = NumberToPattern(index[i], k);
                freqPatterns.insert(pattern);
            }
        }
    }

    return freqPatterns;
}

/*
int main() {
    string _genome;
    int _k;

    cout << "Genome: ";
    cin >> _genome;
    cout << "k: ";
    cin >> _k;

    auto freq_words = FastFrequentWordsBySorting(_genome, _k);

    for (const auto& word : freq_words) {
        cout << word << endl;
    }
}
*/
