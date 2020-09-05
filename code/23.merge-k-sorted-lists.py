#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        return self.divideMerge(lists, 0, len(lists)-1)
        
    def divideMerge(self, lists, left, right):
        if left == right:
            return lists[left]
        elif left == right-1:
            return self.merge2Lists(lists[left], lists[right])
        
        mid = left + (right - left) // 2
        list1 = self.divideMerge(lists, left, mid)
        list2 = self.divideMerge(lists, mid+1, right)
        return self.merge2Lists(list1, list2)


    def merge2Lists(self, list1, list2):
        ptr1 = list1
        ptr2 = list2
        dummy = ListNode()
        new_ptr = dummy
        while ptr1 != None and ptr2 != None:
            if ptr1.val <= ptr2.val:
                new_ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                new_ptr.next = ptr2
                ptr2 = ptr2.next
            new_ptr = new_ptr.next
        while ptr1 != None:
            new_ptr.next = ptr1
            new_ptr = ptr1
            ptr1 = ptr1.next
        while ptr2 != None:
            new_ptr.next = ptr2
            new_ptr = ptr2
            ptr2 = ptr2.next
        return dummy.next
                            


# @lc code=end

