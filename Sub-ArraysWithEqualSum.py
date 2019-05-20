# Splitting an array to two
# sub-arrays with equal sum
def split(arr):
    l_sum, r_sum = 0, 0                             # sum of left and right sub-arrays
    left_arr=[]                                     # left sub-array
    right_arr=[]                                    # right sub-array

    status = False                                  # status to check sum equality of the sub-arrays
    count=1                                         # Backward count for the array

    if sum(arr)%2 == 0:
        print("Split exist")
        left_arr.append(arr[len(arr)-count])
        count += 1

        # Keep running the loop till the sum of sub-array is
        # not half the total sum
        while status == False:
            l_sum = sum(left_arr) + arr[len(arr) - count]
            print(len(arr)-count)

            if l_sum == r_sum:
                left_arr.append(arr[len(arr)-count])
                status = True

            elif l_sum > sum(arr)/2:
                right_arr.append(arr[len(arr)-count])
                count += 1

            else:
                l_sum = l_sum + arr[len(arr)-count]
                left_arr.append(arr[len(arr)-count])
                count += 1

            if count > len(arr):
                status = True

        # To check if the sub-arrays has the equal sum
        if sum(left_arr) != sum(right_arr):
            print("Cannot be divided")
        else:
            print("Match found")

    else:
        print("No Split")

    return left_arr, right_arr

# Define an array with non-negative numbers
arr = [1,2,3,4,1]

print(sum(arr), split(arr))

