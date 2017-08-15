// Reverse a linked list from position m to n. Do it in-place and in one-pass.

// For example:
// Given 1->2->3->4->5->NULL, m = 2 and n = 4,

// return 1->4->3->2->5->NULL.

// Note:
// Given m, n satisfy the following condition:
// 1 ? m ? n ? length of list.



// Runtime: 4 ms

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode tmp = dummy;
        for (int i = 0; i < m - 1; i ++) {
            tmp = tmp.next;
        }
        tmp.next = reversePart(tmp.next, n - m + 1);
        return dummy.next;
    }
    
    private ListNode reversePart(ListNode head, int length) {
        ListNode prev = null;
        ListNode cur = head;
        for (int i = 0; i < length; i ++) {
            ListNode nextNode = cur.next;
            cur.next = prev;
            prev = cur;
            cur = nextNode;
        }
        head.next = cur;
        return prev;
    }
}