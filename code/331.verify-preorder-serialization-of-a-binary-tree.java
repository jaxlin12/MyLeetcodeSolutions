/*
 * @lc app=leetcode id=331 lang=java
 *
 * [331] Verify Preorder Serialization of a Binary Tree
 */

// @lc code=start
import java.util.EmptyStackException;
import java.util.Stack;
class Solution {
    public boolean isValidSerialization(String preorder) {
        if(preorder.equals("#")) {
            return true;
        }
        Stack<Character> tree = new Stack<Character>();
        try {
            for(int i = 0;i < preorder.length();i+=2) {
                char c = preorder.charAt(i);
                if(tree.empty()) {
                    if(c == '#') {
                        return false;
                    }
                    tree.push(c);
                    tree.push('?');
                    tree.push('?');
                }
                else if(c == '#') {
                    tree.pop();
                }
                else {
                    tree.push(c);
                    tree.push('?');
                    tree.push('?');
                }
                while(tree.size() != 1 && tree.peek() != '?') {
                    tree.pop();
                    tree.pop();
                }
                while(i+1<preorder.length() && preorder.charAt(i+1) != ',') {
                    i++;
                }
            }
        }
        catch(EmptyStackException e) {
            return false;
        }
        if(tree.size() != 1) {
            return false;
        }
        return true;
    }
}
// @lc code=end

