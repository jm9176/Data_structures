'''
You are given an array of non-negative integers that represents
a two-dimensional elevation map where each element is unit-width
wall and the integer is the height. Suppose it will rain and all
spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time
and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water
in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first
index, 2 in the second, and 3 in the fourth index (we cannot hold 5
since it would run off to the left), so we can trap 8 units of water.
'''

# Not Staisfying conditions required for the code due to the
# max function while updating the next maximum level at the
# end of for loop. OPTIMIZATION REQUIRED**

# Optimized solution: https://www.geeksforgeeks.org/trapping-rain-water/


# Function returning the extra water units which can be stored
def lvl_wtr(inp_arr):

    # Finding the max level in the list and initializing
    # variables for the extra addition of  water tp be done
    next_max = max(inp_arr[1:len(inp_arr)])
    prev_max = inp_arr[0]
    add_wtr = 0

    # Iterating the loop to update the water requirement
    for index in range(len(inp_arr)):

        # Finding the highest previous level till now
        prev_max = max(inp_arr[index], prev_max)

        # Updating the min of the previous max level and
        # next max of the remaining elements
        curr_lvl = min(prev_max, next_max)

        # required extra water units which can be added
        add_wtr += curr_lvl - inp_arr[index]

        # updating the next maximum level to avoid overflow        
        if next_max == inp_arr[index] and index < len(inp_arr) - 1:
            next_max = max(inp_arr[index + 1:len(inp_arr)])

    return add_wtr

# Taking the input from the user
inp_arr = [3, 0,1,3,0,5]
print(lvl_wtr(inp_arr))

'''
# Function returning the water levels
def lvl_wtr(inp_arr):

    # Two independent lists storing the max water levels starting
    # from left and right
    left_lvl = []
    right_lvl = []

    # Initializing the left and right maximum levels 
    left_max = 0
    right_max = 0

    # Iterating over the given input to check the max water level
    # for left_lvl and right_lvl
    for i in range(len(inp_arr)):
        left_lvl.append(max(left_max, inp_arr[i]))

        if inp_arr[i]>left_max:
            left_max = inp_arr[i]

        right_lvl.insert(0,max(inp_arr[-i-1], right_max))

        if inp_arr[-i-1] > right_max:
            right_max = inp_arr[-i-1]

    # Additionally required water which the given input can hold
    req_water = 0

    for i in range(len(inp_arr)):
        req_water += min(left_lvl[i], right_lvl[i]) - inp_arr[i]


    return req_water

# Taking the input from the user
given_arr = [0,1,2]
print(lvl_wtr(given_arr))
'''
