'''
Given an array of integers where every integer occurs
three times except for one integer, which only occurs
once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1.
Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.

Using the following code:
If the input is [6,-1,6,6,-1,-1,0,0,0,4], then output is 4
If the input is [6,-1,6,6,-1,-1,0], then output is 0
'''

# Function returning the non-duplicate element
def ret_ndp(inp_arr):
    bin_sum = 0
    min_cnt = 0

    # Iterating over the given element list to get the
    # binary output of all the binary values
    for var in inp_arr:
        if var < 0:
            min_cnt += 1
        bin_sum += int(bin(abs(var))[2:])

    # converting the int value to string to perform further
    # iteration
    bin_sum = str(bin_sum)

    # check for the num of negative values
    if min_cnt%3 == 1:
        temp = '-'
    else:
        temp = ''

    # generating the final output by checking the divisibility by 3
    for i in range(len(bin_sum)):
        temp += str(int(bin_sum[i])%3)
        
    return int(temp,2)


# Taking the input from the user
given_arr = [26,-1,26,26,-1,-1,0,0,0,-3]
print("{}".format(ret_ndp(given_arr)))


