/*
 * @lc app=leetcode id=189 lang=javascript
 *
 * [189] Rotate Array
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    var len = nums.length;
    k = k % len;
    if(k >= 1) {
        reverse(nums, 0, len);
        reverse(nums, 0, k);
        reverse(nums, k, len);
    }
};

var reverse = function(nums, start, end) {
    var temp;
    for(var i = 0;i < (end - start) / 2;i++) {
        temp = nums[i + start];
        nums[i+start] = nums[end-i-1];
        nums[end-i-1] = temp;
    }
}
// @lc code=end

