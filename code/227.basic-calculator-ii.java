/*
 * @lc app=leetcode id=227 lang=java
 *
 * [227] Basic Calculator II
 */

// @lc code=start
// class Solution {
//     public int calculate(String s) {

//         if (s == null || s.isEmpty()) return 0;
//         int len = s.length();
//         Stack<Integer> stack = new Stack<Integer>();
//         int currentNumber = 0;
//         char operation = '+';
//         for (int i = 0; i < len; i++) {
//             char currentChar = s.charAt(i);
//             if (Character.isDigit(currentChar)) {
//                 currentNumber = (currentNumber * 10) + (currentChar - '0');
//             }
//             if (!Character.isDigit(currentChar) && !Character.isWhitespace(currentChar) || i == len - 1) {
//                 if (operation == '-') {
//                     stack.push(-currentNumber);
//                 }
//                 else if (operation == '+') {
//                     stack.push(currentNumber);
//                 }
//                 else if (operation == '*') {
//                     stack.push(stack.pop() * currentNumber);
//                 }
//                 else if (operation == '/') {
//                     stack.push(stack.pop() / currentNumber);
//                 }
//                 operation = currentChar;
//                 currentNumber = 0;
//             }
//         }
//         int result = 0;
//         while (!stack.isEmpty()) {
//             result += stack.pop();
//         }
//         return result;
//     }
// }

// The approach works similar to Approach 1 with the following differences :

// Instead of using a stack, we use a variable lastNumber to track the value of the last evaluated expression.
// If the operation is Addition (+) or Subtraction (-), add the lastNumber to the result instead of pushing it to the stack. The currentNumber would be updated to lastNumber for the next iteration.
// If the operation is Multiplication (*) or Division (/), we must evaluate the expression lastNumber * currentNumber and update the lastNumber with the result of the expression. This would be added to the result after the entire string is scanned.

class Solution {
    public int calculate(String s) {
        if (s == null || s.isEmpty()) return 0;
        int length = s.length();
        int currentNumber = 0, lastNumber = 0, result = 0;
        char operation = '+';
        for (int i = 0; i < length; i++) {
            char currentChar = s.charAt(i);
            if (Character.isDigit(currentChar)) {
                currentNumber = (currentNumber * 10) + (currentChar - '0');
            }
            if (!Character.isDigit(currentChar) && !Character.isWhitespace(currentChar) || i == length - 1) {
                if (operation == '+' || operation == '-') {
                    result += lastNumber;
                    lastNumber = (operation == '+') ? currentNumber : -currentNumber;
                } else if (operation == '*') {
                    lastNumber = lastNumber * currentNumber;
                } else if (operation == '/') {
                    lastNumber = lastNumber / currentNumber;
                }
                operation = currentChar;
                currentNumber = 0;
            }
        }
        result += lastNumber;
        return result;
    }
}


// @lc code=end

