# Coverting teh given string to goat latin language using following rules:
# In case of a vowel in a word, add 'ma' at the end of the word
# In case of a consonant put the first letter at the end and add 'ma' at the end
# for each processed word increment the add of a letter 'a' at the end

# For the given input 'My name is abc'
# The output will be 'yMmaa amenmaaa ismaaaa abcmaaaaa'

def string_to_goat_latin(var):
    var_list = var.split(' ')
    add_a = 'a'
    resulting_string = ''

    for var in var_list:

        if var[0] in 'aeiouAEIOU':
            var = var + 'ma'

        else:
            temp = var[0]
            var = var.replace(temp,'')
            var = var + temp + 'ma'

        var = var + add_a
        add_a = add_a + 'a'
        
        resulting_string += var + ' '

    return resulting_string
    
given_string = 'My name is abc'
print(string_to_goat_latin(given_string))
  
