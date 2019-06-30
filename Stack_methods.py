'''
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack.
If there are no elements in the stack, then it should throw an error
or return null.
max(), which returns the maximum value in the stack currently. If
there are no elements in the stack, then it should throw an error or
return null.
Each method should run in constant time.
'''

# Creating a class for the stack which creates a list(stack) to
# store the values and and additional list to store the current
# maximum element till now (max_val)
class Stack(object):

    # Initializes the element list
    def __init__(self):
        self.stack = []
        self.max_val = []

    # Displays the current stack list
    def disp_stack(self):
        return 'Current stack: {}'.format(self.stack)

    # removes last element from the stack list. If an element
    # is removed from teh stack list then an element is also
    # removed from the max_val list to update the current max_value
    def pop_stack(self):

        if not self.stack:
            return None
        else:
            self.max_val.pop()
            return 'Current popped element: {}'.format(self.stack.pop())

    # append and element to the stack list and find the
    # maximum element till now and append it to the
    # max_val list
    def push_stack(self, elem):
        self.stack.append(elem)
    
        if len(self.stack) == 1:
            self.max_val.append(self.stack[0])  
        elif elem > self.max_val[-1]:
            self.max_val.append(elem)
        else:
            self.max_val.append(self.max_val[-1])

    # returns the maximum value from the current elements
    # in the stack list
    def ret_max(self):
        if not self.max_val:
            return 'No max value, stack is empty'
        else:
            return 'Current max value: {}'.format(self.max_val[-1])

    # displays the max_val list corresponding to the stack list
    def disp_max_list(self):
        return 'Current max_list: {}'.format(self.max_val)

# Performing operations for the stack: push, pop, return current max value
stack = Stack()

# storing elements to the stack
stack.push_stack(2)
stack.push_stack(40)
stack.push_stack(10)
stack.push_stack(100)
stack.push_stack(5)

# display the stack and current max_value and max_list
print(stack.disp_stack())
print(stack.disp_max_list())
print(stack.ret_max())

# Pop a single element and display the stack
print(stack.pop_stack())
print(stack.disp_stack())

# Emptying the stack
stack.pop_stack()
stack.pop_stack()
stack.pop_stack()
stack.pop_stack()
print(stack.disp_stack())
print(stack.disp_max_list())
print(stack.ret_max())

