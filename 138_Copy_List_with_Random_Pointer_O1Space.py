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
#
#   THIS solution is from discussion board without hashtable
#   Regardless of the space spent on new list, its Space complexity
#   is O(1)
#
#   Key Point: Insert the copy node into the original linked list,
#              put in right after the being copied one.
#              In the first round, make the exact copy of each node in
#              the list(including the random node) and insert it right
#              after the being copied one.
#              In the next round, copy.random = copy.random.next
#              Finally, split the list into 2 lists.
#
#   Run time: 192 ms
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head

        traverse = head
        # normal copy and insert new node right after its parent
        while traverse:
            p_res = RandomListNode(traverse.label)
            p_res.random = traverse.random
            traverse.next, p_res.next = p_res, traverse.next
            # update traverse
            traverse = traverse.next.next

        traverse = head
        # update random node
        while traverse:
            traverse.next.random = traverse.random.next if traverse.random else None
            traverse = traverse.next.next

        traverse, dummy = head, RandomListNode(-1)
        p_res = dummy
        # split linked list into 2 lists
        while traverse:
            p_res.next, traverse.next, traverse =\
                  traverse.next, traverse.next.next, traverse.next.next
            p_res = p_res.next

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