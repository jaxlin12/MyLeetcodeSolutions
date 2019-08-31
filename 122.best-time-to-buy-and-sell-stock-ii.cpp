/*
 * @lc app=leetcode id=122 lang=cpp
 *
 * [122] Best Time to Buy and Sell Stock II
 */
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int size = prices.size();
        if(size < 2) return 0;
        int vallyIndex = 0;
        int maxProfit = 0;
        int i = 1;
        while(prices[i] <= prices[vallyIndex] && i < size-1) {
            vallyIndex = i;
            ++i;
        }
        for(i -= 1;i < size-1;++i) {
            if(prices[i] > prices[vallyIndex] && prices[i] >= prices[i+1]) {
                maxProfit = maxProfit + prices[i] - prices[vallyIndex];
                vallyIndex = i;
                ++i;
                while(prices[i] <= prices[vallyIndex] && i < size-1) {
                    vallyIndex = i;
                    ++i;
                }
                --i;
            }
        }
        if(vallyIndex < size - 1 && prices[size - 1] > prices[vallyIndex])
            maxProfit += prices[size - 1] - prices[vallyIndex];
        return maxProfit;
    }
};

