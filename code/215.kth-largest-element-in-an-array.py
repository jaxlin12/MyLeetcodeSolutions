#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     nums.sort()
    #     return nums[-k]
    def findKthLargest(self, nums, k):
        # QuickSelect idea: AC in 52 ms
        # ---------------------------
        #
        pivot = nums[randint(0, len(nums) - 1)]

        right = [r for r in nums if r > pivot]
        if k <= len(right):
            return self.findKthLargest(right, k)
        equal = [e for e in nums if e == pivot]
        if (k - len(right)) <= len(equal):
            return equal[0]
        left  = [l for l in nums if l < pivot]
        return self.findKthLargest(left, k - len(right) - len(equal))


# @lc code=end

