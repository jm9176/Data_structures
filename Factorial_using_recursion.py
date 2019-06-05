# Calculating the factorial using recursion
def fact(n):

      if n == 0:
            return 1

      return n*fact(n-1)

# Taking the input from the user
n = int(input("Enter the no: "))
print(fact(n))
