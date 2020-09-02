/*
 * @lc app=leetcode id=125 lang=cpp
 *
 * [125] Valid Palindrome
 */
#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int size = s.size();
        if(!size) return true;
        int i = 0;
        int j = size - 1;
        while(i <= j) {
            while(i <= j && (isspace(s[i]) || ispunct(s[i]))) {
                i++;
            }
            while(i <= j && (isspace(s[j]) || ispunct(s[j]))) {
                j--;
            }
            if(i <= j && tolower(s[i]) != tolower(s[j])) {
                return false;
            }
            ++i;
            --j;
        }
        return true;
    }
};

