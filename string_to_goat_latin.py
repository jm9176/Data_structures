def string_to_goat_latin(var):
    var_list = var.split(' ')
    add_a = 'a'
    resulting_string = ''

    for var in var_list:

        if var[0] in 'aeiouAEIOU':
            var = var + 'ma'

        else:
            temp = var[0]
            var.replace(temp,'')
            var = var + temp + 'ma'

        var = var + add_a
        add_a = add_a + 'a'
        
        resulting_string += var + ' '

    return resulting_string
    
given_string = 'My name is abc'
print(string_to_goat_latin(given_string))
  
