#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        for i in range(1,n+1): 
            fact = fact * i

        string = ""
        numbers = list(range(1, n+1))
        while n > 1:
            fact //= n
            temp = k // fact + (not not(k % fact))
            string += str(numbers[temp-1])
            numbers.remove(numbers[temp-1])
            k %= fact
            n -= 1

        string += str(numbers[0])
        return string
        
# @lc code=end

