/*
 * @lc app=leetcode id=82 lang=cpp
 *
 * [82] Remove Duplicates from Sorted List II
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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode dummy(0);
        dummy.next = head;
        ListNode* nextNode = &dummy;
        int theVal;
        while(nextNode->next && nextNode->next->next) {
            theVal = nextNode->next->val;
            ListNode* tempNode = nextNode->next->next;
            bool toDelete = false;
            while(tempNode && tempNode->val == theVal) {
                tempNode = tempNode->next;
                toDelete = true;
            }
            if(toDelete)
                nextNode->next = tempNode;
            else 
                nextNode = nextNode->next;
        }
        return dummy.next;
    }
};

