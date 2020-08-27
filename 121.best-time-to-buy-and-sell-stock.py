#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        min_price = prices[0]
        max_profit = 0
        for num in prices:
            if num <= min_price:
                min_price = num
            else:
                profit = num - min_price
                max_profit = max(max_profit, profit)
        return max_profit
# @lc code=end

