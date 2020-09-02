#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x
        while l < r:
            mid = (l+r) // 2
            if x < mid*mid:
                r = mid
            else:
                l = mid + 1
        return l-1 if l>1 else l
        
# @lc code=end

