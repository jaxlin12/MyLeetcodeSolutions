#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    # def generateOutter(self, matrix, n, num, i, j):
    #     if n < 1:
    #         return
    #     if n == 1:
    #         matrix[i][j] = num + 1
    #         return
        
    #     for x in range(1, n):
    #         matrix[i][j+x] = num + x + 1
    #         matrix[i+x][j+n-1] = num + x + n
    #         matrix[i+n-1][j+n-1-x] = num + x + 2*n - 1
    #         matrix[i+n-1-x][j] = num + x + 3*n - 2
    #     matrix[i][j] = num + 1
    #     self.generateOutter(matrix, n-2, matrix[i+1][j], i+1, j+1)
            

    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for i in range(n):
            matrix.append([None] * n)

        i = 0
        j = 0

        if n < 1:
            return
        num = 0
        while n >= 1:
            if n == 1:
                matrix[i][j] = num + 1
                break
            for x in range(1, n):
                matrix[i][j+x] = num + x + 1
                matrix[i+x][j+n-1] = num + x + n
                matrix[i+n-1][j+n-1-x] = num + x + 2*n - 1
                matrix[i+n-1-x][j] = num + x + 3*n - 2
            matrix[i][j] = num + 1
            num = matrix[i+1][j]
            n = n - 2
            i = i + 1
            j = j + 1

        return matrix
        
# @lc code=end

