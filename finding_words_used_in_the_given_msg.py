'''
Returning the dictionary words used in the
input string.
For e.g. If the given input is 'thequickbrownfox'
then the output should return a list containing the
words used in the message.
rtd_list = ['the','quick','brown','fox']
'''

# Function to return the list of words as
# found in the dictionary by comparing the
# input string with the keys in the dictionary

#what if the word is not in the dictionary
def wrd_list(msg):

    # word dictionary containing some random words
    dict_wrd = {'the',
                'to',
                'quick',
                'quest',
                'brown',
                'fox'}

    final_list = []
    temp_msg = ''

    # looping over the message to compare
    # with the word in the dictionary
    for i in range(len(msg)):
        temp_msg += msg[i]

        if temp_msg in dict_wrd:
            final_list.append(temp_msg)
            temp_msg = ''


    return final_list

# Defining the input given by the user
msg = 'thequickbrownfox'
print(wrd_list(msg))
