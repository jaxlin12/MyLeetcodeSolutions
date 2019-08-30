/*
 * @lc app=leetcode id=111 lang=cpp
 *
 * [111] Minimum Depth of Binary Tree
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


    int minDepth(TreeNode* root) {
        if(!root) return 0;
        int depth = 1;
        int leftDepth = minDepth(root->left);
        int rightDepth = minDepth(root->right);
        if(leftDepth == 0 && rightDepth == 0) {
            return depth;
        }
        else if(leftDepth == 0) {
            return depth += rightDepth;
        }
        else if(rightDepth == 0) {
           return depth += leftDepth;
        }
        else {
            depth += min(leftDepth, rightDepth);
        }
        return depth; 
    }
};

