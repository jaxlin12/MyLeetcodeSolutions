#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        num = 0
        pow_of_2 = 1
        for i in range(31):
            num = (num + n % 2) * 2
            n = n // 2
        num = num + n % 2
        return num
# @lc code=end

