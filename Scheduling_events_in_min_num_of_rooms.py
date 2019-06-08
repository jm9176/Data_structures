'''
Given an array of time intervals (start, end)
for classroom lectures (possible overlapping),
find the minimum number of rooms required.

For e.g. [(30,75),(0,50),(60,150)], the output
should be 2.
'''

# Function returning the minimum no. of rooms
# required for the given lecture schedule
def min_rooms(arr):

    # List containing the schedules which are
    # far down the list but can be adjusted with
    # the earlier rooms. For e.g. (30,75) and (0,30)
    set_rooms = []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            
            # The intervals will intersect if the difference between the extreme
            # end values is less than the addition of the individual interval
            # For e.g. (30,75) and (0,50), range_diff = max(75,50) - min(30,0)
            # while interval_sum = (75-30) + (50-0)
            range_diff = max(arr[j][1], arr[i][1]) - min(arr[j][0], arr[i][0])
            interval_sum = (arr[j][1] - arr[j][0]) + (arr[i][1]- arr[i][0])

            if range_diff < interval_sum and arr[j] not in set_rooms:
                count = 2 + i
            elif arr[j] in set_rooms:
                continue
            else:
                set_rooms.append(arr[j])

    # count variabe returns the min num of required rooms
    return count

# Taking the input from the user
arr = [(30,75),(0,50),(60,150), (0,30), (40,55), (30,40)]
print(min_rooms(arr))

'''
Expected output in this case will be three rooms:
room1: (30,75), (0,30)
room2: (0,50), (60,150)
room3: (40,55), (30,40)
'''
