#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        ptr1 = l1
        ptr2 = l2
        dummy = ListNode()
        new_ptr = dummy
        carry = 0
        while ptr1 != None and ptr2 != None:
            sum = ptr1.val + ptr2.val + carry
            carry = sum // 10
            new_ptr.next = ListNode(sum % 10)
            new_ptr = new_ptr.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        while ptr1 != None:
            sum = ptr1.val + carry
            carry = sum // 10
            new_ptr.next = ListNode(sum % 10)
            new_ptr = new_ptr.next
            ptr1 = ptr1.next
        while ptr2 != None:
            sum = ptr2.val + carry
            carry = sum // 10
            new_ptr.next = ListNode(sum % 10)
            new_ptr = new_ptr.next
            ptr2 = ptr2.next
        if carry != 0:
            new_ptr.next = ListNode(1)
        return dummy.next


# @lc code=end

