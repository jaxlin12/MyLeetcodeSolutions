#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if root == None:
            ret = [None] * k
            return ret
        
        ret = []
        count = 0
        ptr = root
        while ptr != None:
            count = count + 1
            ptr = ptr.next
        if k >= count:
            ptr = root
            while ptr != None:
                ret.append(ptr)
                temp = ptr.next
                ptr.next = None
                ptr = temp
            for _ in range(count, k):
                ret.append(None)
        else:
            q = count // k
            r = count % k
            ptr = root
            
            count = 0
            while ptr != None:
                if count == 0:
                    ret.append(ptr)
                count = count + 1
                temp = ptr.next
                if count == q + (r > 0):
                    ptr.next = None
                    r = r - 1
                    count = 0
                ptr = temp
        return ret

# @lc code=end

