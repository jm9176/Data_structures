# function to define the array rotation
# a value n
# if the input is arr = [1,2,3,4,5,6,7]
# and the rotation factor is 3 then the
# output should be arr = [4,5,6,7,1,2,3]

def arr_rot(arr, shift):
    
    for i in range(shift):
        temp = arr[0]
        for i in range(len(arr)):
            if i < len(arr) - 1:
                arr[i] = arr[i+1]
            else:
                arr[i] = temp
        

    return arr

arr = [1,2,3,4,5,6,7]
print(arr_rot(arr,4))
