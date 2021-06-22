/*
 * @lc app=leetcode id=316 lang=java
 *
 * [316] Remove Duplicate Letters
 */

import java.util.Stack;
// @lc code=start
class Solution {
    public String removeDuplicateLetters(String s) {
        int[] count = new int[26];
        boolean[] isDuplicate = new boolean[26];

        for (int i = 0;i < s.length();i++) {
            count[s.charAt(i)-'a']++;
        }

        Stack<Character> stack = new Stack<Character>();
        char first = s.charAt(0);
        count[first-'a']--;
        isDuplicate[first-'a'] = true;
        stack.push(first);

        for (int i = 1;i < s.length();i++) {
            char c = s.charAt(i);
            int index = c - 'a';
            if(!isDuplicate[index]) {
                char top = stack.peek();
                while(c < top && count[top-'a']>0 
                        && !stack.empty()) {
                    char remove = stack.pop();
                    isDuplicate[remove-'a'] = false;
                    if(!stack.empty()) {
                        top = stack.peek();
                    }
                }
                isDuplicate[index] = true;
                stack.push(c);
            }
            count[index]--;
        }

        StringBuilder sb = new StringBuilder();
        //pop character from stack and build answer string from back
        while(!stack.isEmpty()){
            sb.insert(0,stack.pop());
        }
        return sb.toString();
    }
}
// @lc code=end

