# Ref: http://www.geeksforgeeks.org/flip-binary-tree/

# Given a binary tree, the task is to flip the binary tree towards right direction that is clockwise. See below examples to see the transformation.
# In the flip operation, left most node becomes the root of flipped tree and its parent become its right child and the right sibling become its left child and same should be done for all left most nodes recursively.
from Queue import Queue

def flipTree(root):
    def constructStack(root):
        stack = []
        tmpNode = root
        while tmpNode:
            stack.append(tmpNode)
            tmpNode = tmpNode.left
        return stack

    if not root:
        return root
    leftNodeStack = constructStack(root)
    ans = leftNodeStack[-1]
    while leftNodeStack:
        thisNode = leftNodeStack.pop(-1)
        if leftNodeStack:
            thisNode.left = leftNodeStack[-1].right
            thisNode.right = leftNodeStack[-1]
        else:
            # thisNode is the root, kick all its child
            thisNode.left = None
            thisNode.right = None
    return ans


class BinaryTree(object):
    def __init__(self, content="EmptyNode"):
        self.val = content
        self.left = None
        self.right = None

    def display(self):
        def print_tree(tree, depth):
            if tree:
                if depth:
                    print "|  " * (depth-1) + '+--+' +str(tree.val)
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
        res = BinaryTree()
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
            new_node = BinaryTree(content)
            self.right = new_node
            return new_node
        elif not flag and not self.left:
            new_node = BinaryTree(content)
            self.left = new_node
            return new_node
        else:
            raise ValueError("Insertion Error!!")


if __name__ == '__main__':
    binaryTree = BinaryTree.deserializeFromList([1,2,3,4,5,6,7])
    binaryTree.display()
    flipTree(binaryTree).display()
    print ""

    binaryTree = BinaryTree.deserializeFromList([1,2,3,"#", "#",4,5])
    binaryTree.display()
    flipTree(binaryTree).display()
