# Function to return the suggestions
def autocomplete(var, dict_map):
    suggestions = []
    len_inp = len(var)

    for word in dict_map:
        if word[:len_inp] == var:
            suggestions.append(word)

    return suggestions 


# Taking the input from the user
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

# Running 
while var not in dict_map:
    var = input("Enter the input letter: ")
    print(autocomplete(var, dict_map))
