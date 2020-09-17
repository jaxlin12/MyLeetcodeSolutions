#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def check(self, i, j, word, visted):
        if (i,j) in visted:
            return False
        if not (0 <= i < self.height):
            return False
        if not (0 <= j < self.width):
            return False
        if self.board[i][j] == word[0]:
            if len(word) == 1:
                return True
            visted.append((i, j))
            if not (self.check(i-1, j, word[1:], visted) or self.check(i+1, j, word[1:], visted) or self.check(i, j-1, word[1:], visted) or self.check(i, j+1, word[1:], visted)):
                visted.pop()
                return False
            return True
        else:
            return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        self.height = len(board)
        if self.height == 0:
            return False
        self.width = len(board[0])
        if self.width == 0:
            return False
        self.board = board
        for i in range(self.height):
            for j in range(self.width):
                if self.check(i, j, word, []):
                    return True

        return False
        
# @lc code=end

