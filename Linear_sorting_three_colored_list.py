'''
Given an array of strictly the characters 'R',
'G', and 'B', segregate the values of the array
so that all the Rs come first, the Gs come second,
and the Bs come last. You can only swap elements
of the array. Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R',
'B', 'R', 'G'], it should become ['R', 'R', 'R',
'G', 'G', 'B', 'B'].

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
        ind_mid = 0
        ind_high = len(inp_arr) - 1

        # Iterating over the over till the following
        # condition is not met
        while ind_mid <= ind_high:

            # If the mid index has character 'R' then swap the
            # low and mid value index's elements and increment
            # the position of low and mid index
            if inp_arr[ind_mid] == 'R':
                inp_arr[ind_low], inp_arr[ind_mid] = inp_arr[ind_mid], inp_arr[ind_low]
                low += 1
                mid += 1
            
            elif inp_arr[mid] == 'G':
                mid += 1

            else:
                inp_arr[mid], inp_arr[high] = inp_arr[high], inp_arr[mid]
                high -= 1

    return inp_arr

# taking the input from the user
inp_arr = ['G', 'B', 'R', 'R','B', 'R', 'G']
print("The sorted list is: ", mod_arr(inp_arr))
