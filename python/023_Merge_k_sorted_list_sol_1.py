# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Sol One:
#     Divede and Conquer by my own idea
#     Disadvantage: del element in a list, which would
#                   cause lots of operation, and mess
#                   index of the elements in the list.
#                   No need to create new node while
#                   sorting. Assign the node list directly
#                   to .next to save memroy
#     Run time: 348 ms

class Solution(object):
    def mergeKLists(self, lists):
        length = len(lists)
        if length <= 2:
            return self.merge2Lists(lists)

        new_lists = list()
        start, end = 0, length-1

        while start < end:
            after_2sort = self.merge2Lists([lists[start], lists[end]])
            del lists[end]
            del lists[start]
            new_lists.append(after_2sort)
            end -= 2
        if start == end:
            new_lists.append(lists[start])
        return self.mergeKLists(new_lists)

    def merge2Lists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) < 1:
            return None
        if len(lists) == 1:
            return lists[0]

        res = ListNode(-1)
        res.next = ListNode(-1)
        res_tmp = res
        tmp0, tmp1 = lists[0], lists[1]
        while (tmp0 is not None) and (tmp1 is not None):
            res_tmp = res_tmp.next
            if tmp0.val > tmp1.val:
                res_tmp.val = tmp1.val
                res_tmp.next = ListNode(-1)
                tmp1 = tmp1.next
            else:
                res_tmp.val = tmp0.val
                res_tmp.next = ListNode(-1)
                tmp0 = tmp0.next

        while tmp0 is not None:
            res_tmp = res_tmp.next
            res_tmp.val = tmp0.val
            res_tmp.next = ListNode(-1)
            tmp0 = tmp0.next

        while tmp1 is not None:
            res_tmp = res_tmp.next
            res_tmp.val = tmp1.val
            res_tmp.next = ListNode(-1)
            tmp1 = tmp1.next

        res_tmp.next = None
        return res.next

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def create_from_array(cls, array):
        res = ListNode(-1)
        res_tmp = res
        for num in array:
            res_tmp.next = ListNode(num)
            res_tmp = res_tmp.next
        return res.next

    def display_list(self):
        tmp = self
        while tmp.next is not None:
            print tmp.val, 
            tmp = tmp.next
        print tmp.val


if __name__ == "__main__":
    lists = list()
    lists.append( ListNode.create_from_array([1,5,8,11,13]) )
    lists.append( ListNode.create_from_array([2,3,6]) )
    lists.append( ListNode.create_from_array([26]) )
    lists.append( ListNode.create_from_array([12,16]) )
    res = Solution()
    final = res.mergeKLists(lists)
    final.display_list()
