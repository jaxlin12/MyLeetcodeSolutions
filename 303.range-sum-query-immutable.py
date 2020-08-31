#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.size = len(nums)
        self.the_sum = [None] * self.size
        if self.size != 0:
            self.the_sum[0] = nums[0]
        self.last_calculate = 0
    
    def sumRange(self, i: int, j: int) -> int:
        if i == j:
            return self.nums[i]
        if not 0 <= i < j < self.size:
            return None

        if self.the_sum[j] == None:
            for k in range(self.last_calculate + 1, j+1):
                self.the_sum[k] = self.the_sum[k - 1] + self.nums[k]
            self.last_calculate = k
        if i == 0:
            return self.the_sum[j]

        return self.the_sum[j] - self.the_sum[i-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

