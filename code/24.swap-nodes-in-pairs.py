#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        ptr1 = head
        ptr2 = head.next
        while ptr1 != None and ptr2 != None:
            prev.next = ptr2
            temp = ptr2.next
            ptr2.next = ptr1
            ptr1.next = temp
            prev = ptr1
            if temp != None:
                ptr1 = temp
                ptr2 = temp.next
            else:
                break
        return dummy.next

# @lc code=end

