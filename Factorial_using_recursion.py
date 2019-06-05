# Calculating the factorial using recursion
def fact(n):

      if n == 0:
            return 1

      return n*fact(n-1)

# Taking the input from the user
n = int(input("Enter the no: "))
print(fact(n))


'''
# Calculating factorial using for loop
def fact(n):

      fac = 1

      for i in range(n-1):
            fac = n*fac
            n-= 1

      return fac

# Taking the input from the user
n = int(input("Enter the no: "))
print(fact(n))
'''
