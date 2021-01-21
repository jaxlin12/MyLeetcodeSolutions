#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def binary_search_row(self, matrix, row, low, high, target):
        ret = (-1, -1)
        while low < high:
            mid = low + (high - low) // 2
            if matrix[row][mid] == target:
                return (mid, mid)
            elif matrix[row][mid] > target:
                high = mid-1
                ret = (low, mid)
            else:
                low = mid+1
                ret = (mid, high)
        return ret

    def binary_search_col(self, matrix, col, low, high, target):
        ret = -1
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[mid][col] == target:
                return mid
            elif matrix[mid][col] > target:
                high = mid-1
            else:
                low = mid+1
        return ret

    def binary_search_col2(self, matrix, col, low, high, target):
        ret = (-1, -1)
        while low < high:
            mid = low + (high - low) // 2
            if matrix[mid][col] == target:
                return (mid, mid)
            elif matrix[mid][col] > target:
                high = mid-1
                ret = (low, mid)
            else:
                low = mid+1
                ret = (mid, high)
        return ret

    def binary_search_row2(self, matrix, row, low, high, target):
        ret = -1
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[row][mid] == target:
                return mid
            elif matrix[row][mid] > target:
                high = mid-1
            else:
                low = mid+1
        return ret

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = high = -1

        for i in range(m):
            low, high = self.binary_search_row(matrix, i, 0, n-1, target)
            if matrix[i][low] == target or matrix[i][high] == target:
                return True
            elif target > matrix[i][low] and target < matrix[i][high]:
                break
        for i in range(0, high+1):
            ret = self.binary_search_col(matrix, i, 0, m-1, target)
            if ret != -1:
                return True

        low = high = -1

        for i in range(n):
            low, high = self.binary_search_col2(matrix, i, 0, m-1, target)
            if matrix[low][i] == target or matrix[high][i] == target:
                return True
            elif target > matrix[low][i] and target < matrix[high][i]:
                break

        for i in range(0, high+1):
            ret = self.binary_search_row2(matrix, i, 0, n-1, target)
            if ret != -1:
                return True
        return False
        
# @lc code=end

