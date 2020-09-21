#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        str1 = version1.split('.')
        str2 = version2.split('.')
        size1 = len(str1)
        size2 = len(str2)
        i = j = 0
        while i < size1 and j < size2:
            int1 = int(str1[i])
            int2 = int(str2[j])
            if int1 > int2:
                return 1
            elif int1 < int2:
                return -1
            i += 1
            j += 1
        if size1 > size2:
            while i < size1:
                if int(str1[i]) != 0:
                    return 1
                i += 1
        elif size1 < size2:
            while j < size2:
                if int(str2[j]) != 0:
                    return -1
                j += 1
        return 0


# @lc code=end

