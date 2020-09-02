/*
 * @lc app=leetcode id=167 lang=cpp
 *
 * [167] Two Sum II - Input array is sorted
 */
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int low = 0;
        int high = numbers.size() - 1;
        int sum = 0;
        while(low < high) {
            sum = numbers[low] + numbers[high];
            if(sum < target) {
                ++low;
            }
            else if(sum > target) {
                --high;
            }
            else {
                break;
            }
        }
        return vector<int>({low+1, high+1});
    }
};

