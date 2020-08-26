#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry_out = 0
        size = len(digits)
        digits[-1] = digits[-1] + 1
        for index in range(size-1, -1, -1):
            digits[index] = digits[index] + carry_out
            carry_out = int(digits[index] / 10)
            digits[index] = digits[index] % 10
        if carry_out > 0:
            digits.insert(0, carry_out)
        return digits

# @lc code=end

