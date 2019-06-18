'''
The edit distance between two strings refers to the minimum
number of character insertions, deletions, and substitutions
required to change one string to the other. For example, the
edit distance between “kitten” and “sitting” is three: substitute
the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
'''

# Function returning the modified string depending on the requirement
def rtr_edit(inp_str1, inp_str2):

    # Counter for the minimum num of edits
    num_edits = 0

    # Condition to check the length of the two string, therefore
    # removing or appending elements as per the desired output
    # The num of edits will be given by the total num of elements
    # appended or removed
    if len(inp_str1) > len(inp_str2):
        num_edits += len(inp_str1) - len(inp_str2)
        inp_str2 += inp_str1[len(inp_str2):len(inp_str1)]
    else:
        num_edits += len(inp_str2) - len(inp_str1)
        inp_str2 = inp_str2.replace(inp_str2[len(inp_str1):len(inp_str2)],'')

    # Iterating over the entire string to compare the remaining characters
    for i in range(len(inp_str2)):
        if inp_str2[i] == inp_str1[i]:
            continue
        else:

            # Replacing the character only at that particular index, rather than multiple occurrences of the
            # same character in the whole string
            inp_str2 = inp_str2[0:i] + inp_str2[i].replace(inp_str2[i],inp_str1[i]) + inp_str2[i+1:len(inp_str2)]
            num_edits += 1

    return num_edits

# Taking the input from the user
inp_str1 = 'kitten'
inp_str2 = 'sitting'

print("Minimum num of edits required are: {}".format(rtr_edit(inp_str1, inp_str2)))
