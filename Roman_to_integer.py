'''
Roman numerals are usually written largest to smallest from left
to right. However, the numeral for four is not IIII. Instead, the
number four is written as IV. Because the one is before the five
we subtract it making four. The same principle applies to the number
nine, which is written as IX. There are six instances where subtraction
is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed
to be within the range from 1 to 3999.
'''

# Function returning the integer value to the given Roman input
def romanToInt(inp_str):

    if not inp_str:
        return 'Input is empty'

    # Dictionary storing the integer value to the corresponding
    # Roman value
    dict_rom = {'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000
                }

    # Returned integer value and index for the iteration
    int_val = 0
    i = 0

    # Iterating over the given input
    while i<len(inp_str):

        # Checking for the subtraction in the roman value by comparing with the
        # next index value
        if i != len(inp_str)-1 and dict_rom[inp_str[i+1]] > dict_rom[inp_str[i]]:
            int_val += (dict_rom[inp_str[i+1]] - dict_rom[inp_str[i]])
            i += 1
        else:
            int_val += dict_rom[inp_str[i]]

        # Incrementing the counter value
        i += 1

    return 'Integer value for the given input {} is: {}'.format(inp_str,int_val)


# Taking the input from the user
given_str = ''
print(romanToInt(given_str))
