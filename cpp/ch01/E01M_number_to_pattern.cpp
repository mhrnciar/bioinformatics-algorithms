//
// Created by Matej Hrnčiar on 21/07/2022.
//

#include "E01M_number_to_pattern.h"

string NumberToPattern(int num, int k) {
    if (k == 1) {
        return string(1, number_key.find(num)->second);
    }

    int prefix_index = num / 4;
    int r = num & 3;
    char symbol = number_key.find(r)->second;

    string prefix_pattern = NumberToPattern(prefix_index, k - 1);
    prefix_pattern.push_back(symbol);

    return prefix_pattern;
}

/*
int main() {
    int _num, _k;

    cout << "Number: ";
    cin >> _num;
    cout << "k: ";
    cin >> _k;

    cout << NumberToPattern(_num, _k) << endl;
}
 */
