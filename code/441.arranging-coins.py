#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 0:
            return 0
        return int((2 * n + 0.25) ** 0.5 - 0.5)
            
# @lc code=end

