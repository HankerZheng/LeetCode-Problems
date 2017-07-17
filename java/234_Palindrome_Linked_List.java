// Given a singly linked list, determine if it is a palindrome.

// Follow up:
// Could you do it in O(n) time and O(1) space?

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
        if ((head == null) || (head.next == null)){
            return true;
        }
        ListNode fast = head, slow = head;
        while (fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        ListNode reversedNode = reverseLinkedList(slow);
        ListNode curNode = head;
        while (curNode!=null && reversedNode!=null){
            if (curNode.val != reversedNode.val){
                return false;
            }
            curNode = curNode.next;
            reversedNode = reversedNode.next;
        }
        return true;
    }
    public ListNode reverseLinkedList(ListNode root){
        ListNode prevNode = null;
        ListNode curNode = root;
        while (curNode != null){
            ListNode tmp = curNode.next;
            curNode.next = prevNode;
            prevNode = curNode;
            curNode = tmp;
            
        }
        return prevNode;
    }
}