#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        array = []
        ptr = head
        while ptr != None:
            array.append(ptr.val)
            ptr = ptr.next
        array.sort()
        ptr = head
        i = 0
        while ptr != None:
            ptr.val = array[i]
            ptr = ptr.next
            i += 1
        return head
        
# @lc code=end

