#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size == 0:
            return 0
        min_price = prices[0]
        max_profit = 0
        i = 0
        while i < size:
            while i < size and prices[i] < min_price:
                min_price = prices[i]
                i = i + 1

            while i < size-1 and prices[i+1] >= prices[i]:
                i = i + 1
            max_profit = max_profit + prices[i] - min_price
            if i < size-1:
                min_price = prices[i+1]
            i = i + 1

        return max_profit
            
        
# @lc code=end

