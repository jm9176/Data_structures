def pair_check(arr, var_sum):
        for var in arr:
            if var_sum - var in arr:
                print "Match found"
                return var, var_sum - var
            else:
                print "Match not found"

arr = []

try:
    for i in range(int(input("Enter the length of the list: "))):
        arr.append(int(input("Enter the elements in the list: ")))
    
    var_sum = int(input("Enter the sum that you want to find: "))
    print pair_check(arr, var_sum)
    
except:
    print "The input is not a number"



