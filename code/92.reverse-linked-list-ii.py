#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None or head.next == None:
            return head
        dummy = ListNode(None, head)
        save1 = None
        save2 = None
        ptr = dummy 
        count = 0
        while ptr != None:
            count += 1
            if count == m:
                save1 = ptr
                save2 = ptr.next
                ptr = ptr.next
                break
            ptr = ptr.next
        next_ptr = ptr.next
        if next_ptr == None:
            save1.next = ptr
            save2.next = None

        while next_ptr != None:
            if count == n:
                save1.next = ptr
                save2.next = next_ptr
                break
            else:
                temp = next_ptr.next
                next_ptr.next = ptr
                ptr = next_ptr
                next_ptr = temp
            count += 1
        if next_ptr == None and count == n:
            save1.next = ptr
            save2.next = next_ptr

        return dummy.next
        


# @lc code=end

