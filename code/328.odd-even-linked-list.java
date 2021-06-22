/*
 * @lc app=leetcode id=328 lang=java
 *
 * [328] Odd Even Linked List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
// public class ListNode {
//     int val;
//     ListNode next;
//     ListNode() {}
//     ListNode(int val) { this.val = val; }
//     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
// }

class Solution {
    public ListNode oddEvenList(ListNode head) {
        if(head == null || head.next == null) {
            return head;
        }
        ListNode oddHead = head;
        ListNode oddPtr = oddHead;
        head = head.next;
        ListNode evenHead = head;
        ListNode evenPtr = evenHead;
        head = head.next;
        int count = 1;
        while(head != null) {
            if(count == 1) {
                oddPtr.next = head;
                oddPtr = oddPtr.next;
            }
            else {
                evenPtr.next = head;
                evenPtr = evenPtr.next;
            }
            head = head.next;
            count = (count + 1) % 2;
        }
        oddPtr.next = evenHead;
        evenPtr.next = null;
        head = oddHead;
        return head;
    }
}
// @lc code=end

