def dict_arr(arr):
    dict_a = {}
    
    for var in arr:
        if var in dict_a:
            dict_a[var] += 1
        else:
            dict_a[var] = 1

    return dict_a

def max_occ(dict_ar):
    temp_val = 0
    for var in dict_ar:
        if dict_ar[var] > temp_val:
            temp_val = dict_ar[var]
            temp_var = var

    return temp_var, temp_val

arr = [1,2,3,4,3,4,2,1,3,4,1,3,1,2,1,3,3]
dict_ar = dict_arr(arr)

print('The max repetition occurs for {} = {}'.format(max_occ(dict_ar)[0],
                                                     max_occ(dict_ar)[1]))

