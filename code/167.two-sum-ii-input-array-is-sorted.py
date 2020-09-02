#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        i = 0
        j = size - 1
        while i < j:
            the_sum = numbers[i] + numbers[j]
            if the_sum == target:
                return [i+1, j+1]
            elif the_sum < target:
                i = i + 1
            else:
                j = j - 1
        return None
# @lc code=end

