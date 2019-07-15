'''
Circular linked list
'''

# class for creating the node
class Node:

    def __init__(self, node = None):
        self.node = node
        self.next = None

# Class for linked list
class LinkedList:

    def __init__(self):
        self.head = None

    # Insert the next element to the list
    def push_ele(self, val):
        temp = self.head
        
        if not temp:
            self.head = Node(val)
            return

        while temp:
            if temp.next == self.head:
                temp.next = None
                
            if not temp.next:
                temp.next = Node(val)
                temp = temp.next
                temp.next = self.head
                return
            else:
                temp = temp.next

    # Print the list
    def print_list(self):

        temp = self.head

        if not temp:
            print('List is empty')

        while temp:
            print(temp.node)
            temp = temp.next
            
            if temp == self.head:
                print(temp.node)
                return
            
# List initialization
list1 = LinkedList()
list1.push_ele(1)
list1.push_ele(2)
list1.push_ele(3)
list1.push_ele(4)
list1.print_list()
