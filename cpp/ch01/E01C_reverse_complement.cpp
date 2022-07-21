//
// Created by Matej Hrnčiar on 21/07/2022.
//

#include "E01C_reverse_complement.h"

string ReverseComplement(const string &pattern) {
    string result = string(pattern.size(), 'X');
    int k = 0;

    for (int i = pattern.size() - 1; i >= 0; i--) {
        result[k] = complement_key.find(pattern[i])->second;
        k++;
    }

    return result;
}

/*
int main() {
    string _pattern;

    cout << "Pattern: ";
    cin >> _pattern;

    auto revComplement = ReverseComplement(_pattern);

    cout << "Original string: " << _pattern << endl << "Reverse complement: " << revComplement;
}
*/
