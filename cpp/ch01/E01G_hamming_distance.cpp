//
// Created by Matej Hrnčiar on 21/07/2022.
//

#include "E01G_hamming_distance.h"

int HammingDistance(const string &str1, const string &str2) {
    int distance = 0;

    if (str1.size() != str2.size()) {
        return -1;
    }

    for (int i = 0; i < str1.size(); i++) {
        if (str1[i] != str2[i]) {
            distance++;
        }
    }

    return distance;
}

tuple< int, vector<char> > ApproximatePatternCount(const string &genome, const string &pattern, int threshold) {
    int count = 0;
    vector<char> indices;

    for (unsigned long i = 0; i < genome.size() - pattern.size(); i++) {
        string n_pattern = Text(genome, i, pattern.size());

        if (HammingDistance(pattern, n_pattern) <= threshold) {
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
    int _threshold;

    cout << "Genome: ";
    cin >> _genome;
    cout << "Pattern: ";
    cin >> _pattern;
    cout << "t: ";
    cin >> _threshold;

    auto [_count, _indices] = ApproximatePatternCount(_genome, _pattern, _threshold);

    cout << "Count: " << _count << endl;
    cout << _genome << endl;

    for (char c : _indices) {
        cout << c;
    }
}
 */
