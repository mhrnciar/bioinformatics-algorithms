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

set<string> FindClumpsWithFrequencies(const string &genome, int k, int window_len, int threshold) {
    set<string> freqPatterns;
    int *clumps = static_cast<int*>(calloc(pow(4, k), sizeof(int)));

    for (int i = 0; i < genome.size() - window_len; i++) {
        string substr = Text(genome, i, window_len);
        int *freqArr = ComputeFrequencies(substr, k);

        for (int j = 0; j < pow(4, k); j++) {
            if (freqArr[j] >= threshold) {
                clumps[j] = 1;
            }
        }
    }

    for (int i = 0; i < pow(4, k); i++) {
        if (clumps[i] == 1) {
            string pattern = NumberToPattern(i, k);
            freqPatterns.insert(pattern);
        }
    }

    return freqPatterns;
}

set<string> FastFindClumps(const string &genome, int k, int window_len, int threshold) {
    set<string> freqPatterns;
    int *clumps = static_cast<int*>(calloc(pow(4, k), sizeof(int)));

    string substr = Text(genome, 0, window_len);
    int *freqArr = ComputeFrequencies(substr, k);

    for (int i = 0; i < pow(4, k); i++) {
        if (freqArr[i] >= threshold) {
            clumps[i] = 1;
        }
    }

    for (int i = 1; i < genome.size() - window_len; i++) {
        string firstPattern = Text(genome, i - 1, k);
        int index = PatternToNumber(firstPattern);
        freqArr[index]--;

        string lastPattern = Text(genome, i + window_len - k, k);
        index = PatternToNumber(lastPattern);
        freqArr[index]++;

        if (freqArr[index] >= threshold) {
            clumps[index] = 1;
        }
    }

    for (int i = 0; i < pow(4, k); i++) {
        if (clumps[i] == 1) {
            string pattern = NumberToPattern(i, k);
            freqPatterns.insert(pattern);
        }
    }

    return freqPatterns;
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

    auto _patterns = FastFindClumps(_genome, _k, _window_len, _threshold);

    for (const auto &word : _patterns) {
        cout << word << " ";
    }
}
 */
