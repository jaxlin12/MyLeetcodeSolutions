#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def dp(self, i, j):
        if i == self.size1 and j == self.size2:
            return True
        elif i >= self.size1:
            for k in range(j, self.size2):
                if self.p[k] != '*':
                    return False
            return True
        elif j >= self.size2:
            return False
        elif self.memory[i][j] != None:
            return self.memory[i][j]


        if self.s[i] == self.p[j]:
            self.memory[i][j] = self.dp(i+1, j+1)
        elif self.p[j] == '?':
            self.memory[i][j] = self.dp(i+1, j+1)
        elif self.p[j] == '*':
            self.memory[i][j] = self.dp(i, j+1) or self.dp(i+1, j+1) or self.dp(i+1, j)
        return self.memory[i][j]


    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = p
        self.size1 = len(s)
        self.size2 = len(p)
        if self.size1 == 0 and self.size2 == 0:
            return True
        elif self.size1 == 0:
            for c in p:
                if c != '*':
                    return False
            return True
        elif self.size2 == 0:
            return False
        self.memory = []
        for _ in range(self.size1):
            self.memory.append([None] * self.size2)
        self.dp(0, 0)
        return self.memory[0][0]
        
# @lc code=end

