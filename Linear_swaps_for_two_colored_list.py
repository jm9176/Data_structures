'''
Linear swaps for a list containing to different colors
Do this in linear time and in-place.
For example, given the array ['B', 'R', 'R',
'B', 'R'], it should become ['R', 'R', 'R', 'B','B'].

Refernce: Dutch Flag example
https://en.wikipedia.org/wiki/Dutch_national_flag_problem
'''

# Function returning the modified list as required
# using the element swap
def mod_arr(inp_arr):

    # return the same list in case the length of the list is 1
    if len(inp_arr) == 1:
        return inp_arr

    else:
        ind_low = 0
        ind_high = len(inp_arr) - 1

        # Iterating over the over till the following
        # condition is not met
        while ind_low <= ind_high:

            # If the mid index has character 'R' then swap the
            # low and mid value index's elements and increment
            # the position of low and mid index
            if inp_arr[ind_low] == 'R':
                ind_low += 1
            
            else:
                inp_arr[ind_low], inp_arr[ind_high] = inp_arr[ind_high], inp_arr[ind_low]
                ind_high -= 1

    return inp_arr

# taking the input from the user
inp_arr = ['B', 'R', 'R','B', 'R']
print("The sorted list is: ", mod_arr(inp_arr))
