#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        sequences = collections.defaultdict(int) #set '0' as the default value for non-existing keys
        for i in range(len(s)):
            sequences[s[i:i+10]] += 1#add 1 to the count
        
        ret = []
        for key in sequences: 
            if sequences[key] > 1:
                ret.append(key)
        return ret
            
        
        
# @lc code=end

