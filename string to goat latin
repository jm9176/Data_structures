def string_to_goat_latin(var):
    var_list = var.split(' ')
    add_a = 'a'

    for var in var_list:

        if var[0] in 'aeiouAEIOU':
            var = var + 'ma'

        else:
            temp = var[0]
            var.remove(temp)
            var = var + temp + 'ma'

        var = var + add_a
        add_a = add_a + 'a'
        
        result += var + ' '

    return result
    
given_string = 'My name is abc'
print(string_to_goat_latin(given_string))
  
