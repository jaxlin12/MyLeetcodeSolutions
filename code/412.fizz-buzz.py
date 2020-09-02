#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []
        count3 = 1
        count5 = 1
        for i in range(1, n+1):
            string = ""
            if not count3:
                string += "Fizz"
            if not count5:
                string += "Buzz"
            if string == "":
                string = str(i)
            ret.append(string)
            count3 = (count3 + 1) % 3
            count5 = (count5 + 1) % 5
        return ret
# @lc code=end

