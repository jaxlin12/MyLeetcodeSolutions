#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     height = len(matrix)
    #     if height == 0:
    #         return False
    #     width = len(matrix[0])
    #     if width == 0:
    #         return False

    #     left = 0
    #     right = height - 1
    #     while left <= right:
    #         mid = left + (right - left) // 2
    #         if matrix[mid][0] == target:
    #             return True
    #         elif matrix[mid][0] > target:
    #             right = mid - 1
    #         else:
    #             left = mid + 1

    #     left -= 1

    #     i = left
    #     left = 0
    #     right = width - 1
    #     while left <= right:
    #         mid = left + (right - left) // 2
    #         if matrix[i][mid] == target:
    #             return True
    #         elif matrix[i][mid] > target:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     return False

    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

# @lc code=end

