# Sort a linked list in O(n log n) time using constant space complexity.

# Subscribe to see which companies asked this question

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Runtime: 339/600 ms
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def createLinkedListFromList(nums):
    head = ListNode("dummy")
    this_node = head
    for i, num in enumerate(nums):
        this_node.next = ListNode(num)
        this_node = this_node.next
    return head.next
def display_linked_list(head):
    ans = []
    this_node = head
    while this_node:
        ans.append(this_node.val)
        this_node = this_node.next
    return ans

class Solution(object):
    def sortList(self, head):
        def mergeSort(head):
            # handle the case when # of elements is smaller than 3
            if head is None:
                return None
            if head.next is None:
                return head
            if head.next.next is None:
                first, second = head, head.next
                if first.val < second.val:
                    return first
                else:
                    second.next = first
                    first.next = None
                    return second
            # divide the linked list into 2 parts
            slow, fast = head, head.next.next
            while fast:
                if fast.next is None:
                    break
                fast = fast.next.next
                slow = slow.next
            first = head
            last = slow.next
            slow.next = None
            # sort the two list recursively
            first = mergeSort(first)
            last = mergeSort(last)
            # number of elements in last is 1 greater than or equal to first
            old_node = ListNode("dummy")
            first_p, last_p = first, last
            while first_p and last_p:
                if first_p.val < last_p.val:
                    old_node.next = first_p
                    first_p = first_p.next
                    old_node = old_node.next
                else:
                    old_node.next = last_p
                    last_p = last_p.next
                    old_node = old_node.next

            if last_p:
                old_node.next = last_p
            else:
                old_node.next = first_p
            return first if first.val < last.val else last
        return mergeSort(head)

    def sortList_QuickSort(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def insert_after(node1, node2):
            # insert node2 after node1
            tmp = node1.next
            node1.next = node2
            node2.next = tmp

        def get_median(node):
            first, second, third = node, node.next, node.next.next
            if first.val > second.val:
                first.val, second.val = second.val, first.val
            if first.val > third.val:
                first.val, third.val = third.val, first.val
            if second.val > third.val:
                second.val, third.val = third.val, second.val
            return first, second, third


        def quick_sort(node):
            # handle the case when # of elements is smaller than 3
            if node is None:
                return None
            if node.next is None:
                return node
            if node.next.next is None:
                first, second = node, node.next
                if first.val < second.val:
                    return first
                else:
                    second.next = first
                    first.next = None
                    return second
            # get the median of the first 3 elements
            smaller, median_node, larger  = get_median(node)
            # traverse the linked list from the 4th elements
            this_node = node.next.next.next
            # make 3 patition of the whole set
            smaller.next, median_node.next, larger.next = None, None, None
            # traverse the rest of the elements
            flag = 0
            while this_node:
                tmp = this_node.next
                if this_node.val < median_node.val:
                    insert_after(smaller, this_node)
                elif this_node.val == median_node.val:
                    if flag:
                        flag = 0
                        insert_after(smaller, this_node)
                    else:
                        flag = 1
                        insert_after(larger, this_node)
                else:
                    insert_after(larger, this_node)
                this_node = tmp
            # recursive sort the 2 parts
            start = quick_sort(smaller)
            end = quick_sort(larger)
            # concatenate the list
            this_node = start
            while this_node.next:
                this_node = this_node.next
            this_node.next = median_node
            median_node.next = end
            return start

        start = quick_sort(head)
        return start

if __name__ == '__main__':
    mylist = createLinkedListFromList([3,7,6,1,5])
    sol = Solution()
    res = sol.sortList(mylist)
    print display_linked_list(res)
