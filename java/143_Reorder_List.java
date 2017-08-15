// Given a singly linked list L: L0?L1?…?Ln-1?Ln,
// reorder it to: L0?Ln?L1?Ln-1?L2?Ln-2?…

// You must do this in-place without altering the nodes' values.

// For example,
// Given {1,2,3,4}, reorder it to {1,4,2,3}.



// Runtime: 3 ms


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;
        ListNode fast = head.next;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode lastHalf = reverseList(slow.next);
        slow.next = null;
        ListNode firstHalf = head;
        mergeTwoList(firstHalf, lastHalf);
        return;
    }
    
    private ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode cur = head;
        while (cur != null) {
            ListNode nextNode = cur.next;
            cur.next = prev;
            prev = cur;
            cur = nextNode;
        }
        return prev;
    }
    
    private ListNode mergeTwoList(ListNode first, ListNode last) {
        ListNode head = new ListNode(-1);
        ListNode tmp = head;
        while (first != null && last != null) {
            tmp.next = first;
            first = first.next;
            tmp = tmp.next;
            
            tmp.next = last;
            last = last.next;
            tmp = tmp.next;
        }
        tmp.next = first == null ? last: first;
        return head.next;
    }
}