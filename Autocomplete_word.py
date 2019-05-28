'''
If a letter is used as an input lets say 'd',
the function will return the list of possible words
starting with that letter. If the input is now further
changed to 'de' then the list will get updated to return 
the related words starting with de and so on.
'''

# Function to return the suggestions
def autocomplete(var, dict_map):
    suggestions = []
    len_inp = len(var)

    for word in dict_map:
        if word[:len_inp] == var:
            suggestions.append(word)

    return suggestions 


# Initializing the input variable
var = ''

# defining the dictionary map for
# words starting with letter 'd'
dict_map = {'dark',
            'dear',
            'den',
            'deer',
            'doll',
            'donkey',
            'double'
            }

# Running the loop to take the input 
# till the actual word is not found
while var not in dict_map:
    var = input("Enter the input letter: ")
    print(autocomplete(var, dict_map))
