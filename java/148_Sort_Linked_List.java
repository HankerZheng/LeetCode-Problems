// Sort a linked list in O(n log n) time using constant space complexity.


// Runtime: 19ms


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    
    ListNode dummyNode = new ListNode(-1);
    
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null)  return head;
        // split current list into 2 part
        ListNode[] headList = new ListNode[2];
        headList[0] = head;
        headList[1] = head.next;
        ListNode tmp = head.next.next;
        head.next.next = null;
        head.next = null;
        int count = 0;
        while (tmp != null) {
            ListNode thisNode = tmp;
            tmp = tmp.next;
            thisNode.next = headList[count & 1];
            headList[count & 1] = thisNode;
            count ++;
        }
        // sort two list
        headList[0] = sortList(headList[0]);
        headList[1] = sortList(headList[1]);
        // connect the main problem and subproblem
        tmp = dummyNode;
        while (headList[0] != null && headList[1] != null){
            if (headList[0].val > headList[1].val){
                tmp.next = headList[1];
                headList[1] = headList[1].next;
            } else {
                tmp.next = headList[0];
                headList[0] = headList[0].next;
            }
            tmp = tmp.next;
        }
        tmp.next = headList[0] != null ? headList[0] : headList[1];
        return dummyNode.next;
    }
}