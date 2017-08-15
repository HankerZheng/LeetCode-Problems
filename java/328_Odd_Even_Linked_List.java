

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode oddEvenList(ListNode head) {
        ListNode oddNode = new ListNode(-1);
        ListNode evenNode = new ListNode(-2);
        ListNode oddTmp = oddNode, evenTmp = evenNode;
        ListNode cur = head;
        while (cur != null) {
            oddTmp.next = cur;
            oddTmp = oddTmp.next;
            if (cur.next == null) break;
            evenTmp.next = cur.next;
            evenTmp = evenTmp.next;
            cur = cur.next.next;
            
        }
        oddTmp.next = evenNode.next;
        evenTmp.next = null;
        return oddNode.next;
    }
}