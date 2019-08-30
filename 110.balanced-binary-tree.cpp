/*
 * @lc app=leetcode id=110 lang=cpp
 *
 * [110] Balanced Binary Tree
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
    bool helper(TreeNode* root, int &depth) {
        if(!root) return true;

        int leftDepth = 0;
        int rightDepth = 0;
        if(helper(root->left, leftDepth) && helper(root->right, rightDepth)) {
            ++depth;
            depth += max(leftDepth, rightDepth);
            return abs(leftDepth - rightDepth) < 2;
        }

        return false;
    }

    bool isBalanced(TreeNode* root) {
        if(!root) return true;
        int leftDepth = 0;
        int rightDepth = 0;
        if(helper(root->left, leftDepth) && helper(root->right, rightDepth)) {
            return abs(leftDepth - rightDepth) < 2;
        }
        return false;
    }
};

