"""
A linked list is given such that each node contains an additional 
random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Subscribe to see which companies asked this question
"""



# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

#   Key Point: First, copy the normal linked list and store
#              every new node into a hash table(dictionary).
#              Then, update every new node's random pointer.
#              Time Complexity = O(n), Space Complexity = O(n)
#
#   Run time: 138 ms
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        hashtable = dict()
        dummy = RandomListNode(-1)
        terverse, p_res = head, dummy
        while terverse:
        # normal copy and store new node into hashtable
            p_res.next = RandomListNode(terverse.label)
            p_res = p_res.next
            hashtable[terverse] = p_res
            terverse = terverse.next

        terverse, p_res = head, dummy.next
        while terverse:
        # update random node
            p_res.random = hashtable[terverse.random] if terverse.random else None
            p_res = p_res.next
            terverse = terverse.next
        return dummy.next



class RandomListNode(object):
    def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

    @classmethod
    def create_from_array(cls, array):
        res = RandomListNode(-1)
        res_tmp = res
        for num in array:
            res_tmp.next = RandomListNode(num)
            res_tmp = res_tmp.next
        return res.next

    def display_list(self):
        tmp = self
        while tmp.next is not None:
            print tmp.label, 
            tmp = tmp.next
        print tmp.label


if __name__ == "__main__":
    head = RandomListNode.create_from_array([1,2,3,4,5,6,7,8])
    res = Solution()
    final = res.copyRandomList(head)
    final.display_list()