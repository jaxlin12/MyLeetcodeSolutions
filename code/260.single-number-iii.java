/*
 * @lc app=leetcode id=260 lang=java
 *
 * [260] Single Number III
 */

// @lc code=start
class Solution {
    public int[] singleNumber(int[] nums) {
        int [] ret = new int[2];
        int mask = 0;
        int mask1 = 0;
        for (int n : nums) {
            mask ^= n;
        }
        for (int i = 0; i < 32;i++) {
            if((mask & (1 << i)) == (1 << i)) {
                mask1 = (1<<i);
                break;
            }
        }

        int mask2 = 0;
        for (int n : nums) {
            if((n & mask1) == mask1) {
                mask2 ^= n;
            }
        }
        ret[0] = mask2 | mask1;
        ret[1] = mask ^ ret[0];
        return ret;
    }
}
// @lc code=end

