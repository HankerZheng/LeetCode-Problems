// Given a linked list, swap every two adjacent nodes and return its head.

// For example,
// Given 1->2->3->4, you should return the list as 2->1->4->3.

// Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.


// Runtime: 5 ms


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode curNode = head;
        ListNode prevNode = dummy;
        while(curNode != null && curNode.next != null) {
            ListNode nextCurNode = curNode.next.next;
            curNode.next.next = curNode;
            prevNode.next = curNode.next;
            curNode.next = nextCurNode;
            prevNode = curNode;
            curNode = nextCurNode;
        }
        return dummy.next;
    }
}