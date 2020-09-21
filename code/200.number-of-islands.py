#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        if height == 0:
            return 0
        width = len(grid[0])
        if width == 0:
            return 0

        queue = collections.deque()
        count = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1":
                    queue.append((i, j))
                    count += 1
                    while len(queue) != 0:
                        m,n = queue.pop()
                        if 0<=m<height and 0<=n<width and grid[m][n] == "1":
                            grid[m][n] = "0"
                            queue.append((m+1, n))
                            queue.append((m-1, n))
                            queue.append((m, n+1))
                            queue.append((m, n-1))
        return count
        


        
# @lc code=end

