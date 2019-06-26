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

Since the question only asks for only one non-duplicate element
so a case where there is no non-duplicate element is not considered
however, this can be checked in the initial FOR loop while calculating
the sum by using a counter for the num of zeros and following

if odd_sum%3 == eve_sum%3 and count_zeros == 3:
        return "Input contains no non-duplicate element"        
'''

# Function returning the non-duplicate element
def ret_ndp(inp_arr):

    # Variables to store the sum of evena and odd elements using the given input
    eve_sum = 0
    odd_sum = 0

    # Calculating the total sum of odd elements and even elements and taking
    # absolute for the negative values in order to avoid subtraction
    for var in inp_arr:

        if var % 2 == 0:
            eve_sum += abs(var)
        else:
            odd_sum += abs(var)

    # to check if there is a single zero element and at the same,
    # both even and odd element sum gives 0 remainder when divided by 3
    if odd_sum%3 == eve_sum%3 and 0 in inp_arr:
        return "Input contains non-duplicate 0 value at index: {}".format(inp_arr.index(0))
    
    # Iterating over the list for len(inp_arr) times, where temp_eve and
    # temp_odd stores the total corresponding sum (even/odd) minus the
    # current element
    for var in inp_arr:
        
        if var % 2 == 0:
            temp_eve = eve_sum - abs(var)

            if temp_eve%3 == odd_sum%3:
                return "Non-duplicate element is: {}".format(var)

        else:
            temp_odd = odd_sum - abs(var)

            if temp_odd%3 == eve_sum%3:
                return "Non-duplicate element is: {}".format(var)


# Taking the input from the user
given_arr = [6,-1,6,6,-1,-1,0,0,0,4]
print("{}".format(ret_ndp(given_arr)))





