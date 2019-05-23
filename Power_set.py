# Function to return the power set of the given array
def power_set(arr):
   
   # The final list containing
   # the power-set of the input array
   # An temp list ot store the new sets
   # Count variable to check the output response
   
   power_list = [[]]
   list = []
   count = 1

   for var in arr:
       for var1 in power_list:
           list.extend([var1 + [var]])
           count += 1

       power_list.extend(list)
       list.clear()

   print(count)
   return power_list

# Input array
arr = [1,2,3,4,5]
print(power_set(arr))

'''
# Using comprehension

def power_set(arr):
    power_list = [[]]

    for var in arr:
        power_list.extend([var1 + [var] for var1 in power_list])

    return power_list

arr = [1,2,3,4,5]
print(power_set(arr))
'''
