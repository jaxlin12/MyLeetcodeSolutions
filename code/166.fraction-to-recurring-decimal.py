#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0:
            return ""
        sign = 1
        if numerator < 0 and denominator < 0:
            sign = 1
        elif numerator < 0 or denominator < 0:
            sign = -1
        numerator = abs(numerator)
        denominator = abs(denominator)

        integer = ""
        fraction = ""
        while numerator >= denominator:
            integer += str(numerator // denominator)
            numerator = numerator % denominator
        if integer == "":
            integer = "0"
        
        repeat = {}
        i = 0
        while numerator != 0:
            if numerator not in repeat:
                repeat[numerator] = i
            else:
                i = repeat[numerator]
                fraction = fraction[:i] + '(' + fraction[i:] + ')'
                break
            numerator *= 10
            if numerator < denominator:
                fraction += "0"
            else:
                fraction += str(numerator // denominator)
                numerator = numerator % denominator
            i += 1
        

        string = ""
        if fraction == "":
            string += integer
        else:
            string = integer + '.' + fraction
        if string != "0":
            if sign == -1:
                string = '-' + string
        return string

        
# @lc code=end

