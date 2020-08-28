#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        ptr1 = head
        ptr2 = head.next
        while ptr1 != None and ptr2 != None:
            if ptr1 == ptr2:
                return True
            if ptr2.next == None:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        return False
# @lc code=end

