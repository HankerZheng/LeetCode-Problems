# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Sol Two:
#     Divede and Conquer as it appears in MergeSort
#     Advantage:  No new memory required. Data stored in
#                 ListNode is in disorder, it is the pointer
#                 that keep the order of data. Therefore, it
#                 is unnecessary to create new ListNode to sort,
#                 we just need to arrange the pointer.
#                 Also, in divide_conquer, no need to create new
#                 list, because we are only asked to return a ListNode.
#                 It is okay to leave the list as it was.
#     ListNode, no data operation while sorting!!!!
#     Run time: 152ms
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """ 
        def merge2Lists(list0, list1):
            res = res_tmp = ListNode(-1)  # dummy node
            tmp0, tmp1 = list0, list1
            while tmp0 and tmp1:
                if tmp0.val > tmp1.val:
                    res_tmp.next = tmp1
                    tmp1 = tmp1.next
                else:
                    res_tmp.next = tmp0
                    tmp0 = tmp0.next
                res_tmp = res_tmp.next

            if tmp0 is not None:
                res_tmp.next = tmp0
            else:
                res_tmp.next = tmp1
            return res.next

        def divide_conquer(lists, start, end):
            if start == end:
                return lists[start]
            mid = start + (end-start)/2
            list0 = divide_conquer(lists, start, mid)
            list1 = divide_conquer(lists, mid+1, end)
            return merge2Lists(list0, list1)

        if not lists:
            return None
        length = len(lists)
        if length < 2:
            return lists[0]

        start, end = 0, length-1
        return divide_conquer(lists, start, end)

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
