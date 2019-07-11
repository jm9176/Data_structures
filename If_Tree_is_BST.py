'''
To check if the given tree is a BST tree or not
'''
# creating a class for the node
class Node:

    def __init__(self, node = None):
        self.node = node
        self.left = None
        self.right = None
    
# Function running a chek on the given tree
def chk_tree(temp):

    if not temp:
        return
    
    if temp.left is not None and temp.right is not None: 
        if temp.left.node > temp.node or temp.right.node < temp.node :
            return -1
    
    chk_tree(temp.left)
    chk_tree(temp.right)

# Tree input
root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3)

if chk_tree(root) == -1:
    print('Tree not BST')
else:
    print('Tree is BST')
