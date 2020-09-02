#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        current_ptr = head
        val = head.val
        while current_ptr != None:
            next_ptr = current_ptr.next
            if next_ptr == None:
                break
            if next_ptr.val == val:
                current_ptr.next = next_ptr.next
            else:
                val = next_ptr.val
                current_ptr = current_ptr.next
        return head
# @lc code=end

