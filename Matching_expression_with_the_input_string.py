'''
Given an input string (s) and a pattern (p), implement regular
expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and
characters like . or *.
'''

def ret_status(inp_exp, inp_str):

    # Storing the original inp_exp to be used later for restoring
    # in case the match is not found
    temp = inp_exp

    # Iteration index variable for inp_str, and incrementing it
    # accordingly in case a condition is satisfied
    j = 0

    # If the following condition is true then there is
    # no point to check or modify the expression
    if len(inp_str) > len(inp_exp):
        print("No match available")
        return False

    else:

        # Iterating over the inp_exp based on the given inp_str
        # to find the match
        for i in range(len(inp_exp)):

            if inp_str[j] == inp_exp[i]:
                continue

            # If the expression is '.' then replace it directly with
            # the corresponding element of the inp_str
            elif inp_exp[i] == '.':
                inp_exp = inp_exp.replace(inp_exp[i], inp_str[j])

            # If the expression is * then check for the previous element
            # and the current index
            elif inp_exp[i] == '*':
                if i==0:
                    inp_exp = inp_exp.replace(inp_exp[i],inp_str[j])

                # if the index is greater than 0, then check for the previous
                # element, and compare with the inp_str
                elif ord(inp_str[j])-96 >= ord(inp_exp[i-1])-96:
                    inp_exp = inp_exp.replace(inp_exp[i],inp_str[j])

                else:
                    # If match not found then restoring the expression to
                    # its original state by reverting the changes
                    inp_exp = temp
                    j = 0
            
            # Incrementing the index for the inp_str
            j += 1
            
            # Check if inp_exp has been modified to contain the full inp_str
            # If yes, then stop the iteration and return the new expression
            if inp_str in inp_exp:
                print("New expression: {}".format(inp_exp))
                return True

# Taking the input from the user
inp_exp = 'c*a*bbb.'
inp_str = 'aab'
print(ret_status(inp_exp, inp_str))
