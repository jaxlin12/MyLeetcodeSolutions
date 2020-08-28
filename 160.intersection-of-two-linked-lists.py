#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        ptr1 = headA
        ptr2 = headB
        count1 = 0
        count2 = 0
        while ptr1 != None and ptr2 != None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            count1 = count1 + 1
            count2 = count2 + 1
        while ptr1 != None:
            ptr1 = ptr1.next
            count1 = count1 + 1
        while ptr2 != None:
            ptr2 = ptr2.next
            count2 = count2 + 1
        difference = count1 - count2
        ptr1 = headA
        ptr2 = headB
        if difference > 0:
            while difference > 0:
                ptr1 = ptr1.next
                difference = difference - 1
        else:
            while difference < 0:
                ptr2 = ptr2.next
                difference = difference + 1
        while ptr1 != None and ptr2 != None:
            if ptr1 == ptr2:
                return ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return None
        
# @lc code=end

