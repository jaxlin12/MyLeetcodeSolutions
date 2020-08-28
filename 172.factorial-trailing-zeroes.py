#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        pow_of_five = 5
        num_of_zeros = 0
        while n >= pow_of_five:
            num_of_zeros += n // pow_of_five
            pow_of_five *= 5
        return num_of_zeros
        
# @lc code=end

