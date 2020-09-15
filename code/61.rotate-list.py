#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None or k == 0:
            return head

        ptr1 = ListNode(None, head)
        ptr2 = ListNode(None, head)

        count = 0
        while ptr2.next != None and count < k:
            ptr2 = ptr2.next
            count += 1
        if count != k:
            k = count - k % count
            if k == count:
                return head
            count2 = 0
            while count2 < k:
                ptr1 = ptr1.next
                count2 += 1
        elif ptr2.next != None:
            while ptr2.next != None:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
        else:
            return head

        temp = head
        head = ptr1.next
        ptr1.next = None
        ptr2.next = temp
        return head
            

# @lc code=end

