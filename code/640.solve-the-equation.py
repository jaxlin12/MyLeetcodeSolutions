#
# @lc app=leetcode id=640 lang=python3
#
# [640] Solve the Equation
#

# @lc code=start
class Solution:
    def solveEquation(self, equation: str) -> str:
        lhs, rhs = equation.split('=', 2)
        print(lhs, rhs)
        x_count = 0
        num_count = 0
        operator = 1
        i = 0
        if lhs[0] == '-':
            operator = -1
            i = 1
        while i < len(lhs):
            j = i
            while j < len(lhs) and lhs[j] != '+' and lhs[j] != '-' and lhs[j] != 'x':
                j = j + 1;
            if j == len(lhs):
                num_count = num_count + operator * int(lhs[i:j])
            elif lhs[j] == '+':
                num_count = num_count + operator * int(lhs[i:j])
                operator = 1
            elif lhs[j] == '-':
                num_count = num_count + operator * int(lhs[i:j])
                operator = -1
            elif lhs[j] == 'x':
                if i == j:
                    x_count = x_count + operator
                else:
                    x_count = x_count + operator * int(lhs[i:j])
                j = j + 1
                if j < len(lhs):
                    if lhs[j]== '+':
                        operator = 1
                    elif lhs[j] == '-':
                        operator = -1
            i = j + 1

        operator = -1
        i = 0
        if rhs[0] == '-':
            operator = 1
            i = 1
        while i < len(rhs):
            j = i
            while j < len(rhs) and rhs[j] != '+' and rhs[j] != '-' and rhs[j] != 'x':
                j = j + 1;
            if j == len(rhs):
                num_count = num_count + operator * int(rhs[i:j])
            elif rhs[j] == '+':
                num_count = num_count + operator * int(rhs[i:j])
                operator = -1
            elif rhs[j] == '-':
                num_count = num_count + operator * int(rhs[i:j])
                operator = 1
            elif rhs[j] == 'x':
                if i == j:
                    x_count = x_count + operator
                else:
                    x_count = x_count + operator * int(rhs[i:j])
                j = j + 1
                if j < len(rhs):
                    if rhs[j] == '+':
                        operator = -1
                    elif rhs[j] == '-':
                        operator = 1
            i = j + 1
        if x_count == 0:
            if num_count == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        return f"x={-num_count//x_count}"
            
                
        
# @lc code=end

