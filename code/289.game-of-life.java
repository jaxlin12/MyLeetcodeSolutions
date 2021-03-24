/*
 * @lc app=leetcode id=289 lang=java
 *
 * [289] Game of Life
 */

// @lc code=start
class Solution {
    public void gameOfLife(int[][] board) {
        int n = board.length;
        int m = board[0].length;
        // 0: dead
        // 1: live
        // 2: dead to live
        // 3: live to dead
        for (int i = 0;i < n;i++) {
            for (int j = 0;j < m;j++) {
                int countLive = 0;
                if (j-1 >= 0) {
                    if (board[i][j-1] == 1 || board[i][j-1] == 3)
                        countLive++;
                }
                if (j+1 < m) {
                    if (board[i][j+1] == 1 || board[i][j+1] == 3)
                        countLive++;
                }
                if(i-1 >= 0) {
                    if (board[i-1][j] == 1 || board[i-1][j] == 3)
                        countLive++;
                    if (j-1 >= 0) {
                        if (board[i-1][j-1] == 1 || board[i-1][j-1] == 3)
                            countLive++;
                    }
                    if (j+1 < m) {
                        if (board[i-1][j+1] == 1 || board[i-1][j+1] == 3)
                            countLive++;
                    }
                }
                if(i+1 < n) {
                    if (board[i+1][j] == 1 || board[i+1][j] == 3)
                            countLive++;
                    if (j-1 >= 0) {
                        if (board[i+1][j-1] == 1 || board[i+1][j-1] == 3)
                            countLive++;
                    }
                    if (j+1 < m) {
                        if (board[i+1][j+1] == 1 || board[i+1][j+1] == 3)
                            countLive++;
                    }
                }
                if (board[i][j] == 0) {
                    if (countLive == 3) {
                        board[i][j] = 2;
                    }
                }
                else {
                    if (countLive < 2 || countLive > 3) {
                        board[i][j] = 3;
                    }
                }
            }
        }

        for (int i = 0;i < n;i++) {
            for (int j = 0;j < m;j++) {
                if(board[i][j] == 2) {
                    board[i][j] = 1;
                }
                else if (board[i][j] == 3) { 
                    board[i][j] = 0;
                }
            }
        }
    }
}
// @lc code=end

