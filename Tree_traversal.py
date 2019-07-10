'''
To display the nodes in the tree
'''

# Defining the class for the node
class Node(object):

    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

# Printing the tree nodes
def print_tree(temp):

    if not temp:
        return None

    print(temp.key)
    print_tree(temp.left)
    print_tree(temp.right)


# Defining the tree
root = Node(10)
root.left = Node(11)
root.right = Node(9)
root.left.left = Node(7)
root.right.left = Node(15)
root.right.right = Node(8)
print_tree(root)
