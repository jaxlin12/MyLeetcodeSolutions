#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node_index = {}
        new_nodes = []
        ptr = head
        dummy = Node(0)
        prev = dummy

        i = 0
        while ptr != None:
            node_index[ptr] = i
            new_nodes.append(Node(ptr.val))
            prev.next = new_nodes[i]
            ptr = ptr.next
            prev = prev.next
            i += 1
        ptr = head
        prev = dummy.next
        while ptr != None:
            if ptr.random != None:
                prev.random = new_nodes[node_index[ptr.random]]
            ptr = ptr.next
            prev = prev.next

        return dummy.next

# @lc code=end

