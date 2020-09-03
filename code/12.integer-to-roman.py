#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    # def intToRoman(self, num: int) -> str:
    #     dictionary = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M",
    #                   4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM"}
    #     quotient = [1,4,5,9]
    #     i = 1000
    #     new_str = ""
    #     while num > 0:
    #         quo = num // i
    #         if quo in quotient:
    #             new_str += dictionary[quo * i]
    #         else:
    #             if quo > 5:
    #                 new_str += dictionary[5*i]
    #                 quo -= 5
    #             for _ in range(quo):
    #                 new_str += dictionary[i]
    #         num %= i
    #         i //= 10

    #     return new_str
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ""
        for n, v in zip(numerals, values):
            res += (num // v) * n
            num %= v 
        return res
        
# @lc code=end

