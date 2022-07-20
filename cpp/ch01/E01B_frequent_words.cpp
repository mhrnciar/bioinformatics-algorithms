//
// Created by Matej Hrnčiar on 20/07/2022.
//

#include "E01B_frequent_words.h"

std::set<std::string> FrequentWords(const string &genome, int k, int limit = -1) {
    std::set<std::string> freq_words;
    int *count = static_cast<int *> (calloc(genome.size(), sizeof(int)));

    for (int i = 0; i < genome.size() - k; i++) {
        std::string pattern = Text(genome, i, k);
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

int main() {
    std::string _genome;
    int _k;

    std::cout << "Genome: ";
    std::cin >> _genome;
    std::cout << "k: ";
    std::cin >> _k;

    auto freq_words = FrequentWords(_genome, _k);

    for (const auto& word : freq_words) {
        std::cout << word << std::endl;
    }
}
