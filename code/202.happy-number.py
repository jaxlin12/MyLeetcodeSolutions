#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        loop = 0
        while loop < 6:
            new_n = 0
            while n > 0:
                digit = n % 10
                new_n += digit * digit
                n = n // 10
            n = new_n
            if n == 0:
                return False
            if n == 1:
                return True
            loop += 1
        return False

# @lc code=end

