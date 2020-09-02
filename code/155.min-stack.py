#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([x, x])
        else:
            self.stack.append([x, min(self.stack[-1][1], x)])

    def pop(self) -> None:
        if len(self.stack) != 0:
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

