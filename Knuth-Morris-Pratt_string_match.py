'''
Knuth-Morris-Pratt (KMP) algorithm for string matching. The difference
between normal approach and KMP approach is as follows:
In case of normal iteration (lets say using for loop), the iteration will
occur for one step at a time, although there was a partial match in case of
previous iteration. However, in case of the KMP approach, the iteration
will skip the partially matched indexes to speed up the process.
'''
# Function returning the index from where the pattern matching start
# if there is a match, using KMP approach
def ret_string_match(inp_str, inp_patt):

    # Indexes for given string and pattern, and curr_index storing
    # the index from where the match starts to occur
    i, j = 0, 0
    curr_index = 0

    # Iterating over the given pattern and string to find the match
    while i < len(inp_str):

        # If the current element matches then iterate over to
        # the next element for the pattern. Else turn index
        # for pattern to 0 and record the current indexx as well
        if inp_str[i] == inp_patt[j]:
            j += 1
        else:
            j = 0
            curr_index = i

        # If the length of the pattern matches the index length using
        # curr_index, then return the index value for the pattern
        if i - curr_index == len(inp_patt) - 1:
            return 'Match found at starting index: {}'.format(curr_index + 1)

        i += 1

    # If there is no match
    return 'Match not found'

# Taking the input from the user
given_str = 'abcdefghi'
given_patt = 'def'
print(ret_string_match(given_str, given_patt))

