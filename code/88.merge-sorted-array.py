#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        elif n == 0:
            return

        mark = [0] * (m+1)
        i = 0
        j = 0
        while i < m and j < n:
            if nums2[j] < nums1[i]:
                mark[i] = mark[i] + 1
                j = j + 1
            else:
                i = i + 1
        while j < n:
            mark[m] = mark[m] + 1
            j = j + 1
        
        i = m - 1
        j = n - 1
        k = m + n - 1
        while k >= 0 and i >= 0:
            for _ in range(mark[i+1]):
                nums1[k] = nums2[j]
                j = j - 1
                k = k - 1
            nums1[k] = nums1[i]
            i = i - 1
            k = k - 1
        for _ in range(mark[0]):
            nums1[k] = nums2[j]
            j = j - 1
            k = k - 1
# @lc code=end

