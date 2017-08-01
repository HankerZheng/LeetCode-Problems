// Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

// You may assume the integer do not contain any leading zero, except the number 0 itself.

// The digits are stored such that the most significant digit is at the head of the list.

// Example:
// Input:
// 1->2->3

// Output:
// 1->2->4


// Time Complexity: O(n)
// Runtime: 1 ms


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode plusOne(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode slow = dummy;
        ListNode fast = dummy;
        while (fast != null) {
            slow = fast;
            while (slow.next != null && slow.next.val != 9){
                slow = slow.next;
            }
            fast = slow.next;
            while(fast != null && fast.val == 9) {
                fast = fast.next;
            }
        }
        slow.val += 1;
        while (slow.next != null) {
            slow = slow.next;
            slow.val = 0;
        }
        if (dummy.val == 0) {
            return head;
        }        
        return dummy;
    }
}