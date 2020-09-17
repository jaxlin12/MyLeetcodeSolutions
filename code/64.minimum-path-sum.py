#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:    
    def move(self, i, j):
        if i >= self.height:
            return None
        if j >= self.width:
            return None
        if i == self.height - 1 and j == self.width - 1:
            return self.grid[i][j]
        if self.ways[i][j] != None:
            return self.ways[i][j]
        down = self.move(i+1, j)
        right = self.move(i, j+1)
        if down == None and right == None:
            self.ways[i][j] = self.grid[i][j]
        elif down == None:
            self.ways[i][j] = self.grid[i][j] + right
        elif right == None:
            self.ways[i][j] = self.grid[i][j] + down
        else:
            self.ways[i][j] = self.grid[i][j] + min(down, right)
        return self.ways[i][j]


    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.height = len(grid)
        if self.height == 0:
            return 0
        self.width = len(grid[0])
        if self.width == 0:
            return 0
        self.ways = []
        for i in range(self.height):
            self.ways.append([None] * self.width)
    
        return self.move(0,0)
# @lc code=end

