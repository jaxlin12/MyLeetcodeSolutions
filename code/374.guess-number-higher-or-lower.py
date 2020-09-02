#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            half = lo + (hi - lo) // 2
            result = guess(half)
            if result == -1:
                hi = half - 1
            elif result == 1:
                lo = half + 1
            else:
                return half
        return -1
        
# @lc code=end

