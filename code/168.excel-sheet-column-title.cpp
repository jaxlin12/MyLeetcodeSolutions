/*
 * @lc app=leetcode id=168 lang=cpp
 *
 * [168] Excel Sheet Column Title
 */
#include <string>
using namespace std;
class Solution {
public:
    string convertToTitle(int n) {
        return n == 0 ? "" : convertToTitle(n / 26) + (char) (--n % 26 + 'A');

    }
};

