# Given a singly linked list where elements are sorted
# in ascending order, convert it to a height balanced BST.

# Subscribe to see which companies asked this question

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Runtime: 417ms
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def getheight(node):
            if node is None:
                return -1
            return node.height
        def construct(root, node):
            if root is None:
                return node
            if getheight(root.left)>=getheight(root.right):
                root.right = construct(root.right, node)
                root.height = max(getheight(root.left), getheight(root.right))+1
                return root
            else:
                k1, k2 = root, root.right
                k1.right, k2.left = k2.left, k1
                k1.height = max(getheight(k1.left), getheight(k1.right))+1
                k2.right = construct(k2.right, node)
                k2.height = max(getheight(k2.left), getheight(k2.right))+1
                return k2

        if head is None:
            return None
        root = TreeNode(head.val)
        link = head.next
        while link:
            thisnode = TreeNode(link.val)
            thisnode.height = 0
            root = construct(root, thisnode)
            link = link.next
        # root = TreeNode(head[0])
        # for num in head[1:]:
        #     thisnode = TreeNode(num)
        #     thisnode.height = 0
        #     root = construct(root, thisnode)

        return root

class TreeNode(object):
    def __init__(self, content="EmptyNode"):
        self.val = content
        self.left = None
        self.right = None

    def display(self):
        def print_tree(tree, depth):
            if tree:
                if depth:
                    print "|  " * (depth-1) + '+--+' +str(tree.val)+'(%s)'%tree.height
                else:
                    print '+' +str(tree.val)

                if tree.left or tree.right:
                    print_tree(tree.left, depth+1)
                    print_tree(tree.right, depth+1)
            else:
                print "|  " * (depth-1) + '+--+' + 'None'
        # call the recursive function
        print_tree(self, 0)

    @classmethod
    def deserializeFromList(cls, in_list):
        res = TreeNode()
        queue = Queue()
        queue.put((res, False))
        for item in in_list:
            if not queue.empty():
                this_node = queue.get(block=False)
            else:
                raise ValueError("Deserialization list error!")
            if item != '#':
                new_node = this_node[0].raw_insert(item, this_node[1])
                queue.put((new_node,False))
                queue.put((new_node,True))

        return res

    def serialize(self):
        queue = Queue()
        res = list()
        queue.put(self)
        while not queue.empty():
            this_node = queue.get(block=False)
            if this_node:
                res.append(this_node.val)
                queue.put(this_node.left)
                queue.put(this_node.right)
            else:
                res.append('#')
        last = -1
        while res[last] == '#':
            last -= 1
        if last == -1:
            return res
        return res[:last+1]



    def raw_insert(self, content, flag):
        """
        Insert new node with content right below self node
        If both 2 nodes are used, raise an error
        Params: content - the value of new node
                flag - False is for left node, True is for right node
        Return the new inserted node
        """
        if self.val == "EmptyNode":
            self.val = content
            return self
        if flag and not self.right:
            new_node = TreeNode(content)
            self.right = new_node
            return new_node
        elif not flag and not self.left:
            new_node = TreeNode(content)
            self.left = new_node
            return new_node
        else:
            raise ValueError("Insertion Error!!")

if __name__ == '__main__':
    sol = Solution()
    ans = sol.sortedListToBST(range(19))
    ans.display()
    print ans.height, ans.left.height, ans.right.height