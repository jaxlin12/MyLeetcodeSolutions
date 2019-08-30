/*
 * @lc app=leetcode id=119 lang=cpp
 *
 * [119] Pascal's Triangle II
 */
class Solution {
public:
    void combination(int n, int k, int m, long& product) {
        if(k <= n) {
            product *= k;
            product /= m;
            combination(n, k+1, m+1, product);
        }
    }

    vector<int> getRow(int rowIndex) {
        if(rowIndex == 0) return {1};
        vector<int> row;
        for(int i = 0;i < (rowIndex + 2)/ 2;++i) {
            long temp = 1;
            combination(rowIndex, rowIndex - i + 1, 1, temp);
            row.push_back(temp);
        }
        for(int j = (rowIndex + 1) / 2 - 1;j >= 0;--j) {
            row.push_back(row[j]);
        }
        return row;
    }
};

