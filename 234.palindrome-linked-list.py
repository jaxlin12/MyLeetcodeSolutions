#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        ptr = head
        count = 0
        while ptr != None:
            count += 1
            ptr = ptr.next
        if count == 1:
            return True
        is_odd = count % 2
        mid = count // 2
        prev = head
        ptr = head.next
        head.next = None
        for _ in range(mid - 1):
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp
        ptr2 = ptr
        ptr = prev
        if is_odd:
            ptr2 = ptr2.next
        while ptr != None and ptr2 != None:
            if ptr.val != ptr2.val:
                return False
            ptr = ptr.next
            ptr2 = ptr2.next

        return True

# @lc code=end

