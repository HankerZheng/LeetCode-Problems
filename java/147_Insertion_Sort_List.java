// Sort a linked list using insertion sort.

// Runtime: 11ms

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode insertionSortList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        
        ListNode prev = head;
        ListNode cur = head.next;
        while(cur != null) {
            // if it's already in accending order, skip these nodes
            while (cur != null && cur.val >= prev.val){
                cur = cur.next;
                prev = prev.next;
            }
            ListNode tmp = dummy;
            while (cur != null && tmp.next.val <= cur.val) {
                tmp = tmp.next;
            }
            cur = insertAfter(tmp, cur);
            prev.next = cur;
        }
        return dummy.next;
    }
    // insert one node after the position, and return the node after the insertedNode
    private ListNode insertAfter(ListNode position, ListNode insertedNode) {
        if (insertedNode == null) return null;
        ListNode retNode = insertedNode.next;
        insertedNode.next = position.next;
        position.next = insertedNode;
        return retNode;
    }
}