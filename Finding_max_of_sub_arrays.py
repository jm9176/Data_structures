'''
Finding the maximum value in each of the
sub array of size k. If the given array is
[10,5,2,7,8,7] then the resulting output
should be [10,7,8,8].
'''

# this fnction will return the list of
# max element of the sub array
def max_sub(arr, k):
      max_sub_arr = []

      for i in range(len(arr)-k+1):
            max_sub_arr.append(max(arr[i:i+k]))

      return max_sub_arr


# Defining the input list
arr =[10,5,-1,7,8,7]
k = int(input("Enter the size of sub-arrays: "))

print(max_sub(arr, k))
