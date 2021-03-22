/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start
import java.util.*;
import java.io.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
        int[] ret = new int[2];
        for (int i = 0;i < nums.length;i++) {
            if (hash.containsKey(nums[i])) {
                ret[0] = hash.get(nums[i]);
                ret[1] = i;
                return ret;
            }
            else {
                hash.put(target-nums[i], i);
            }
        }
        return ret;
    }
}

// @lc code=end

