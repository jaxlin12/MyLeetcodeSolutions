#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k = k % size
        if k == 0:
            return
        if size == 0 or size == 1:
            return
        start = 0
        save = nums[0]
        i = 0
        j = 0
        is_cycle = False
        while j < size:
            temp = save
            save = nums[(i + k) % size]
            nums[(i + k) % size] = temp
            if is_cycle:
                start = start + 1
                i = start
                save = nums[i]
                j = j - 1
                is_cycle = False
            else:
                if (i + k) % size == start:
                    is_cycle = True
                    i = (i + k) % size
                elif i + k >= size:
                    i = (i + k) % size
                else:
                    i = (i + k) % size
            j = j + 1
            
# @lc code=end

