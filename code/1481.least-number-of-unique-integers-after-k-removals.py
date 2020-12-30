#
# @lc app=leetcode id=1481 lang=python3
#
# [1481] Least Number of Unique Integers after K Removals
#

# @lc code=start
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        def sorted_func(a):
            return freq[a]
        key_list = list(freq.keys())
        key_list.sort(key=sorted_func)
        for i in range(len(key_list)):
            k -= freq[key_list[i]]
            if k == 0:
                return len(key_list) - i - 1
            elif k < 0:
                return len(key_list) - i

            

        
# @lc code=end

