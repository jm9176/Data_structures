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
                
    return 'Person itinerary is defined as: {}'.format(itinerary)

# Taking the input from the user
given_arr = [('A','B'),('A','C'),('B','C'),('C','A')]
given_start = 'A'
print(ret_itinerary(given_arr, given_start))

''' 
                ANOTHER APPROACH

# Fnction returning the list of person's itinerary
def ret_itinerary(inp_arr, start):
    start_list, dest_list = [], []
    itinerary = [start]

    # separating the start and destination locations in lists
    for var in inp_arr:
        start_list.append(var[0])
        dest_list.append(var[1])

    # Updating the itinerary list using the given start location
    # and the generated start and destination list for different
    # airport arrivals
    for i in range(len(inp_arr)):

        # If the airport fount in the start list else
        # return none
        if start in start_list:        

            # Calculating the index of the current start location
            # and updating the start value by using the index location
            # in the destination list and removing the elements on each
            # performed iteration to keep both the lists balanced
            temp_ind = start_list.index(start)
            start_list.remove(start)

            start = dest_list[temp_ind]
            dest_list.remove(dest_list[temp_ind])

            itinerary.append(start)
            
        else:
            return '{}: Location not found'.format(None)
    
    return 'Person itinerary is defined as: {}'.format(itinerary)

# Taking the input from the user
#given_arr = [('SFO','HKO'),('YYZ','SFO'),('YUL','YYZ'),('HKO','ORD')]
given_arr = [('A','B'),('A','C'),('B','C'),('C','A')]
given_start = 'A'
print(ret_itinerary(given_arr, given_start))
'''
