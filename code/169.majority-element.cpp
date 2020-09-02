/*
 * @lc app=leetcode id=169 lang=cpp
 *
 * [169] Majority Element
 */
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int counter = 0, majority;
        for (int num : nums) {
            if (!counter) {
                majority = num;
            }
            counter += num == majority ? 1 : -1;
        }
        return majority;
    }
};

