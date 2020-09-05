#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        slow = head
        fast = head
        dummy = ListNode()
        save = dummy
        while fast != None:
            count = 0
            while count < k and fast != None:
                if count == k - 1:
                    save.next = fast
                fast = fast.next
                count += 1
            if count != k:
                save.next = slow
                return dummy.next
            save = slow
            
            prev = slow
            slow = slow.next
            while slow != fast:
                temp = slow.next
                slow.next = prev
                prev = slow
                slow = temp
            if fast == None:
                save.next = None
        
        return dummy.next

# @lc code=end

