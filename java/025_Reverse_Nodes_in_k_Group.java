// Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

// k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

// You may not alter the values in the nodes, only nodes itself may be changed.

// Only constant memory is allowed.

// For example,
// Given this linked list: 1->2->3->4->5

// For k = 2, you should return: 2->1->4->3->5

// For k = 3, you should return: 3->2->1->4->5



// Runtime: 8 ms

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (k == 1) return head;
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode cur = dummy;
        while(cur != null) {
            ListNode nextNode = cur.next;
            ListNode retNode = reversePart(nextNode, k);
            if (retNode == nextNode) break;
            cur.next = retNode;
            cur = nextNode;
        }
        return dummy.next;
    }
    
    public ListNode reversePart(ListNode head, int len) {
        // First, check the length of the given node;
        ListNode tmp = head;
        int count = 0;
        while (tmp != null) {
            tmp = tmp.next;
            count ++;
        }
        if (count < len) return head;

        // Then, reverse the linked list
        ListNode prev = null;
        ListNode cur = head;
        for (int i = 0; i < len; i++){
            ListNode nextNode = cur.next;
            cur.next = prev;
            prev = cur;
            cur = nextNode;
        }
        head.next = cur;
        return prev;
    }
}