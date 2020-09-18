#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None:
            return head
        less = ListNode()
        greater = ListNode()
        less_ptr = less
        greater_ptr = greater
        ptr = head
        while ptr != None:
            if ptr.val < x:
                less_ptr.next = ptr
                less_ptr = less_ptr.next
            else:
                greater_ptr.next = ptr
                greater_ptr = greater_ptr.next
            ptr = ptr.next

        less_ptr.next = greater.next
        greater_ptr.next = None
        return less.next

        
# @lc code=end

