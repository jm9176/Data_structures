'''
Given a list of integers S and a target number k, write a
function that returns a subset of S that adds up to k. If
such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume
all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return
[12, 9, 2, 1] since it sums up to 24.
'''

# Function returning the subset of the given input as per the
# required sum
def arr_subset(inp_arr, inp_sum):

    # To check if the input is not empty
    if not inp_arr:
        return 'Error: the input array is empty'

    else:
        arr_sub = []
        power_list = [[]]

        # Calculating the power set using the given list
        for var in inp_arr:
            power_list.extend([var1 + [var] for var1 in power_list])

        # Finding the lists from the calculated power set whose sum of
        # elements adds up to the desired sum
        for var in power_list:
            temp_sum = 0
            for var1 in var:
                temp_sum += var1 

            if temp_sum == inp_sum:
                if var not in arr_sub:
                    arr_sub.append(var)

        return 'The required subset that adds up to {}, is: {}'.format(inp_sum, arr_sub)

# Taking the input from the user
given_arr = [12,1,61,5,9,2,7]
#given_arr = []
given_sum = 24
print(arr_subset(given_arr, given_sum))



