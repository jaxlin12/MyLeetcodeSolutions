#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def subRotate(self, matrix, start, n):
        if n <= 1:
            return
        save = matrix[start][start:start+n]
        for i in range(0, n-1):
            matrix[start][start+i] = matrix[start+n-1-i][start]
            matrix[start+n-1-i][start] = matrix[start+n-1][start+n-1-i]
            matrix[start+n-1][start+n-1-i] = matrix[start+i][start+n-1]
            matrix[start+i][start+n-1] = save[i]
        self.subRotate(matrix, start+1, n-2)

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        width = len(matrix[0])
        if height == 0 or width == 0 or height != width:
            return
        self.subRotate(matrix, 0, height)

        
# @lc code=end

