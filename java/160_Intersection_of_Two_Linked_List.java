// Write a program to find the node at which the intersection of two singly linked lists begins.


// For example, the following two linked lists:

// A:          a1 → a2
//                    ↘
//                      c1 → c2 → c3
//                    ↗            
// B:     b1 → b2 → b3
// begin to intersect at node c1.


// Notes:

// If the two linked lists have no intersection at all, return null.
// The linked lists must retain their original structure after the function returns.
// You may assume there are no cycles anywhere in the entire linked structure.
// Your code should preferably run in O(n) time and use only O(1) memory.
// Credits:
// Special thanks to @stellari for adding this problem and creating all test cases.



// Runtime: 2 ms

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int lengthA = checkLength(headA);
        int lengthB = checkLength(headB);
        int delta = Math.abs(lengthA - lengthB);
        ListNode shortHead = (lengthA > lengthB) ? headB: headA;
        ListNode longHead = (shortHead == headA) ? headB: headA;
        
        ListNode shortNode = shortHead;
        ListNode longNode = longHead;
        for (int i = 0; i < delta; i++) {
            longNode = longNode.next;
        }
        while (longNode != shortNode) {
            longNode = longNode.next;
            shortNode = shortNode.next;
        }
        return longNode;
        
    }
    
    private int checkLength(ListNode node){
        if (node == null) return 0;
        int count = 0;
        ListNode curNode = node;
        while (curNode != null) {
            count ++;
            curNode = curNode.next;
        }
        return count;
    }
}