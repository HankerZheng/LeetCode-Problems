"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
Subscribe to see which companies asked this question
"""

# Key Points: Only keep track of the most left node of each level.
#             Then we could traverse the nodes in the same level by next
#             without FIFO.
#
# Run time: 120 ms

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return root

        this_level = root
        next_level = this_level.left if this_level.left else this_level.right

        # traverse all the level except the last one
        while next_level:
            next_level = None
            first_found = 0 # whether next_level found
            last_most_right = None
            # this_level has already been connected
            # connect next_level
            while this_level:
                # get next_level first element
                if not first_found and (this_level.left or this_level.right):
                    next_level = this_level.left if this_level.left else this_level.right
                    first_found = 1
                # first connect the inner
                if this_level.right and this_level.left:
                    this_level.left.next = this_level.right
                # then connect the most right and this_most left
                this_most_left = this_level.left if this_level.left else this_level.right
                if this_most_left and last_most_right:
                    last_most_right.next = this_most_left
                # last, update last_most_right
                if this_most_left:
                    # if this node has at least one child, this_most_left shouldnt be None
                    # then last_most_right should either be this_most_left or this_most_left.next
                    last_most_right = this_most_left.next if this_most_left.next else this_most_left
                # update this_levet:
                this_level = this_level.next
            this_level = next_level