#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 or num == 0:
            return True
        if num < 0:
            return False
        lo, hi = 0, num
        mid = lo + (hi - lo) // 2
        while lo < hi and lo != mid:
            if num > mid * mid:
                lo = mid
            elif num < mid * mid:
                hi = mid
            else:
                return True      
            mid = lo + (hi - lo) // 2  
        return False
# @lc code=end

