'''
If the input is arr = [2,4,6,2,5]
    var = 2, sw = 2, swo = 0
    max(sw, swo) = 2

    var = 4, psw = 0, pswo = 2
    sw = 4+0 = 4, swo = 2
    max(4,2) = 4

    var = 6, psw = 2, pswo = 4
    sw = 2+6 = 8, swo = 4
    max(8,4) = 8

    var = 2, psw = 4, pswo = 8
    sw = 8+2 = 10, swo = 8
    max(10,8) = 10

    var = 5, psw = 8, pswo = 10
    sw = 8+5, swo = 10
    max(13,10) = 1
    
    return max_sum = 13
'''

# To find the max sum in the given list
# taking non-adjacent elements
def max_sum(arr):

    final_sum = [0,0]

    for var in arr:
        final_sum[0] += var
  
        temp = max(final_sum)
        final_sum[0] = final_sum[1]
        final_sum[1] = temp
        
    return max(final_sum)

# Defined input 
arr = [-2,6,-1,1,5]
print(max_sum(arr))
