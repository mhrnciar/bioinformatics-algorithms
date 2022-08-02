//
// Created by Matej Hrnčiar on 20/07/2022.
//

#include "utils.h"

string Text(const string &genome, unsigned long i, unsigned long pattern_len) {
    return genome.substr(i, pattern_len);
}

vector<string> ReadLines(const string &prompt) {
    vector<string> dna;
    string temp;

    cout << prompt << endl;
    cin.ignore();

    while(getline(cin, temp)) {
        if (temp.empty())
            break;

        dna.push_back(temp);
    }

    return dna;
}

vector<string> GeneratePatterns(int k, vector<string> arr, const string &prefix) {
    if (k == 0) {
        arr.push_back(prefix);
        return arr;
    }

    for (auto &base : bases) {
        string new_prefix = prefix + base;
        arr = GeneratePatterns(k - 1, arr, new_prefix);
    }

    return arr;
}

vector< vector<float> > GenerateProbs(int n) {
    vector< vector<float> > matrix;
    float temp;

    for (int i = 0; i < 4; i++) {
        vector<float> line;

        for (int j = 0; j < n; j++) {
            cin >> temp;
            line.push_back(temp);
        }

        matrix.push_back(line);
    }

    return matrix;
}

int Score(const vector<string> &motifs) {
    int total = 0;

    for (int i = 0; i < motifs[0].size(); i++) {
        vector<string> j;

        for (auto &m : motifs) {
            j.push_back(m.substr(i, 1));
        }

        vector<int> counts = {0, 0, 0, 0};
        for (auto &temp : j) {
            if (temp == "A")
                counts[0]++;
            else if (temp == "C")
                counts[1]++;
            else if (temp == "G")
                counts[2]++;
            else
                counts[3]++;
        }

        total += (j.size() - *max_element(counts.begin(), counts.end()));
    }

    return total;
}
