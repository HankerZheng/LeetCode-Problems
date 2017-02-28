/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null){
            return null;
        }
        int length = getListLength(head);
        int rotateNum = k % length;
        if (rotateNum == 0){
            return head;
        }
        
        ListNode fast = head;
        for(int i = 0; i < rotateNum; i++){
            fast = fast.next;
        }
        ListNode newTail = head;
        while (fast.next != null){
            fast = fast.next;
            newTail = newTail.next;
        }
        ListNode newHead = newTail.next;
        fast.next = head;
        newTail.next = null;
        return newHead;
    }
    
    public int getListLength(ListNode node){
        int length = 0;
        ListNode curNode = node;
        while (curNode != null){
            length += 1;
            curNode = curNode.next;
        }
        return length;
    }
}