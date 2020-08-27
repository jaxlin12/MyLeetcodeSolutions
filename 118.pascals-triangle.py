#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        rows = [[1], [1, 1]]
        for i in range(2, numRows):
            rows.append([1] * (len(rows[i-1])+1))
            k = 1
            for j in range(len(rows[i-1])-1):
                rows[i][k] = rows[i-1][j] + rows[i-1][j+1]
                k = k + 1
        return rows


            
# @lc code=end

