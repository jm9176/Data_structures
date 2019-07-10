# Node class
class Node(object):

    def __init__(self, data = None):
        self.data = data
        self.next = None

# Linked list class
class LinkedList(object):

    # Initialize the linked list
    def __init__(self):
        self.head = None

    # display the linked list
    def print_list(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next 

    # Adding a node at the front
    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Adding a node at the end
    def push_end(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp_node = self.head

        while temp_node:
            if not temp_node.next:
                temp_node.next = new_node
                return
            else:
                temp_node = temp_node.next

    # Insert an intermediate node
    def insert_node(self, prev_data, new_data):
        prev_node = Node(prev_data)
        new_node = Node(new_data)

        temp = self.head

        while temp:

            if temp.data == prev_node.data:
                new_node.next = temp.next
                temp.next = new_node
                
                break
            else:
                temp = temp.next
                
        
        
# Initializing the linked list
list1 = LinkedList()
list1.head = Node(1)

# Printing the current head node value of the linked list
print(list1.head.data, list1.head.next)

second = Node(2)
third = Node(3)

list1.head.next = second
print(list1.head.next.data, list1.head.next.next)

second.next = third

list1.print_list()

# Insert a node at the front
list1.push_front(0)
list1.print_list()

# Inserting node at the end
list1.push_end(4)
list1.print_list()

# Inserting the node in-between
list1.insert_node(2,7)
list1.print_list()
