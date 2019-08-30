/*
 * @lc app=leetcode id=108 lang=cpp
 *
 * [108] Convert Sorted Array to Binary Search Tree
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
// #include <cmath>

class Solution {
public:
    TreeNode* helper(vector<int>& nums, int low, int high) {
        int dis = high - low;
        if(dis < 0) return nullptr;       
        else if(dis == 0) return new TreeNode(nums[low]); 
        int mid;
        if(dis % 2 == 1)
            mid = low + (dis + 1) / 2;
        else
            mid = low + dis / 2;
        TreeNode* newNode = new TreeNode(nums[mid]);
        newNode->left = helper(nums, low, mid-1);
        newNode->right = helper(nums, mid+1, high); 
        return newNode;  
    }

    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return helper(nums, 0, nums.size() - 1);
    }
};

