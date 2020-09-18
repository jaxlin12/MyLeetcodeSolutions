#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        index = 0
        count = 0
        size = len(nums)
        if size == 0:
            return 0
        temp = nums[0]
        while i < size:
            if nums[i] == temp:
                if count == 2:
                    index = i
                    break
                else:
                    count += 1
            else:
                temp = nums[i]
                count = 1
            i += 1
        if i == size:
            return i
        while i < size:
            if nums[i] == temp:
                i += 1
            else:
                break
        count = 0
        if i == size:
            return index
        temp = nums[i]
        count = 0
        while i < size:
            if nums[i] == temp:
                if count < 2:
                    count += 1
                    nums[index] = nums[i]
                    index += 1
            else:
                temp = nums[i]
                count = 1
                nums[index] = nums[i]
                index += 1
            i += 1
        return index

        
# @lc code=end

