'''
Using the carry for the digit based sum.
'''
# Function returning the sum using the carry 
def ret_ele_sum(inp_arr1, inp_arr2):

    # Initializing the variables to store the sum
    ele_sum = 0
    carry = 0
    temp_str = ''

    # TO check if the length of each list is equal or not
    if len(inp_arr1) != len(inp_arr2):
        return 'Input length not equal'

    # Iterating over the list
    for i in range(len(inp1)):
        if inp1[-1-i] + inp2[-1-i] + carry >9:
            temp_str = str((inp1[-1-i] + inp2[-1-i] + carry)%10) + temp_str
            carry = 1
    
        else:
            temp_str = str((inp1[-1-i] + inp2[-1-i] + carry)%10) + temp_str
            carry = 0

    # to add the additional element for the carry at zeroth index
    if carry == 0:
        ele_sum = int(temp_str)
    else:
        ele_sum = int(str(carry)+temp_str)
    return ele_sum

# Taking the input from the user
inp1 = [1,2,3,4]
inp2 = [7,7,7,7]
print(ret_ele_sum(inp1, inp2))
