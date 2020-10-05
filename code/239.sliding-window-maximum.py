#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k == 0:
            return []
        dq = collections.deque()
        for i in range(k):
            while dq:
                if nums[dq[-1]] <= nums[i]:
                    dq.pop()
                else:
                    break
            dq.append(i)
        res = []
        for i in range(k, len(nums)):
            res.append(nums[dq[0]])
            while dq:
                if nums[dq[-1]] <= nums[i]:
                    dq.pop()
                else:
                    break
            if dq and dq[0] + k <= i:
                dq.popleft()
            dq.append(i)
        res.append(nums[dq[0]])
        return res

# @lc code=end

