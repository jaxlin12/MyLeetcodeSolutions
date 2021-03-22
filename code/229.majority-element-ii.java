import java.util.List;

/*
 * @lc app=leetcode id=229 lang=java
 *
 * [229] Majority Element II
 */
import java.util.*;
// @lc code=start
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int threshold = nums.length / 3;
        List<Integer> ret = new ArrayList<Integer>();
        int count1 = 0;
        int count2 = 0;
        int candidate1 = 0;
        int candidate2 = 1;
        for (int i = 0;i < nums.length;i++) {
            if (nums[i] == candidate1) {
                count1++;
            }
            else if(nums[i] == candidate2) {
                count2++;
            }
            else if(count1 == 0) {
                count1 = 1;
                candidate1 = nums[i];
            }
            else if(count2 == 0) {
                count2 = 1;
                candidate2 = nums[i];
            }
            else {
                count1--;
                count2--;
            }
        }
        count1 = count2 = 0;
        for (int i = 0;i < nums.length;i++) {
            if(nums[i] == candidate1) {
                count1++;
            }
            else if(nums[i] == candidate2) {
                count2++;
            }
        }

        if(count1 > threshold) {
            ret.add(candidate1);
        }
        if(count2 > threshold) {
            ret.add(candidate2);
        }
        return ret;
        



    }
}
// @lc code=end

