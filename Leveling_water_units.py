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

