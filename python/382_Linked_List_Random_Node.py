# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

# Follow up:
# What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

# Example:

# // Init a singly linked list [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);

# // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
# solution.getRandom();
# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self._data = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        this_node = self._data
        count = 1
        ans = 0
        while this_node:
            if random.randrange(0,count) == 0:
                ans = this_node.val
            this_node = this_node.next
            count += 1
        return ans        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

sol = Solution(head)
hashtable = {}
for i in xrange(1000):
    this = sol.getRandom()
    hashtable[this] = hashtable.get(this,0)+1
print hashtable