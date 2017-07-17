class TreeNode(object):
    def __init__(self, val=-1):
        self.val = val
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
                print "  " * depth + 'None'
        # call the recursive function
        print_tree(self, 0)

def getTenaryExpression(s):
    root = TreeNode(s[0])
    curNode = root
    stack = []
    idx = 1
    while idx < len(s):
        newNode = TreeNode(s[idx + 1])
        if s[idx] == ":":
            parentNode = stack.pop(-1)
            parentNode.right = newNode
            curNode = newNode
        elif s[idx] == "?":
            stack.append(curNode)
            curNode.left = newNode
            curNode = newNode            
        idx += 2
    return root

if __name__ == '__main__':
    root = getTenaryExpression("a?b:c?d:e?f:g")
    root.display()
    root = getTenaryExpression("a?b?c?d:e:f:g")
    root.display()
    root = getTenaryExpression("a?c:d")
    root.display()