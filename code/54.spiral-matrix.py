#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        upper_bound = 0
        lower_bound = len(matrix)
        left_bound = 0
        right_bound = len(matrix[0])
        i = j = k = 0
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []
        count = 0
        size = lower_bound * right_bound
        while count != size:
            while upper_bound <= i < lower_bound and left_bound <= j < right_bound:
                res.append(matrix[i][j])
                count += 1
                i += direction[k][0]
                j += direction[k][1]
            if direction[k][0] == -1:
                left_bound += 1
                i += 1
                j += 1
            elif direction[k][0] == 1:
                right_bound -= 1
                i -= 1
                j -= 1
            elif direction[k][1] == -1:
                lower_bound -= 1
                i -= 1
                j += 1
            else:
                upper_bound += 1
                i += 1
                j -= 1
            k += 1
            k %= 4
        return res




# @lc code=end

