#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = (j - i) * min(height[i], height[j])
        while i < j:
            max_area = max(max_area, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                while i < j - 1 and height[i+1] <= height[i]:
                    i += 1
                i += 1
            else:
                while i + 1 < j and height[j-1] <= height[j]:
                    j -= 1            
                j -= 1

        return max_area

# @lc code=end

