#
# @lc app=leetcode id=537 lang=python3
#
# [537] Complex Number Multiplication
#

# @lc code=start
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a = a.split('+')
        b = b.split('+')
        for i in range(len(a)-1):
            a[i] = int(a[i])
        a[-1] = int(a[-1][:-1])
        for i in range(len(b)-1):
            b[i] = int(b[i])
        b[-1] = int(b[-1][:-1])

        real = a[0] * b[0]
        imaginary = a[1] * b[1]
        realImaginary = a[0] * b[1]
        imaginaryReal = a[1] * b[0]
        real = real - imaginary
        imaginary = realImaginary + imaginaryReal

        return f"{real}+{imaginary}i"
        



        
# @lc code=end

