//
// Created by Matej Hrnčiar on 21/07/2022.
//

#include "E01J_frequent_words_mismatches_reverse_complements.h"

set<string> neighbour(const string& pattern, int mismatch, set<string> words) {
    if (mismatch == 0) {
        words.insert(pattern);
    }
    else {
        for (int i = 0; i < pattern.size(); i++) {
            for (const auto &base : bases) {
                string new_pattern = pattern.substr(0, i) + base + pattern.substr(i + 1);

                if (mismatch <= 1) {
                    words.insert(new_pattern);
                }
                else {
                    neighbour(new_pattern, mismatch - 1, words);
                }
            }
        }
    }

    return words;
}

set<string> MismatchFrequentWordsWithRevComps(const string &genome, int k, int threshold) {
    map<string, int> allFrequentWords;

    for (int i = 0; i < genome.size() - k + 1; i++) {
        set<string> frequentWords;
        frequentWords = neighbour(Text(genome, i, k), threshold, frequentWords);

        for (const auto &word : frequentWords) {
            if (allFrequentWords.find(word) != allFrequentWords.end()) {
                allFrequentWords.find(word)->second++;
            }
            else {
                allFrequentWords.insert(pair<string, int>(word, 0));
            }
        }
    }

    int max_count = 0;

    for (const auto &t : allFrequentWords) {
        string rev = ReverseComplement(t.first);

        for (int i = 0; i < genome.size() - k + 1; i++) {
            if (HammingDistance(Text(genome, i, k), rev) <= threshold) {
                allFrequentWords.find(t.first)->second++;

                max_count = allFrequentWords.find(t.first)->second > max_count ?
                        allFrequentWords.find(t.first)->second : max_count;
            }
        }
    }

    set<string> result;

    for (const auto &t : allFrequentWords) {
        if (allFrequentWords.find(t.first)->second == max_count) {
            result.insert(allFrequentWords.find(t.first)->first);
            result.insert(ReverseComplement(allFrequentWords.find(t.first)->first));
        }
    }

    return result;
}

int main() {
    string _genome;
    int _k, _threshold;

    cout << "Genome: ";
    cin >> _genome;
    cout << "k: ";
    cin >> _k;
    cout << "t: ";
    cin >> _threshold;

    auto _result = MismatchFrequentWordsWithRevComps(_genome, _k, _threshold);

    for (const auto &word : _result) {
        cout << word << endl;
    }
}
