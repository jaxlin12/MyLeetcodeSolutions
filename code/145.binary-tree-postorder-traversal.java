import java.util.LinkedList;
import java.util.List;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode id=145 lang=java
 *
 * [145] Binary Tree Postorder Traversal
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> ret = new LinkedList<Integer>();
        if(root == null) {
            return ret;
        }
        LinkedList<TreeNode> BFSStack = new LinkedList<TreeNode>();
        BFSStack.push(root);
        while (!BFSStack.isEmpty()) {
            TreeNode n = BFSStack.peek();
            if (n.left != null) {
                BFSStack.push(n.left);
                n.left = null;
            }
            else if(n.right != null) {
                BFSStack.push(n.right);
                n.right = null;
            }
            else {
                ret.add(BFSStack.pop().val);
            }
        }
        return ret;

    }
}
// @lc code=end

