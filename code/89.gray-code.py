#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        def gray(n):
            return n^(n>>1)
        
        ans = []
        for i in range(2**n):
            ans.append(gray(i))
        return ans
# @lc code=end

