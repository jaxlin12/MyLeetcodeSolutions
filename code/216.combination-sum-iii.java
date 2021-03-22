import java.util.ArrayList;

/*
 * @lc app=leetcode id=216 lang=java
 *
 * [216] Combination Sum III
 */

// @lc code=start
class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> ret = helper(k, n, 0);
        if (ret == null) {
            return new ArrayList<List<Integer>>();
        }
        return helper(k, n, 0);
    }

    public List<List<Integer>> helper(int k, int n, int min) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        List<Integer> newArray = new ArrayList<Integer>();
        if (k < 1 || n <= 0) {
            return null;
        }
        else if (k == 1 && 0 < n && n <= 9 && n > min) {
            newArray.add(0, n);
            ret.add(newArray);
            return ret;
        }

        for (int i = min+1;i < 10;i++) {
            List<List<Integer>> nextLevel = helper(k-1, n-i, i);
            if (nextLevel != null) {
                for (List<Integer> a : nextLevel) {
                    a.add(0, i);
                    ret.add(a);
                }
            }
        }
        if (ret.size() == 0) {
            return null;
        }
        return ret;
    }
}
// @lc code=end

