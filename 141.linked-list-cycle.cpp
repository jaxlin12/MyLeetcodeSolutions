/*
 * @lc app=leetcode id=141 lang=cpp
 *
 * [141] Linked List Cycle
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *fast;
        fast = head;
        while (head)
        {

            if (fast->next && fast->next->next)
                fast = fast->next->next;
            else
                return false;
                
            if (fast == head)
                return true;
            head = head->next;//move to here
        }

        return false;
    }
};

