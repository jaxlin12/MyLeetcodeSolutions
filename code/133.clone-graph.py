#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        new_head = Node(node.val)
        queue1 = collections.deque()
        queue2 = collections.deque()
        queue1.append(node)
        queue2.append(new_head)
        visted = {}
        new = {}
        visted[new_head.val] = True
        new[new_head.val] = new_head
        
        while len(queue1) != 0:
            the_node = queue1.popleft()
            new_node = queue2.popleft()
            neighbors = []
            for n in the_node.neighbors:
                if n.val not in new:
                    new[n.val] = Node(n.val)
                neighbors.append(new[n.val])
                if n.val not in visted:
                    visted[n.val] = True
                    queue1.append(n)
                    queue2.append(neighbors[-1])
            new_node.neighbors = neighbors
        return new_head
                
        
        
        
# @lc code=end

