#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        def sort_func(k):
            return k[1]

        cur, ans = float('-inf'), 0
        for x, y in sorted(pairs, key =sort_func):
            if cur < x:
                cur = y
                ans += 1
        return ans

# @lc code=end

