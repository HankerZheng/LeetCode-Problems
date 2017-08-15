// A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

// Return a deep copy of the list.


// Runtime: 2 ms


/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) return null;
        RandomListNode curNode = head;
        while (curNode != null){
            RandomListNode nextNode = curNode.next;
            RandomListNode newNode = new RandomListNode(curNode.label);
            curNode.next = newNode;
            newNode.next = nextNode;
            curNode = nextNode;
        }
        curNode = head;
        while(curNode != null) {
            curNode.next.random = (curNode.random == null) ? null : curNode.random.next;
            curNode = curNode.next.next;
        }
        RandomListNode dummy = new RandomListNode(-1), tmpNode = dummy;
        curNode = head;
        while(curNode != null) {
            RandomListNode nextNode = curNode.next.next;
            tmpNode.next = curNode.next;
            curNode.next = nextNode;
            curNode = nextNode;
            tmpNode = tmpNode.next;
        }
        return dummy.next;
    }
}