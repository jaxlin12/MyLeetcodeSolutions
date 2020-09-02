/*
 * @lc app=leetcode id=171 lang=cpp
 *
 * [171] Excel Sheet Column Number
 */

#include <string>
#include <cmath>
using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        int size = s.size();
        int num = 0;
        for(int i = 0;i < size;i++) {
            num += (pow(26, size - i - 1) * int(s[i] - 'A' + 1));
        }
        return num;
    }
};

