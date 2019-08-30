/*
 * @lc app=leetcode id=112 lang=cpp
 *
 * [112] Path Sum
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
    bool addNext(TreeNode* root, int sum, int target) {
        if(!root) return false;
        sum += root->val;
        if(sum == target && !root->left && !root->right) {
                return true;
        }
        return addNext(root->left, sum, target) || addNext(root->right, sum, target);

    }

    bool hasPathSum(TreeNode* root, int sum) {
        return addNext(root, 0, sum);
    }
};

