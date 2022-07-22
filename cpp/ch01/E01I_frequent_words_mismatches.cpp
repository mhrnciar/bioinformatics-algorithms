//
// Created by Matej Hrnčiar on 21/07/2022.
//

#include "E01I_frequent_words_mismatches.h"

set<string> MismatchFrequentWords(const string &genome, int k, int threshold) {
    set<string> freqPatterns;
    int *freqArr = static_cast<int *>(calloc(pow(4, k), sizeof(int)));
    int *close = static_cast<int *>(calloc(pow(4, k), sizeof(int)));

    for (int i = 0; i < genome.size() - k; i++) {
        auto neighborhood = Neighbors(Text(genome, i, k), threshold);

        for (auto &pattern : neighborhood) {
            auto index = PatternToNumber(pattern);
            close[index] = 1;
        }
    }

    for (int i = 0; i < pow(4, k); i++) {
        if (close[i] == 1) {
            auto pattern = NumberToPattern(i, k);
            auto [count, temp] = ApproximatePatternCount(genome, pattern, threshold);

            freqArr[i] = count;
        }
    }

    int max_count = *max_element(freqArr , freqArr + static_cast<int>(pow(4, k)));

    for (int i = 0; i < pow(4, k); i++) {
        if (freqArr[i] == max_count) {
            auto pattern = NumberToPattern(i, k);
            freqPatterns.insert(pattern);
        }
    }

    return freqPatterns;
}

set<string> MismatchFrequentWordsBySorting(const string &genome, int k, int threshold) {
    set<string> freqPatterns;
    vector<string> neighborhood;
    int neighborhoods_count = 0;

    for (int i = 0; i < genome.size() - k; i++) {
        auto temp = Neighbors(Text(genome, i, k), threshold);
        neighborhoods_count++;

        for (auto &word : temp) {
            neighborhood.push_back(word);
        }
    }

    int *index = static_cast<int*>(calloc(neighborhoods_count, sizeof(int)));
    int *count = static_cast<int*>(calloc(neighborhoods_count, sizeof(int)));

    for (int i = 0; i < neighborhoods_count; i++) {
        string pattern = neighborhood[i];
        index[i] = PatternToNumber(pattern);
        count[i] = 1;
    }

    std::sort(index, index + neighborhoods_count);

    for (int i = 0; i < neighborhoods_count - 1; i++) {
        if (index[i] == index[i+1]) {
            count[i+1] = count[i] + 1;
        }
    }

    int max_count = *max_element(count , count + neighborhoods_count);

    for (int i = 0; i < neighborhoods_count; i++) {
        if (count[i] == max_count) {
            auto pattern = NumberToPattern(index[i], k);
            freqPatterns.insert(pattern);
        }
    }

    return freqPatterns;
}

/*
int main() {
    string _genome;
    int _k, _threshold;

    cout << "Genome: ";
    cin >> _genome;
    cout << "k: ";
    cin >> _k;
    cout << "t: ";
    cin >> _threshold;

    auto _result = MismatchFrequentWordsBySorting(_genome, _k, _threshold);

    for (auto &word : _result) {
        cout << word << endl;
    }
}
 */
