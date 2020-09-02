/*
 * @lc app=leetcode id=107 lang=cpp
 *
 * [107] Binary Tree Level Order Traversal II
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void helper(TreeNode* node, int level, vector<vector<int>> &theVector) {
        if(!node) return;
        int size = theVector.size();
        ++level;
        if(level > size) {
            theVector.push_back(vector<int>());
        }
        helper(node->left, level, theVector);
        helper(node->right, level, theVector);
        theVector[level - 1].push_back(node->val);
    }

    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> theVector;
        helper(root, 0, theVector);
        reverse(theVector.begin(), theVector.end());
        return theVector;
    }
};

