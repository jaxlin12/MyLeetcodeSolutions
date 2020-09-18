#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        dummy = ListNode(None, head)
        prev = dummy
        ptr = head
        temp = head.val
        duplicate = False
        while ptr != None:
            while ptr.next != None and ptr.next.val == temp:
                ptr = ptr.next
                duplicate = True
            if duplicate:
                duplicate = False
                if ptr.next != None:
                    ptr = ptr.next
                    temp = ptr.val 
                else:
                    prev.next = None
                    ptr = ptr.next
            else:
                prev.next = ptr
                prev = ptr
                ptr = ptr.next
                if ptr != None:
                    temp = ptr.val
        

        return dummy.next


# @lc code=end

