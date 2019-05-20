'''
Defining the fibonacci series where the input
is given by the user in terms of the series
length
'''

def series(series_len):
    var_1 = 0
    var_2 = 1
    fibb_series = []

    for i in range(series_len):
        fibb_series.append(var_1)
        var_sum = var_1 + var_2
        var_1 = var_2
        var_2 = var_sum

    return fibb_series

try:
    series_len = int(input("Enter the series length: "))
    print(series(series_len))

except:
    print("Not a number")

'''
# using the list
def series(series_len):
    fibb_series = [0,1]

    for i in range(2,series_len):
        fibb_series.append(fibb_series[i-2] + fibb_series[i-1])

    return fibb_series

try:
    series_len = int(input("Enter the series length: "))
    print(series(series_len))

except:
    print("Not a number")
'''