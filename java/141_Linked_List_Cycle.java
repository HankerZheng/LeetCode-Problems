// Given a linked list, determine if it has a cycle in it.

// Follow up:
// Can you solve it without using extra space?



// Runtime: 1 ms


/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) return false;
        ListNode slow = head;
        ListNode fast = head.next;
        while (slow != fast) {
            if (slow == null || fast == null || fast.next == null) return false;
            slow = slow.next;
            fast = fast.next.next
        }
        return true;
    }
}