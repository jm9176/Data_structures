'''
Compute the running median of a sequence of numbers.
That is, given a stream of numbers, print out the median
of the list so far on each new element.

Recall that the median of an even-numbered list is the average
of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your
algorithm should print out: 2, 1.5, 2, 3.5, 2, 2, 2
'''
# Function returning the median value based on the curent list
# and printing the elements currently in the list
def ret_med(inp_arr):

    print("Current list: ", inp_arr)

    # sorting the list in the increasing order
    inp_arr.sort()

    # Condition to check for odd or even num of elements
    if len(inp_arr)%2 == 0:
        temp = len(inp_arr)
        med = (inp_arr[int(temp/2)-1] + inp_arr[int((temp+2)/2)-1])/2
    else:
        temp = len(inp_arr)
        med = inp_arr[int((temp+1)/2)-1]

    return med

# Taking the input from the user in form a stream
# and updating the previous list using the append command
inp_arr = []

# Keep iterating until stopped by the user
while True:
    usr_inp = input("Enter the integer value: ")
    if usr_inp == 'stop':
        print("Loop stopped by the user")
        break

    elif usr_inp == '':
        print("The input list is empty")

    elif usr_inp != '':
        inp_arr.append(int(usr_inp))
        print("Current median: ",ret_med(inp_arr))
