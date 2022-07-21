//
// Created by Matej Hrnčiar on 21/07/2022.
//

#include "E01I_frequent_words_mismatches.h"

set<string> MismatchFrequentWords(const string &genome, int k, int threshold) {
    set<string> freq_patterns;
    int *freq_arr = static_cast<int *>(calloc(pow(4, k), sizeof(int)));
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

            freq_arr[i] = count;
        }
    }

    int max_count = *max_element(freq_arr , freq_arr + static_cast<int>(pow(4, k)));

    for (int i = 0; i < pow(4, k); i++) {
        if (freq_arr[i] == max_count) {
            auto pattern = NumberToPattern(i, k);
            freq_patterns.insert(pattern);
        }
    }

    return freq_patterns;
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

    auto _result = MismatchFrequentWords(_genome, _k, _threshold);

    for (auto word : _result) {
        cout << word << endl;
    }
}
 */
