'''
Stair-case problem: If an object can
take one-step and two-steps at a time. what would
be no. of ways in which an object can reach nth step
For e.g. step_1 = 1
         step_2 = (1,1), (2)
         step_3 = (1,1,1), (2,1), (1,2)
'''

# Function for step-size = 1
def one_step(arr):
    temp = []
    for var in arr:
        temp.append(var + [1])
    
    return temp
    
# Function for step-size = 2
def two_step(arr):
    temp = []
    for var in arr:
        temp.append(var + [2])

    return temp


# Function to generate the ways to reach a
# required step
def staircase(num):
    step_0 = [[1]]
    step_1 = [[1,1],[2]]

    print("No. of ways to reach step {}".format(num))
    for i in range(num-2):
        new_step = one_step(step_1) + two_step(step_0)       
        step_0 = step_1[:]
        step_1 = new_step[:]

    return new_list


# Defining the input
nth_step = int(input("Enter the step: "))
print(staircase(nth_step))
