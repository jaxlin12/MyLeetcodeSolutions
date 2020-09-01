#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hours_digit = 0
        minutes_digit = 0
        ret = []
        while hours_digit <= num and hours_digit <= 4:
            minutes_digit = num - hours_digit
            if minutes_digit <= num and minutes_digit <= 6:
                hours = combinations([1,2,4,8], hours_digit)
                minutes = combinations([1,2,4,8,16,32], minutes_digit)
                sum1 = []
                sum2 = []
                for num1 in hours:
                    sum1.append(sum(num1))
                for num2 in minutes:
                    sum2.append(sum(num2))
                for num1 in sum1:
                    if num1 < 12:
                        for num2 in sum2:
                            if num2 < 60:
                                ret.append(f"{num1}:{num2:02d}")
            hours_digit += 1
        return ret

# @lc code=end

