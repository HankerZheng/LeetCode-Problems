# You must do this in-place without altering the nodes' values.

# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.

# Subscribe to see which companies asked this question

# Definition for singly-linked list.

# Runtime 179ms
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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # first divide the linked list into 2 parts
        if head is None or head.next is None:
            return
        fast, slow = head, head
        while fast and slow:
            if fast.next is None or fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next
        part2 = slow.next
        slow.next = None
        part1 = head
        # Now, part1 is the first half and part2 is the last half
        # Reverse the last half
        this_node = part2
        last_node = None
        while this_node:
            this_node, last_node, this_node.next = this_node.next, this_node, last_node
            # print display_linked_list(this_node)
            # print display_linked_list(last_node)
        part2 = last_node
        # combine this 2 parts together
        p1, p2 = part1, part2
        while p1 and p2:
            p1.next, p2.next, p1, p2 =  p2, p1.next, p1.next, p2.next

if __name__ == '__main__':
    head = createLinkedListFromList([1,2,3,4,5,6,7])
    # print display_linked_list(head)
    sol = Solution()
    sol.reorderList(head)
    print display_linked_list(head)