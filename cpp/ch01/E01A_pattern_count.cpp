//
// Created by Matej Hrnčiar on 20/07/2022.
//

#include "E01A_pattern_count.h"

std::tuple< int, std::list<char> > PatternCount(const std::string &genome, const std::string &pattern) {
    int count = 0;
    std::list<char> indices;

    for (unsigned long i = 0; i < genome.size() - pattern.size(); i++) {
        if (Text(genome, i, pattern.size()) == pattern) {
            count++;
            indices.push_back('^');
        }
        else {
            indices.push_back('-');
        }
    }

    return {count, indices};
}

/*
int main() {
    std::string _genome, _pattern;

    std::cout << "Genome: ";
    std::cin >> _genome;
    std::cout << "Pattern: ";
    std::cin >> _pattern;

    auto [count, indices] = PatternCount(_genome, _pattern);

    std::cout << "Count: " << count << std::endl;
    std::cout << _genome << std::endl;

    for (char c : indices) {
        std::cout << c;
    }
}
 */
