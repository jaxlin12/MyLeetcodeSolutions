/*
 * @lc app=leetcode id=334 lang=java
 *
 * [334] Increasing Triplet Subsequence
 */

// @lc code=start
class Solution {
    public boolean increasingTriplet(int[] nums) {
        int first = Integer.MAX_VALUE;
        int second = Integer.MAX_VALUE;
        for(int i = 0;i < nums.length;i++) {
            if(nums[i] < first) {
                first = nums[i];
            }
            else if(nums[i] < second && nums[i] != first) {
                second = nums[i];
            }
            else if(nums[i] != first && nums[i] != second) {
                return true;
            }
        }
        return false;
    }
}
// @lc code=end

