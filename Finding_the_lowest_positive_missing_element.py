'''
Find the lowest positive integer that does not exist in the
array. The array can contain duplicates and negative numbers
as well. For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.
'''

# Function to find and add the lowest positive element
# to the defined input

def input_elem(arr):
    elem_search = 1
    found = 0

    while found == 0:

        if elem_search not in arr:
            arr.append(elem_search)
            found = 1 
            return elem_search, arr
        
        else:
            elem_search += 1

            
# Define the input 
arr = [3,4,-1,1,5,6]
print(input_elem(arr))

