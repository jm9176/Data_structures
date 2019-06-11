# Creating the class for the stack
# Can be used for the queue as well
# by using the pop defined at index 0
class stack:

    def __init__(self):
        self.stack = []

    def ins_elem(self, ins_elem):
        return self.stack.append(ins_elem)

    def rem_elem(self):
        return self.stack.pop()

    def disp_stack(self):
        return self.stack

    def len_stack(self):
        return len(self.stack)

# Function returning the reversed string
# using the string input from the user
def rev_string(inp_str):

    stk = stack()
    final_str = ''

    for i in range(len(inp_str)):
        stk.ins_elem(inp_str[i])

    # Displaying the stack after inserting the elems
    print("Stack after insert function: {}".format(stk.disp_stack()))

    for i in range(stk.len_stack()):
        temp_str = stk.rem_elem()
        final_str += temp_str

    print("Stack after pop function: {}".format(stk.disp_stack()))

    return final_str

# Taking the input from the user
inp_str = input("Enter the string: ")
print(rev_string(inp_str))
