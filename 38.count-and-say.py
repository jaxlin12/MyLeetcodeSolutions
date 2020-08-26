#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        sequence = ""
        for i in range(1, n+1):
            if i == 1:
                sequence = "1"
            else:
                new_sequence = ""
                count = 0
                say = sequence[0]
                for char in sequence:
                    if char == say:
                        count = count + 1
                    else:
                        new_sequence = new_sequence + str(count) + say
                        count = 1
                        say = char
                if count != 0:
                    new_sequence = new_sequence + str(count) + say
                    
                sequence = new_sequence
        return sequence
                
# @lc code=end

