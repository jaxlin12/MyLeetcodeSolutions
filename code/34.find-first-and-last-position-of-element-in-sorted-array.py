#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if not nums:
#             return [-1, -1]
        
#         left, right = 0, len(nums) - 1
#         start, end = -1, -1
#         mid = None
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 break
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         if nums[mid] != target:
#             return [-1, -1]

#         print(mid)
#         left, right = 0, mid
#         half = left + (right - left) // 2
#         while left < right:
#             half = left + (right - left) // 2
#             if nums[half] < target:
#                 left = half + 1
#             else:
#                 right = half
#         if nums[half] != target:
#             half += 1
#         start = half

#         left, right = mid, len(nums) - 1
#         half = left + (right - left) // 2        
#         while left < right:
#             half = left + (right - left) // 2
#             if nums[half] > target:
#                 right = half
#             else:
#                 left = half + 1
#         print(half)
#         if half+1 < len(nums) and nums[half + 1] == target:
#             half += 1
#         if nums[half] != target:
#             half -= 1
#         end = half
#         return [start, end]

class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]


# @lc code=end

