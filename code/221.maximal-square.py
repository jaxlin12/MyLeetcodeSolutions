#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         if len(matrix) == 0 or len(matrix[0]) == 0:
#             return 0
#         low = 1
#         high = min(len(matrix), len(matrix[0]))+1
#         maxLength = 0
#         while low <= high:
#             mid = low + (high - low) // 2
#             ret = self.searchSquare(matrix, mid)
#             if ret:
#                 maxLength = mid * mid
#                 low = mid+1
#             else:
#                 high = mid-1
#         return maxLength
        
#     def searchSquare(self, matrix, sideLength):
#         ret = False
#         for row in range(len(matrix)-sideLength+1):
#             for col in range(len(matrix[0])-sideLength+1): 
#                 if matrix[row][col] != '0':
#                     ret = True
#                     for i in range(sideLength):
#                         for j in range(sideLength):
#                             if matrix[row+i][col+j] == '0':
#                                 ret = False
#                                 break
#                         if ret == False:
#                             break
#                     if ret == True:
#                         return True
#         return ret
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1 # Be careful of the indexing since dp grid has additional row and column
                    max_side = max(max_side, dp[r+1][c+1])
                
        return max_side * max_side
        
# @lc code=end

