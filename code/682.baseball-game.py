#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for s in ops:
            if s == "C":
                stack.pop()
            elif s == "D":
                stack.append(stack[-1] * 2)
            elif s == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(s))
        return sum(stack)
        
# @lc code=end

