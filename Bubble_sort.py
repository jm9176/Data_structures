'''
The code given below uses a bubble sort approach to
sort the elements in the given array. The average
time complexity is O(n^2)

# IF sort checking is allowed to stop at intermediate step
# then a sorted array of the given input can be stored in
# a temp array and can be compared with each iteration
#
# ELSE another way to check is to initialize a counter to check
# if there was no swap for a particular iteration, at that point
# stop the loop and return the inp_arr

#1st APPROACH

# Function returning the sorted array
def bubble_sort(inp_arr):
    
    sort_chk = 0
    temp_arr = inp_arr.copy()
    temp_arr.sort()

    # Iterating over the loop  
    for i in range(len(inp_arr)):
        for j in range(len(inp_arr)-i-1):

            if inp_arr[j] > inp_arr[j+1]:
                inp_arr[j], inp_arr[j+1] = inp_arr[j+1], inp_arr[j]
            
            if inp_arr == temp_arr:
                return inp_arr
                
    return inp_arr

# Taking the input from the user
given_arr = [5,4,3,2,1]
print("The final array using bubble sort is: {}".format(bubble_sort(given_arr)))


#2nd APPROACH

# Function returning the sorted array
def bubble_sort(inp_arr):

    # Iterating over the loop  
    for i in range(len(inp_arr)):
        
        # variable to check if the sorting is done without completing
        # all the iterations
        sort_chk = 0
        
        for j in range(len(inp_arr)-i-1):
    
            if inp_arr[j] > inp_arr[j+1]:
                inp_arr[j], inp_arr[j+1] = inp_arr[j+1], inp_arr[j]
            else:
                sort_chk += 1
            
            # if there was no swap in this loop iteration then the
            # inp_array has been sorted
            if sort_chk == len(inp_arr)-i-1:
                return inp_arr

# Taking the input from the user
given_arr = [2,1,2,4,1,0,1]
print("The final array using bubble sort is: {}".format(bubble_sort(given_arr)))
'''

# Normal APPROACH

# Function returning the sorted array
def bubble_sort(inp_arr):
    
    # Iterating over the list
    for i in range(len(inp_arr)):
        for j in range(len(inp_arr)-i-1):

            if inp_arr[j] < inp_arr[j+1]:
                continue
            else:
                inp_arr[j], inp_arr[j+1] = inp_arr[j+1], inp_arr[j]

    return inp_arr

# Taking the input from the user
given_arr = [5,4,3,2,1]
print("The final array using bubble sort is: {}".format(bubble_sort(given_arr)))
