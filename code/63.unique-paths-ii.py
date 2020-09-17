#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def move(self, i, j):
        if i >= self.height:
            return 0
        if j >= self.width:
            return 0
        if self.obstacleGrid[i][j] == 1:
            self.ways[i][j] = 0
            return 0
        if i == self.height - 1 and j == self.width - 1:
            return 1

        if self.ways[i][j] != None:
            return self.ways[i][j]

        self.ways[i][j] = self.move(i+1, j) + self.move(i, j+1)
        return self.ways[i][j]


    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.obstacleGrid = obstacleGrid
        self.height = len(obstacleGrid)
        if self.height == 0:
            return 0
        self.width = len(obstacleGrid[0])
        if self.width == 0:
            return 0
        if self.obstacleGrid[-1][-1] == 1 or self.obstacleGrid[0][0] == 1:
            return 0
        self.ways = []
        for i in range(self.height):
            self.ways.append([None] * self.width)
            for j in range(self.width):
                if obstacleGrid[i][j] == 1:
                    self.ways[i][j] = 0
    
        return self.move(0,0)


# @lc code=end

