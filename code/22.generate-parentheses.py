#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def backtracking(self, left, right, str):
        if left == 0 and right == 0:
            self.str.append(str)
            return
        if left >= 1:
            self.backtracking(left-1, right, str+'(')
        if right > left:
            self.backtracking(left, right-1, str+')')

    def generateParenthesis(self, n: int) -> List[str]:
        self.str = []
        self.backtracking(n,n,"")
        return self.str

# @lc code=end

