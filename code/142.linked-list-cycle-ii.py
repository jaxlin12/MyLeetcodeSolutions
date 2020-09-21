#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        ptr1 = ptr2 = dummy
        count1 = count2 = 0
        length = None
        while True:
            if ptr2 == None or ptr2.next == None or ptr2.next.next == None:
                return None
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            count1 += 1
            count2 += 2
            if ptr1 == ptr2:
                length = count2 - count1
                break
        ptr1 = ptr2 = dummy
        count = 0
        while count < length-1:
            ptr2 = ptr2.next
            count += 1
        while ptr2.next != ptr1:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
        


# @lc code=end

