# Initializing the node class
class Node:

    def __init__(self, node = None):
        self.node = node
        self.left = None
        self.right = None

# Invert the tree
def invert_tree(node):

    # Initializing temp list to store the nodes
    temp_node_list = []
    temp_node_list.append(node)

    # till the list is not empty
    while temp_node_list:
        temp = temp_node_list.pop()

        if temp:
            temp.left, temp.right = temp.right, temp.left
            temp_node_list.append(temp.left)
            temp_node_list.append(temp.right)

# Displaying the tree
def print_tree(node):

    if not node:
        return 'Tree is empty'

    print(node.node)
    print_tree(node.left)
    print_tree(node.right)

# Defining the tree
root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.right.right = Node(4)
root.right.left = Node(5)

print('Tree before inversion')
print_tree(root)

invert_tree(root)

print('Tree after inversion')
print_tree(root)
