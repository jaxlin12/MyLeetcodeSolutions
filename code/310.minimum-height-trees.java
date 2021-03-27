/*
 * @lc app=leetcode id=310 lang=java
 *
 * [310] Minimum Height Trees
 */


/*
    Implementation

    Given the above algorithm, we could implement it via the Breadth First Search (BFS) strategy, to trim the leaf nodes layer by layer (i.e. level by level).

    Initially, we would build a graph with the adjacency list from the input.

    We then create a queue which would be used to hold the leaf nodes.

    At the beginning, we put all the current leaf nodes into the queue.

    We then run a loop until there is only two nodes left in the graph.

    At each iteration, we remove the current leaf nodes from the queue. While removing the nodes, we also remove the edges that are linked to the nodes. As a consequence, some of the non-leaf nodes would become leaf nodes. And these are the nodes that would be trimmed out in the next iteration.

    The iteration terminates when there are no more than two nodes left in the graph, which are the desired centroids nodes.

*/
// @lc code=start
class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {

        // base cases
        if (n < 2) {
            ArrayList<Integer> centroids = new ArrayList<>();
            for (int i = 0; i < n; i++)
                centroids.add(i);
            return centroids;
        }

        // Build the graph with the adjacency list
        ArrayList<Set<Integer>> neighbors = new ArrayList<>();
        for (int i = 0; i < n; i++)
            neighbors.add(new HashSet<Integer>());

        for (int[] edge : edges) {
            Integer start = edge[0], end = edge[1];
            neighbors.get(start).add(end);
            neighbors.get(end).add(start);
        }

        // Initialize the first layer of leaves
        ArrayList<Integer> leaves = new ArrayList<>();
        for (int i = 0; i < n; i++)
            if (neighbors.get(i).size() == 1)
                leaves.add(i);

        // Trim the leaves until reaching the centroids
        int remainingNodes = n;
        while (remainingNodes > 2) {
            remainingNodes -= leaves.size();
            ArrayList<Integer> newLeaves = new ArrayList<>();

            // remove the current leaves along with the edges
            for (Integer leaf : leaves) {
                // the only neighbor left for the leaf node
                Integer neighbor = neighbors.get(leaf).iterator().next();
                // remove the edge along with the leaf node
                neighbors.get(neighbor).remove(leaf);
                if (neighbors.get(neighbor).size() == 1)
                    newLeaves.add(neighbor);
            }

            // prepare for the next round
            leaves = newLeaves;
        }

        // The remaining nodes are the centroids of the graph
        return leaves;
    }
}



// import java.util.*;
// class TreeNode {
//     public Integer height = 0;
//     public Boolean visited = false;
//     public HashSet<Integer> edges = new HashSet<Integer>();
// }

// class Solution {
//     public List<Integer> findMinHeightTrees(int n, int[][] edges) {
//         HashMap<Integer, TreeNode> ptr = new HashMap<Integer, TreeNode>();
//         for (int i = 0;i < n;i++) {
//             TreeNode newNode = new TreeNode();
//             ptr.put(i, newNode);
//         }
//         for (int i = 0;i < edges.length;i++) {
//             ptr.get(edges[i][0]).edges.add(edges[i][1]);
//             ptr.get(edges[i][1]).edges.add(edges[i][0]);
//         }

//         int[] h = new int[n];
//         int minHeight = Integer.MAX_VALUE;

//         LinkedList<TreeNode> BFSQueue = new LinkedList<TreeNode>();
//         for (int i = 0;i < n;i++) {
//             BFSQueue.clear();
//             for(int j = 0;j < n;j++) {
//                 ptr.get(j).height = 0;
//                 ptr.get(j).visited = false;
//             }
//             ptr.get(i).visited = true;
//             ptr.get(i).height = 0;
//             BFSQueue.add(ptr.get(i));
//             while(!BFSQueue.isEmpty()) {
//                 TreeNode currentNode = BFSQueue.pop();
//                 for (Integer c : currentNode.edges) {
//                     if(!ptr.get(c).visited) {
//                         ptr.get(c).visited = true;
//                         ptr.get(c).height = currentNode.height + 1;
//                         BFSQueue.add(ptr.get(c));
//                     }
//                 }
//                 h[i] = currentNode.height;
//                 if(h[i] > minHeight && !BFSQueue.isEmpty()) {
//                     break;
//                 }
//             }
//             minHeight = Math.min(h[i], minHeight);
//         }

//         List<Integer> ret = new ArrayList<Integer>();
//         for (int i = 0;i<n;i++) {
//             if(h[i] == minHeight) {
//                 ret.add(i);
//             }
//         }
//         return ret;
//     }
// }
// @lc code=end

