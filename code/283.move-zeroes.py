#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # size = len(nums)
        # if size <= 1:
        #     return
        # non_zero = 0
        # i = 0
        # while i < size:
        #     if nums[i] != 0:
        #         i += 1
        #     else:
        #         break
        # while i < size:
        #     if nums[i] != 0:
        #         non_zero = i
        #         break
        #     i += 1
        # if i == size:
        #     return

        # i = 0
        # while non_zero < size and i < size:
        #     if nums[i] == 0:
        #         nums[i] = nums[non_zero]
        #         nums[non_zero] = 0
        #         j = non_zero + 1
        #         for j in range(non_zero+1, size):
        #             if nums[j] != 0:
        #                 non_zero = j
        #                 break
        #         if j == size:
        #             return
        #     i += 1

        size = len(nums)
        lastNonZeroFoundAt = 0
        i = 0
        while i < size:
            if nums[i] != 0:
                if i == lastNonZeroFoundAt:
                    lastNonZeroFoundAt += 1
                else:
                    nums[lastNonZeroFoundAt] = nums[i]
                    lastNonZeroFoundAt += 1
            i = i + 1
        i = lastNonZeroFoundAt
        while i < size:
            nums[i] = 0
            i += 1
# @lc code=end

