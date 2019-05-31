# Function to return the longest substring
# with k distinct characters
def substring(arr, k):
    substr = []

    # Generating a list of all the sub-strings
    # with length greater than and equal to k
    for i in range(len(arr)-k+1):
        for j in range(0,len(arr)-i-1):
            if len(arr[i:len(arr)-j]) >= k:
                substr.append(arr[i:len(arr)-j])

    temp_val = 0

    # Finding the larget substring from substr
    # with k distinct characters
    for var in substr:
        dict_char= {}

        for var1 in var:
            if var1 not in dict_char:
                dict_char[var1] = 1

        if len(dict_char) == k:
            if len(var) > temp_val:
                temp_val = len(var)
                temp_var = var

    
    return temp_var


# Defining the input string
arr = 'aabsca'
k = int(input("Required distinct characters: "))

print(substring(arr, k))

