'''
Given a string, find the longest palindromic contiguous
substring. If there are more than one with the maximum
length, return any one.

For example, the longest palindromic substring of "aabcdcb"
is "bcdcb". The longest palindromic substring of "bananas"
is "anana".
'''

#Function returning the palindrome with maximum length
def ret_palindrome(inp_str):

    # To check the existence fo plaindrome sub-strings in case length
    # of the input is 1 and 2, thereby avoiding the for loop
    if len(inp_str) == 1 or len(inp_str) == 0:
        return 'Input too small for Palindrome'
    
    elif len(inp_str) == 2:
        if inp_str[0] == inp_str[-1]:
            return 'Max. palindrome sub-string is: {}'.format(inp_str)
        else:
            return 'No palindrome exist'

    # Creating an empty list which will store the plaindrome sub-strings
    pali_str = []
    max_len = 0
    
    # Iterating over the given input to find the palindrome sub-string
    for i in range(len(inp_str)):
        for j in range(len(inp_str[i:])-2):

            # Creating a sub-string, such that the length of the sub-string
            # is reduced by one element with each iteration in the j-loop
            temp_str = inp_str[i:-1-j]
            temp_len = int(len(temp_str)/2)

            # To check if the current sub-string is of even length
            if len(temp_str)%2 == 0 and len(temp_str)>1:
                temp_str1 = temp_str[:temp_len]
                temp_str2 = temp_str[temp_len:]

                # If 1st half is equal to 2nd then append to palndrome list
                if temp_str1 == temp_str2[::-1]:
                    pali_str.append(temp_str)

                    # Updating the sub-string with palindrome having max length
                    if len(temp_str) > max_len:
                        max_str = temp_str
                        max_len = len(temp_str)
                        
            # To check if the current sub-string is of odd length
            else:

                # creating half strings about the center element
                # For e.g. if ana, then str1 = a, str2 = a, center = n
                temp_str1 = temp_str[:temp_len]
                temp_str2 = temp_str[temp_len+1:]
                
                if temp_str1 == temp_str2[::-1]:
                    pali_str.append(temp_str)

                    if len(temp_str) > max_len:
                        max_str = temp_str
                        max_len = len(temp_str)

    # Displaying the current list of palindromes
    print('List of palindromes: {}'.format(pali_str))

    # Returning the final output
    if not pali_str:
        return 'No palindrome exist'
    else:
        return 'Max. palindrome sub-string is: {}'.format(max_str)

# Taking the input from the user
given_str = 'bananas'
print(ret_palindrome(given_str))
