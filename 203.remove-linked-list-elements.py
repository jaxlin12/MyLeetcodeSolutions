#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head
        prev = None
        ptr = head
        while ptr != None:
            if ptr.val == val:
                ptr = ptr.next
            else:
                break
        if ptr == None:
            return None
        new_head = ptr
        prev = ptr
        ptr = ptr.next
        while ptr != None:
            if ptr.val == val:
                prev.next = ptr.next
            else:
                prev = ptr
            ptr = ptr.next
        return new_head

# @lc code=end

