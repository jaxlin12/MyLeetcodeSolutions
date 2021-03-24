/*
 * @lc app=leetcode id=275 lang=java
 *
 * [275] H-Index II
 */

// @lc code=start
class Solution {
    public int hIndex(int[] citations) {
        int low = 0, high = citations.length-1;
        if (high == 0 && citations[0] > 0) {
            return 1;
        }
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (citations[mid] == citations.length - mid) {
                return citations[mid];
            }
            else if (citations[mid] < citations.length - mid) {
                low = mid+1;
            }
            else {
                high = mid-1;
            }
        }
        return citations.length - (high + 1);
    }
}
// @lc code=end

