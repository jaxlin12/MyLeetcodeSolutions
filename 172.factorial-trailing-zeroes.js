/*
 * @lc app=leetcode id=172 lang=javascript
 *
 * [172] Factorial Trailing Zeroes
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var trailingZeroes = function(n) {
    if (n < 5) {
        return 0;
    }
    var count = 0;
    while(n) {
        count += Math.floor(n/5);
        n = Math.floor(n/5);
    }
    return count;
};
// @lc code=end

