/*
 * @lc app=leetcode id=33 lang=cpp
 *
 * [33] Search in Rotated Sorted Array
 */
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int index = nums.size() / 2;
        bool found = false;
        while(!found && index == 0) {
            if(target == nums[index]) {
                found = true;
                
            }
            else if(target < nums[index]) {

            }
            else {

            }
        }
    }
};

