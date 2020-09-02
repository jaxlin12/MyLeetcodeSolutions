#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        prev = head
        ptr = head.next
        while ptr != None:
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp 
        head.next = None
        return prev
# @lc code=end

