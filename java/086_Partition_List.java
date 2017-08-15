// Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

// You should preserve the original relative order of the nodes in each of the two partitions.

// For example,
// Given 1->4->3->2->5->2 and x = 3,
// return 1->2->2->4->3->5.



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
    public ListNode partition(ListNode head, int x) {
        ListNode less = new ListNode(-1);
        ListNode more = new ListNode(1);
        ListNode tmpLess = less, tmpMore = more, tmp = head;
        while (tmp != null) {
            if (tmp.val < x) {
                tmpLess.next = tmp;
                tmpLess = tmpLess.next;
            } else {
                tmpMore.next = tmp;
                tmpMore = tmpMore.next;
            }
            tmp = tmp.next;
        }
        tmpLess.next = more.next;
        tmpMore.next = null;
        return less.next == null ? more.next : less.next;
    }
}