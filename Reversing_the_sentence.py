'''
Reversing the given sentence. For e.g. if the input
sentence is 'Hello World' then the output will be 
returned as 'World Hello'
'''

# Class for the stack, to store and pop the word
# element
class stack:

    # Initialization
    def __init__(self):
        self.stack = []

    # Insert the element to the stack
    def ins_elem(self, elem):
        return self.stack.append(elem)

    # Remoe the element from the stack
    def pop_elem(self):
        return self.stack.pop()

    # Display the stack
    def disp_stk(self):
        print("Current stack is: {}".format(self.stack))

    # return the current length of the stack
    def len_stk(self):
        return len(self.stack)

# Function returning the reversed sentence
def rev_sen(inp_str):

    temp_list = inp_str.split(' ')
    stk = stack()
    reversed_sen = ''

    # Inserting the word elements of the given sentence
    # to the stack
    for i in range(len(temp_list)):
        stk.ins_elem(temp_list[i])

    stk_len = stk.len_stk()

    # Displaying the current stack
    stk.disp_stk()

    # Reversing the elements of teh stack using the pop function
    for i in range(stk_len):
        if i < stk_len - 1:
            reversed_sen += stk.pop_elem() + ' '
        else:
            reversed_sen += stk.pop_elem()

    # Displaying the current stack
    stk.disp_stk()

    return reversed_sen

# taking the input from the user
inp_str = 'Taking the input from the user'
print("Original sentence: {}".format(inp_str))
print("Reversed sentence: {}".format(rev_sen(inp_str)))
