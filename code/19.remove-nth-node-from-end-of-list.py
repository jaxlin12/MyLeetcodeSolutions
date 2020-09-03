#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        size = 1
        cur = p = head
        while cur.next:
            size += 1
            cur = cur.next
            if size > n + 1:
                p = p.next
        if size == n:
            return head.next
        else:
            p.next = p.next.next
            return head

#     def dfs(self, head):
#         if head == None:
#             return
#         self.dfs(head.next)
#         self.count += 1
#         if self.count == self.target + 1:
#             head.next = head.next.next
#         return

#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         dummy = ListNode(0,head)
#         self.target = n
#         self.count = 0
#         self.dfs(dummy)
#         return dummy.next
# @lc code=end

