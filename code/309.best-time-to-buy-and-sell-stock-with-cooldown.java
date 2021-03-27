/*
 * @lc app=leetcode id=309 lang=java
 *
 * [309] Best Time to Buy and Sell Stock with Cooldown
 */

// @lc code=start
class Solution {
    /*
        There are three states, according to the action that you can take.

        Hence, from there, you can now the profit at a state at time i as:

        s0[i] = max(s0[i - 1], s2[i - 1]); // Stay at s0, or rest from s2
        s1[i] = max(s1[i - 1], s0[i - 1] - prices[i]); // Stay at s1, or buy from s0
        s2[i] = s1[i - 1] + prices[i]; // Only one way from s1
        Then, you just find the maximum of s0[n] and s2[n], since they will be the maximum profit we need (No one can buy stock and left with more profit that sell right :) )

        Define base case:
    */
    public int maxProfit(int[] prices) {
        if (prices.length <= 1) return 0;
        int[] s0 = new int[prices.length];
        int[] s1 = new int[prices.length];
        int[] s2 = new int[prices.length];
        s0[0] = 0; // At the start, you don't have any stock if you just rest
        s1[0] = -prices[0]; // After buy, you should have -prices[0] profit. Be positive!
        s2[0] = Integer.MIN_VALUE;// Lower base case
        for (int i = 1; i < prices.length; i++) {
            s0[i] = Math.max(s0[i - 1], s2[i - 1]);
            s1[i] = Math.max(s1[i - 1], s0[i - 1] - prices[i]);
            s2[i] = s1[i - 1] + prices[i];
        }
        return Math.max(s0[prices.length - 1], s2[prices.length - 1]);       
    }
}
// @lc code=end

