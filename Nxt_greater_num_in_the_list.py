'''
For a given list of elements return the next
greater element in the list from the remaining
list of elements. If the element if the largest
in the list then return -1 and same for the
elements after that

For e.g. if the given list is [4,5,2,25].
The output should be [5,25,25,-1]
'''

# Function returning the list of next greater
# element to the current element in the list.
# It takes the defined list of numbers
def rtd_gtr(arr):

    # List storing the next greater element
    gtr_list = []

    # Iterating over the entire list elements
    for i in range(len(arr)):

        # Initial condition to assign a maximum
        # value to a temp variable. If the list
        # element is the last element, then add
        # -1 to the gtr_list
        if i < len(arr) - 1:
            temp = max(arr[i:len(arr)])
        else:
            gtr_list.append(-1)
            return gtr_list

        # Condition for the intermediate element.
        # If the element is the largest in the list
        # then add -1 to gtr_list and move to the
        # next iteration
        if arr[i] == temp:
            gtr_list.append(-1)
            continue

        # Loop to find the greater element from the
        # remaining list, such that the element is
        # next greater than the selected element
        for j in range(i, len(arr)):
            if arr[j] > arr[i] and arr[j] < temp:
                temp = arr[j]

        gtr_list.append(temp)


# Taking the input from the user
arr = [3, 1, 8, 2, 3, 1, 8.5, 0, 12, 32, 20]

# Check if all the elements in the list are numbers
# else raise an error
try:
    inp_arr = [var for var in arr if float(var)]
    print(rtd_gtr(inp_arr))
except:
    raise ValueError
