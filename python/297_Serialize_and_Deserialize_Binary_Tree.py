# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# For example, you may serialize the following tree

#     1
#    / \
#   2   3
#      / \
#     4   5
# as "[1,2,3,None,None,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        ans = []
        queue = [root]
        while queue:
            this_node = queue.pop(0)
            if this_node is None:
                ans.append(None)
            else:
                ans.append(this_node.val)
                queue.append(this_node.left)
                queue.append(this_node.right)
        # i = len(ans)-1
        # while i>=0 and ans[i] == None:
        #     ans.pop(i)
        #     i -= 1
        return ans


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data[0] is None:
            return None
        root = TreeNode(data[0])
        queue = [root]
        i = 1
        while i < len(data):
            this_parent = queue.pop(0)
            # left child
            if data[i] is None:
                this_parent.left = None
            else:
                this_parent.left = TreeNode(data[i])
                queue.append(this_parent.left)
            i += 1
            if i == len(data):
                break
            # right child
            if data[i] is None:
                this_parent.right = None
            else:
                this_parent.right = TreeNode(data[i])
                queue.append(this_parent.right)
            i += 1
        return root

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    codec = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right = TreeNode(3)
    root.right.left = TreeNode(5)

    print codec.serialize(root)
    print codec.serialize(codec.deserialize(codec.serialize(root)))

    print codec.deserialize([])