//
// Created by Matej Hrnčiar on 20/07/2022.
//

#include "E01A_pattern_count.h"

tuple< int, vector<char> > PatternCount(const string &genome, const string &pattern) {
    int count = 0;
    vector<char> indices;

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
    string _genome, _pattern;

    cout << "Genome: ";
    cin >> _genome;
    cout << "Pattern: ";
    cin >> _pattern;

    auto [count, indices] = PatternCount(_genome, _pattern);

    cout << "Count: " << count << endl;
    cout << _genome << endl;

    for (char c : indices) {
        cout << c;
    }
}
 */
