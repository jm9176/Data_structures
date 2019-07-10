'''
To Insert the node in the tree
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

# Inserting a node in the tree
def insert(temp, key):
    key_list = []
    key_list.append(temp)

    while len(key_list) > 0:
        temp = key_list[0]
        key_list.pop(0)

        if not temp.left:
            temp.left = Node(key)
            break
        else:
            key_list.append(temp.left)

        if not temp.right:
            temp.right = Node(key)
            break
        else:
            key_list.append(temp.right)


# Defining the tree
root = Node(10)
root.left = Node(11)
root.right = Node(9)
root.left.left = Node(7)
root.right.left = Node(15)
root.right.right = Node(8)

# Display the tree before the insertion
print_tree(root)

# Call the insert function
insert(root, 12)

# Display the tree after the insertion
print_tree(root)
