'''
 Rotating a matrix by a given angle
 if the input is arr =[[1,2,3],
                       [4,5,6],
                       [7,8,9]]

 The output will be
 ccw-arr = [[3,6,9],
            [2,5,8],
            [1,4,7]]

 cw-arr = [[7,4,1],
           [8,5,2],
           [9,6,3]]

Approach:
1. Finding the transpose
2. Swapping the row for ccw
   and cols for cw
        
'''

# Finding the transpose of a 2d matrix
def mat_trans(arr):
    trans_arr = [[0 for i in range(len(arr))] for j in range(len(arr))]
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            trans_arr[i][j] = arr[j][i]   
    return trans_arr

# Finding the rotation matrix for a given input
def mat_rot(arr,direct):
    trans_arr = mat_trans(arr)
    rot_arr = []
    
    if direct == 'ccw': 
        for i in range(len(arr)):
            rot_arr.append(trans_arr[-1-i])

    elif direct == 'cw':
        for i in range(len(trans_arr)):
            rot_arr.append(trans_arr[i][::-1])

    return rot_arr


# Input matrix
arr=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]
    ]


print("Matrix transpose", mat_trans(arr))
print("Rotation matrix", mat_rot(arr, 'cw'))

