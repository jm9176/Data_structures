'''
Given an unordered list of flights taken by someone, each represented
as (origin, destination) pairs, and a starting airport, compute the
person's itinerary. If no such itinerary exists, return null. If there
are multiple possible itineraries, return the lexicographically smallest
one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO','HKO'),('YYZ','SFO'),
('YUL','YYZ'),('HKO','ORD')] and starting airport 'YUL', you should return
the list ['YUL','YYZ','SFO','HKO','ORD'].

Given the list of flights [('SFO','COM'),('COM','YYZ')] and starting
airport 'COM', you should return null.

Given the list of flights [('A','B'),('A','C'),('B','C'),('C','A')] and
starting airport 'A', you should return the list ['A','B','C','A','C']
even though ['A','C','A','B','C'] is also a valid itinerary. However,
the first one is lexicographically smaller.
'''

# Fnction returning the list of person's itinerary
def ret_itinerary(inp_arr, start):
    itinerary = [start]
    lex_str = []
    temp_var = start
    iter_cnt = 0

    # Iterating over the entire input list
    while len(inp_arr) > 0:

        # If the location is not found and the iteration
        # count equals to the len of the inp_arr which is
        # greater than max count value
        if iter_cnt == len(inp_arr):    
            return '{}: Location not found'.format(None)

        # If the start location is found the perform the following
        # operations and make iteration count zero else update the
        # iteration count
        if inp_arr[iter_cnt][0] == start:
            start = inp_arr[iter_cnt][1]
            itinerary.append(start)

            inp_arr.remove(inp_arr[iter_cnt])
            iter_cnt = 0
        else:
            iter_cnt += 1

    # Arranging the itinerary lexicorgraphically and returning the
    # final desired list in iternary. The variable temp_var will
    # generate the strings to arrange iternary alphabetically, which
    # in this case will be AC, ABC and will be stored in lex_str list
    start = temp_var
    temp_var += '-'
    
    for i in range(1,len(itinerary)):

        # separating the strings at each repitition of start value
        if itinerary[i] == start:
            lex_str.append(temp_var[:-1])
            temp_var = itinerary[i] + '-'
        else:
            temp_var += itinerary[i] + '-'

    # Append the last string value and sort the strings in the list
    lex_str.append(temp_var[:-1])
    lex_str.sort()

    itinerary.clear()

    # Generating the iternary order as desired in the question
    for var in lex_str:
        temp = var.split('-')
        itinerary.extend(temp)

    return 'Person itinerary is defined as: {}'.format(itinerary)

# Taking the input from the user
#given_arr = [('SFO','HKO'),('YYZ','SFO'),('YUL','YYZ'),('HKO','ORD')]
given_arr = [('A','B'),('A','C'),('B','C'),('C','A')]
given_start = 'A'
print(ret_itinerary(given_arr, given_start))
