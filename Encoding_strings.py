'''
Representing repeated successive characters as a
single count and character.
For e.g. If the string is "AAAABBBCCDAA", then
the output should return "4A3B2C1D2A"
'''

# Function returning the desired output string
def decd_str(inp_str):

    # Condition to check if input is empty
    if inp_str == '':
        return "input string is empty"
    
    # Variable representing the final output,
    # character value and count
    out_str = ''
    temp_val = inp_str[0]
    temp_cnt = 0

    # Iterating over the length of the inp_str
    for i in range(len(inp_str)):
        
        # Incrementing cnt for each repetition
        if temp_val == inp_str[i]:
            temp_cnt += 1
        else:
            out_str += str(temp_cnt) + temp_val
            temp_val = inp_str[i]
            temp_cnt = 1

    # Adding the last element and the final count
    out_str += str(temp_cnt) + temp_val

    return out_str

# Taking the input from the user
inp_str = "AABBBC22222$$$"
print(decd_str(inp_str))
