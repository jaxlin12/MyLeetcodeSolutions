#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None or l2 == None:
            if l1 == None:
                return l2
            elif l2 == None:
                return l1
            else:
                return None

        dummy_head = ListNode()
        next_ptr = dummy_head
        l1_ptr, l2_ptr = l1, l2
        while l1_ptr != None and l2_ptr != None:
            if l1_ptr.val < l2_ptr.val:
                next_ptr.next = l1_ptr
                next_ptr = l1_ptr
                l1_ptr = l1_ptr.next
            else:
                next_ptr.next = l2_ptr
                next_ptr = l2_ptr
                l2_ptr = l2_ptr.next
        if l1_ptr != None:
            next_ptr.next = l1_ptr
        if l2_ptr != None:
            next_ptr.next = l2_ptr
        return dummy_head.next
        
# @lc code=end

