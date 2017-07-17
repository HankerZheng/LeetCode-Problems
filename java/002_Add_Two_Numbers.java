// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyNode = new ListNode(-1);
        int carry = 0;
        ListNode tmp1 = l1, tmp2 = l2, tmpAns = dummyNode;
        while (tmp1!= null || tmp2 != null || carry!=0){
            int thisDigit = carry;
            if (tmp1 != null){
                thisDigit += tmp1.val;
                tmp1 = tmp1.next;
            }
            if (tmp2 != null){
                thisDigit += tmp2.val;
                tmp2 = tmp2.next;
            }
            carry = thisDigit / 10;
            thisDigit = thisDigit % 10;
            tmpAns.next = new ListNode(thisDigit);
            tmpAns = tmpAns.next;
        }
        return dummyNode.next;
        
    }
}