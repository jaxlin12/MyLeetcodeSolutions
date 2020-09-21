#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ptr = head
        count = 0
        while ptr != None:
            ptr = ptr.next
            count += 1
        if count <= 2:
            return head

        mid = count // 2
        i = 0
        ptr = head
        while i < mid:
            ptr = ptr.next
            i += 1
        ptr1 = head
        ptr2 = ptr.next
        save = ptr.next

        next_ptr = ptr2.next        
        while next_ptr != None:
            temp = next_ptr.next
            next_ptr.next = ptr2
            ptr2 = next_ptr
            next_ptr = temp
        save.next = None

        while ptr2 != None:
            temp1 = ptr1.next
            temp2 = ptr2.next
            ptr1.next = ptr2
            ptr2.next = temp1
            ptr1 = temp1
            ptr2 = temp2
        while ptr1.next != save:
            ptr1 = ptr1.next
        ptr1.next = None
        return head

        
# @lc code=end

