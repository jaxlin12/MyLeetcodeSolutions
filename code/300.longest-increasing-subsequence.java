/*
 * @lc app=leetcode id=300 lang=java
 *
 * [300] Longest Increasing Subsequence
 */

// @lc code=start
class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int [] memo = new int[n];
        memo[0] = 1;
        int maxRet = 1;
        for (int i = 1;i < n;i++) {
            int maxDP = 1;
            for (int j = 0;j < i;j++) {
                if(nums[j] < nums[i]) {
                    maxDP = Math.max(memo[j]+1, maxDP);
                }
            }
            memo[i] = maxDP;
            maxRet = Math.max(maxRet, maxDP);
        }
        return maxRet;
    }
}

// input: [0, 8, 4, 12, 2]

// dp: [0]

// dp: [0, 8]

// dp: [0, 4]

// dp: [0, 4, 12]

// dp: [0 , 2, 12]  which is not the longest increasing subsequence, but length of dpdp array 
// results in length of Longest Increasing Subsequence.

// @lc code=start
// class Solution {
//         public int lengthOfLIS(int[] nums) {
//             int[] dp = new int[nums.length];
//             int len = 0;
//             for (int num : nums) {
//                 int i = Arrays.binarySearch(dp, 0, len, num);
//                 if (i < 0) {
//                     i = -(i + 1);
//                 }
//                 dp[i] = num;
//                 if (i == len) {
//                     len++;
//                 }
//             }
//             return len;
//         }
// }
// @lc code=end

