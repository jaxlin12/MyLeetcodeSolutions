/*
 * @lc app=leetcode id=122 lang=cpp
 *
 * [122] Best Time to Buy and Sell Stock II
 */
class Solution {
    public:
    int maxProfit(vector<int>& prices) {
        int maxprofit = 0;
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] > prices[i - 1])
                maxprofit += prices[i] - prices[i - 1];
        }
        return maxprofit;
    }
};

