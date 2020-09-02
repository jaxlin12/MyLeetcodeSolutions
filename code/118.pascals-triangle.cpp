/*
 * @lc app=leetcode id=118 lang=cpp
 *
 * [118] Pascal's Triangle
 */
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        if(numRows == 0) return {};
        vector<vector<int>> result = {{1}};
        for(int i = 1;i < numRows;++i) {
            vector<int> row;
            row.push_back(1);
            for(int j = 0;j < result[i - 1].size() - 1;++j) {
                row.push_back(result[i - 1][j] + result[i - 1][j + 1]);
            }
            row.push_back(1);
            result.push_back(row);
        }
        
        return result;
    }
};

