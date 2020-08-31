#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        # if num < 0:
        #     return False
        # if num <= 6 and num > 0:
        #     return True
        # prime = 2
        # while num >= prime ** 2:
        #     if num % prime == 0:
        #         if prime != 2 and prime != 3 and prime != 5:
        #             return False
        #         num = num // prime
        #     else:
        #         prime += 1
        # if num != 2 and num != 3 and num != 5:
        #     return False
        # return True
        
        if (num <= 0): return False
        # while (num % 2 == 0): num //= 2
        # while (num % 3 == 0): num //= 3
        # while (num % 5 == 0): num //= 5
        # return num == 1;

        for p in 2, 3, 5:
            while num % p == 0:
                num /= p
        return num == 1

# @lc code=end

