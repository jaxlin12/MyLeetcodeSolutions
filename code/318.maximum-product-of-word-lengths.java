/*
 * @lc app=leetcode id=318 lang=java
 *
 * [318] Maximum Product of Word Lengths
 */

// @lc code=start
class Solution {
    public int maxProduct(String[] words) {
        int maxLen = 0;
        int[] masks = new int[words.length];
        for(int i = 0;i < masks.length;i++) {
            for(int j = 0;j < words[i].length();j++) {
                masks[i] |= (1 << (words[i].charAt(j)-'a'));
            }
        }
        for(int i = 0;i < words.length;i++) {
            for(int j = 1;j < words.length;j++) {
                int mask1 = masks[i];
                int mask2 = masks[j];
                if((mask1 & mask2) == 0) {
                    maxLen = Math.max(maxLen, words[i].length()*words[j].length());
                }
            }
        }
        return maxLen;
    }
}
// @lc code=end

