#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x = -x

        starting_zero = False
        num_of_digits = 0
        temp_x = x / 10
        while(int(temp_x) != 0):
            temp_x = temp_x / 10
            num_of_digits = num_of_digits + 1
        dividend = pow(10, num_of_digits)
        
        temp_x = x
        new_x = 0
        i = 0
        while dividend >= 1:
            new_x = new_x + int(temp_x / dividend)  * pow(10, i)
            temp_x = temp_x % dividend
            dividend = dividend / 10
            i = i + 1
        if is_negative:
            x = -x
            new_x = -new_x
        int_max = pow(2, 31)
        if new_x > int_max - 1 or new_x < -int_max:
            return 0
        return new_x

        
# @lc code=end

