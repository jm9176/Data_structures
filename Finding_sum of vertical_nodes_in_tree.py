'''
Finding the sum of the nodes falling the same vertical line
'''

# Initializing the node class, with sum for each node
class Node(object):

    def __init__(self, node = None, node_sum = 0):
        self.node = node
        self.node_sum = node_sum
        self.left = None
        self.right = None

# Finding the nodes in the tree with the same node sum, which
# is equal to the nodes falling in the same vertical line
def calc_vert(root_val):

    closed_list = []
    
    # Function finding the sum correponding to each node, and
    # storing each node and its sum in the closed list
    def print_tree(temp, temp_sum, closed_list):

        if not temp:
            return None
        
        closed_list.append((temp.node,temp_sum))

        # to check the existence of each node and iterate it recursively
        # using the same print_tree function
        if temp.left:
            temp.left.node_sum = temp.node_sum - 1
            print_tree(temp.left, temp.left.node_sum, closed_list)
            
        if temp.right:
            temp.right.node_sum = temp.node_sum + 1
            print_tree(temp.right, temp.right.node_sum, closed_list)

    print_tree(root_val, root_val.node_sum, closed_list)

    return closed_list

# Initializing the tree with the correponding
# leaf nodes
root = Node(10)
root.left = Node(11)
root.right = Node(9)
root.left.left = Node(7)
root.right.left = Node(15)
root.right.right = Node(8)

print(calc_vert(root))
        
