//
// Created by Matej Hrnčiar on 21/07/2022.
//

#include "E01L_pattern_to_number.h"

int PatternToNumber(const string &pattern) {
    if (pattern.empty()) {
        return 0;
    }

    char symbol = pattern[pattern.size()-1];
    string prefix = pattern.substr(0, pattern.size() - 1);

    return 4 * PatternToNumber(prefix) + symbol_key.find(symbol)->second;
}

/*
int main() {
    string _pattern;

    cout << "Pattern: ";
    cin >> _pattern;

    cout << PatternToNumber(_pattern) << endl;
}
 */
