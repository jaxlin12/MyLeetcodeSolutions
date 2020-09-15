#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def factorial(self, n):
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

    def uniquePaths(self, m: int, n: int) -> int:
        if n == 0 or m == 0:
            return 0
        elif n == 1 or m == 1:
            return 1
        
        m -= 1
        n -= 1
        total = m + n
        combination = self.factorial(total) // (self.factorial(m) * self.factorial(n))
        return combination
        
# @lc code=end

