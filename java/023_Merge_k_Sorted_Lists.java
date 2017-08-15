// Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.


// Runtime: 14 ms

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        int end = lists.length - 1;
        while (end != 0) {
            int start = 0, curEnd = end;
            while (start < curEnd) {
                lists[start] = merge2Lists(lists[start], lists[curEnd]);
                start ++;
                curEnd --;
            }
            end = curEnd;
        }
        return lists[0];
        
    }
    
    private ListNode merge2Lists(ListNode node1, ListNode node2){
        if (node1 == null || node2 == null) return node1 == null ? node2 : node1;
        if (node1.val > node2.val) return merge2Lists(node2, node1);
        ListNode tmp1 = node1.next, tmp2 = node2;
        ListNode curNode = node1;
        while (tmp1 != null && tmp2 != null) {
            if (tmp1.val < tmp2.val) {
                curNode.next = tmp1;
                tmp1 = tmp1.next;
            } else {
                curNode.next = tmp2;
                tmp2 = tmp2.next;
            }
            curNode = curNode.next;
        }
        curNode.next = (tmp1 == null) ? tmp2 : tmp1;
        return node1;
    }
}