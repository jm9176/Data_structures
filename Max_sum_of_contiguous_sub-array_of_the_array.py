'''
Kadane's Algorithm

Given an array of numbers, find the maximum sum of any contiguous
subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum
sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since
we would not take any elements.

Do this in O(N) time.

'''

# Function returning the maximum sub-array and the sum
def ret_max_sum(inp_arr):

    # Initializing the variables for the current sum using each elem
    # (elem_sum) and the current maximum sum till now
    elem_sum = 0
    curr_max_sum = 0

    # If required to return the list of elements resulting
    # int the maximum sum
    temp_list, elem_list = [], []

    # Iterating over the given list to find the maximum sum and the
    # list of elements giving the max sum
    for i in range(len(inp_arr)):

        # Updating the current sum and the current list of elements
        elem_sum += inp_arr[i]
        temp_list.append(inp_arr[i])

        # Updating the current sum to zero is the current sum gets less
        # than zero
        if elem_sum < 0:
            elem_sum = 0
            temp_list = []

        # Updating the current maximum sum 
        if curr_max_sum < elem_sum:
            curr_max_sum = elem_sum
            elem_list.extend(temp_list)

    return elem_list, curr_max_sum

    
# Taking the input from the user
#given_arr = [34,-50,42,14,-5,86]
given_arr = [-5,1,-8,-9]
print(ret_max_sum(given_arr))
