#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        size = len(x_str)
        is_odd = False
        if size % 2 == 1:
            is_odd = True
        mid = int(size / 2)
        if is_odd:
            l, r = mid-1, mid+1
        else:
            l, r = mid-1, mid
        while l >= 0:
            if x_str[l] != x_str[r]:
                return False
            l = l - 1
            r = r + 1
        return True


    # Without converting to str:
        # if x < 0:
        #     return False

        # temp_x = x / 10
        # dividend = 1
        # while(int(temp_x) != 0):
        #     temp_x = temp_x / 10
        #     dividend = dividend * 10

        # temp_x = x
        # while temp_x != 0:
        #     left = int(temp_x / dividend)
        #     right = temp_x % 10
        #     if left != right:
        #         return False
        #     temp_x = int((temp_x % dividend) / 10)
        #     dividend = int(dividend / 100)
        # return True

# @lc code=end

