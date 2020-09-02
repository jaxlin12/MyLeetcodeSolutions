#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        height = len(grid)
        if height == 0:
            return 0
        perimeter = 0
        width = len(grid[0])
        if width == 0:
            return 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    perimeter += 0 > (i - 1) or grid[i-1][j] == 0
                    perimeter += (i + 1) >= height or grid[i+1][j] == 0
                    perimeter += 0 > (j - 1) or grid[i][j-1] == 0
                    perimeter += (j + 1) >= width or grid[i][j+1] == 0
        return perimeter
                

# @lc code=end

