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
            if not temp.next:
                temp.next = Node(val)
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

    # reverse the list
    def rev_list(self):

        curr_node = self.head
        prev_node = None

        if not curr_node:
            return

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node

# List initialization
list1 = LinkedList()
list1.push_ele(1)
list1.push_ele(2)
list1.print_list()
list1.rev_list()
list1.print_list()
