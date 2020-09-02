/*
 * @lc app=leetcode id=61 lang=cpp
 *
 * [61] Rotate List
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
    void goToNext(ListNode* theNode, int count, int &n, ListNode*& head) {
        if(theNode->next) {
            ++count;
            goToNext(theNode->next, count, n , head);
        }
        else {
            n = n % count;
            theNode->next = head;
        }
        --n;
        if(n == 0)
            head = theNode;
        else if(n == -1)
            theNode->next = nullptr;
        return;
    } 

    ListNode* rotateRight(ListNode* head, int k) {
        if(!head || !head->next)
            return head;
        if(k > 0) {
            goToNext(head, 1, k, head);
        }
        return head;
    }
};

