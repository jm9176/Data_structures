# Function returning the
def ret_pair(inp_arr, req_sum):

    # To initially check the input list
    if not inp_arr:
        return 'input is empty'
        
    pair_count = 0
    i, j = 0, len(inp_arr) - 1
    
    # Iteratig over the given list
    while i<j:

        # To check the sum of the end elements
        if inp_arr[i] + inp_arr[j] < req_sum:
            pair_count += j-i
            i += 1
        else:
            j -= 1

    return pair_count

# Taking the input from the user
given_arr = [2,4,6,7,9]
given_sum = 14
print(ret_pair(given_arr, given_sum))

