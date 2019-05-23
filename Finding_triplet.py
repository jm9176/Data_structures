# Find the pythagorean triplet in an array
# if the input is arr = [1,2,3,4,5]
# the output should return (3,4,5)

def py_triplet(arr):
    pair_list = []
    c_list = []

    for i in range(len(arr)):
        arr_temp = arr[:]
        
        temp = arr_temp[i]
        arr_temp.remove(arr_temp[i])

        for j in range(len(arr_temp)):
            c = pow((pow(temp,2))+(pow(arr_temp[j],2)),0.5)
            if c in arr_temp:

                # if statement to avoid the repetition
                # a pair for e.g. (3,4,5), (4,3,5)
                # as both of them represent the same c value
                # This statement can be removed in case multiple
                # occurrences of c are allowed

                if c not in c_list:
                    c_list.append(c)
                    pair_list.append([temp, arr_temp[j], int(c)])

    return pair_list

# Input list
arr = [-1,2,-3,4,5,6,7,8,9,10]
print(py_triplet(arr))
                
                            
