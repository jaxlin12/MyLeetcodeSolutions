/*
 * @lc app=leetcode id=304 lang=java
 *
 * [304] Range Sum Query 2D - Immutable
 */

// @lc code=start
class NumMatrix {
    public static int[][] myPrefixSum;

    public NumMatrix(int[][] matrix) {
        myPrefixSum = new int[matrix.length][matrix[0].length];

        myPrefixSum[0][0] = matrix[0][0];
        
        for(int i = 0;i < matrix.length;i++){
            for(int j = 0;j < matrix[0].length;j++){
                if (i-1>=0 && j-1>=0) {
                    myPrefixSum[i][j] = myPrefixSum[i-1][j] + myPrefixSum[i][j-1] - myPrefixSum[i-1][j-1] + matrix[i][j];
                }
                else if(i-1>=0) {
                    myPrefixSum[i][j] = myPrefixSum[i-1][j] + matrix[i][j];
                }
                else if(j-1>=0) {
                    myPrefixSum[i][j] = myPrefixSum[i][j-1] + matrix[i][j];
                }
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        if(row1==0 && col1==0) {
            return myPrefixSum[row2][col2];
        }
        else if(row1 == 0) {
            return myPrefixSum[row2][col2] - myPrefixSum[row2][col1-1];
        }
        else if(col1 == 0) {
            return myPrefixSum[row2][col2] - myPrefixSum[row1-1][col2];
        }
        
        return myPrefixSum[row2][col2] - myPrefixSum[row2][col1-1] - myPrefixSum[row1-1][col2] + myPrefixSum[row1-1][col1-1];
        
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */
// @lc code=end

