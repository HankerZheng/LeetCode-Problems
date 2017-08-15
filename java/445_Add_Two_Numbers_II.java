// You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Follow up:
// What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

// Example:

// Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 8 -> 0 -> 7




// Use int arr instead of stack<Integer> to improve performance

// Runtime: 53 ms

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
        int count1 = countLinkedList(l1);
        int count2 = countLinkedList(l2);
        int[] num1 = initNums(l1, count1);
        int[] num2 = initNums(l2, count2);
        
        return addArraysToListNode(num1, num2);
    }
    
    private int countLinkedList(ListNode head) {
        int count = 0;
        ListNode tmp = head;
        while (tmp != null) {
            tmp = tmp.next;
            count++;
        }
        return count;
    }
    
    private int[] initNums(ListNode head, int count) {
        int[] retNums = new int[count];
        int i = 0;
        ListNode tmp = head;
        while (tmp != null) {
            retNums[count - 1 - i] = tmp.val;
            tmp = tmp.next;
            i++;
        }
        return retNums;
    }
    
    private ListNode addArraysToListNode(int[] num1, int[] num2) {
        if (num1.length > num2.length) return addArraysToListNode(num2, num1);
        ListNode dummy = new ListNode(-1);
        ListNode curNode = null;
        int i = 0, carry = 0;
        while (i < num2.length) {
            int res = (i < num1.length ? num1[i] : 0) + num2[i] + carry;
            num2[i] = res % 10;
            carry = res / 10;
            i ++;
        }
        ListNode head = carry == 0 ? (new ListNode(-1)) : (new ListNode(carry));
        curNode = head;
        for (i = num2.length - 1; i >= 0; i--) {
            curNode.next = new ListNode(num2[i]);
            curNode = curNode.next;
        }
        return head.val == -1 ? head.next : head;
    }
}