'''
Performing binary search operation on a given input
list with elements in increasing order.
The input takes a list and some random values to be
searched in the list. The function binary search returns
the index of the element, if found in the list else it
returns, value not found
'''
# Function returning the index value of the element to be found
def binary_search(inp_arr, value):

    # Calculating the length of teh input list and
    # defining a index variable of the value to be searched as 0
    len_arr = len(inp_arr)
    val_index = 0

    # Iterating over the list till the length of the list is
    # not equal to 1
    while len_arr > 0:

        # if the list with length 1, has the element to be found
        # at index zero then return the index value
        if len_arr == 1 and inp_arr[0] == value:
            return '{} found at index: {}'.format(value, val_index)
        elif len_arr == 1 and inp_arr[0] != value:
            return '{} not found in the list'.format(value)

        # If the value is greater than the middle element, then
        # select the 2nd half of the list else the 1st half
        if value > inp_arr[int(len_arr/2)-1]:
            inp_arr = inp_arr[int(len_arr/2):]
            val_index += int(len_arr/2)
        else:
            inp_arr = inp_arr[:int(len_arr/2)]

        # Updating the list len variable for the while loop condition
        len_arr = len(inp_arr)
        

# Taking the nput from the user
input_list = [1,3,9,11,15,19,29]

# Value to be found
test_val1 = 25
test_val2 = 1

print(binary_search(input_list, test_val1))
print(binary_search(input_list, test_val2))
