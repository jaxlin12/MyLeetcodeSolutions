/*
 * @lc app=leetcode id=160 lang=cpp
 *
 * [160] Intersection of Two Linked Lists
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution
{
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
    {
        int diff = 0;
        ListNode *i = headA, *j = headB;
        while (i != nullptr)
        {
            i = i->next;
            diff += 1;
        }
        while (j != nullptr)
        {
            j = j->next;
            diff -= 1;
        }
        i = headA;
        j = headB;
        while (diff != 0)
        {
            if (diff < 0)
            {
                j = j->next;
                diff += 1;
            }
            else
            {
                i = i->next;
                diff -= 1;
            }
        }
        while (i != j)
        {
            i = i->next;
            j = j->next;
        }
        return i;
    }
};

