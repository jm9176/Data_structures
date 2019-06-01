'''
Find the nth term in the series,
14,28,20,40,32,64...
'''

# Function returning a series till the
# nth number
def nth_num(n):
    arr = [14]

    if n < 1:
        return "Invalid input"

    for i in range(1,n):
        if i%2 == 1:
            arr.append(2*(arr[i-1]))

        else:
            arr.append((6*i) + 8)

    return arr


# Taking the input from the user
n = int(input("Enter the nth num to be found: "))
print(nth_num(n))

'''
Finding only the number

# Function returning only the desired
# number
def nth_num(n):

    if n == 1:
        num = 6*(n) + 8
    elif n%2 == 1:
        num = 6*(n-1) + 8
    elif n%2 == 0:
        temp = 6*(n-2) + 8
        num = 2*temp
    else:
        num = None
        print("Invalid input")
        
    return num


# Taking the input from the user
n = int(input("Enter the nth num to be found: "))
print(nth_num(n))

'''
