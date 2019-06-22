'''
Given the string "race", you should return "ecarace",
since we can add three letters to it (which is the smallest amount
to make a palindrome). There are seven other palindromes that can
be made from "race" by adding three letters, but "ecarace" comes
first alphabetically. As another example, given the string "google",
you should return "elgoogle".

Approach:
for the palindrome word generation either the reverse of input word
can be added to the front of input word or at the end. For e.g if the
word is 'race', then reverse word will be 'ecar'. So the basic approach
will give us ecar + race or race + ecar, which on further processing
can give ecarace and racecar

'''

# Function returning the independent word list for, prefix addition
# and suffix addition to the input string
def ret_wrdList(inp_str, rev_str, index):

    # list containing all the possible palindrome words
    wrd_list = []

    # Iterating till the rev_str is not empty, till then adding inp_str
    # and rev_str as shown below
    while True:

        if index == -1:
            temp_wrd = rev_str + inp_str
        elif index == 0:
            temp_wrd = inp_str + rev_str
        else:
            raise ValueError('Incorrect index, can only be 0 or -1')

        # adding only the palindrome words
        if inp_str in temp_wrd and temp_wrd == temp_wrd[::-1]:
            wrd_list.append(temp_wrd)

        # Breaking the loop in case the word to be added gets empty
        if rev_str == '':
            break
        elif index == 0:
            rev_str = rev_str[1:]
        elif index == -1:
            rev_str = rev_str[:len(rev_str)-1]
                
    return wrd_list 

# Function returning the list of palindrome words and the word with minimum edits
def ret_plindrme(inp_str):

    rev_str = inp_str[::-1]

    # The third parameter for the function can only be 0 or -1. 0 where the rev_str
    # will be added to the inp_str and -1 where the inp_str is being added to rev_str
    wrd_list = ret_wrdList(inp_str, rev_str,-1) + ret_wrdList(inp_str, rev_str, 0)
    
    # Arranging the words in alphabetical order
    wrd_list.sort()
    
    # Finding the word with minimum edits and calculating the edit length
    min_wrd = wrd_list[0]

    for var in wrd_list:
        if len(var) < len(min_wrd):
            min_wrd = var

    min_edits = len(min_wrd) - len(inp_str)
    
    return min_wrd, min_edits

# Taking the input from the user
inp_str = 'google'
print("Palindrome word with min insertion: ", ret_plindrme(inp_str))


