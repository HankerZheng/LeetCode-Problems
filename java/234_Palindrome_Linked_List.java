// Given a singly linked list, determine if it is a palindrome.

// Follow up:
// Could you do it in O(n) time and O(1) space?


// Runtime: 2 ms

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;
        ListNode fast = head.next;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode lastHalf = reverseLinkedList(slow.next);
        ListNode firstHalf = head;
        while(lastHalf != null) {
            if (lastHalf.val != firstHalf.val) return false;
            lastHalf = lastHalf.next;
            firstHalf = firstHalf.next;
        }
        return true;
    }
    
    private ListNode reverseLinkedList(ListNode head) {
        ListNode prevNode = null;
        ListNode curNode = head;
        while (curNode != null) {
            ListNode nextNode = curNode.next;
            curNode.next = prevNode;
            prevNode = curNode;
            curNode = nextNode;
        }
        return prevNode;
    
    }
}