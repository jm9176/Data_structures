'''
Kadane's Algorithm

Given an array of numbers, find the minumu sum of any contiguous
subarray of the array.
For e.g. Given the list of elements [0,-80,90,-100]
The minimum sum would be -100

Given the list of elements [0,80,90,100], the function should
return 0, as the sum is always positive

Do this in O(N) time.

'''

# Function returning the maximum sub-array and the sum
def ret_min_sum(inp_arr):

    # Initializing the variables for the current sum using each elem
    # (elem_sum) and the current maximum sum till now
    elem_sum = 0
    curr_min_sum = 0

    # Iterating over the given list to find the maximum sum and the
    # list of elements giving the max sum
    for i in range(len(inp_arr)):

        # Updating the current sum and the current list of elements
        elem_sum += inp_arr[i]

        # Updating the current sum to zero is the current sum gets less
        # than zero
        if elem_sum > 0:
            elem_sum = 0

        # Updating the current maximum sum 
        if curr_min_sum > elem_sum:
            curr_min_sum = elem_sum

    return curr_min_sum

    # Taking the input from the user
#given_arr = [34,-50,42,14,-5,86]
given_arr = [0,-100,90,-100]
print(ret_min_sum(given_arr))
