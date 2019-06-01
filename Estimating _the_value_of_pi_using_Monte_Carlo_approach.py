'''
Approximating the calue of pi using Monte-Carlo
method to 3 decimal places. Use a one-fourth
region of a square (side = 1 unit) and define
a circular arc in it with radius 1 unit. Count
the no. of randomly generated points inside the
square region. Dividing the pts inside by total
will give a value equal to pi/4. 
'''
import numpy as np

def pi_est(num_iter):
    pt_in = 0.0
    pt_out = 0.0

    # Generating num_iter uniformly
    for i in range(num_iter):

        x = np.random.uniform(0,1)
        y = np.random.uniform(0,1)

        if pow(x,2) + pow(y,2) <= 1:
            pt_in += 1

        else:
            pt_out += 1

    pi = 4*(pt_in/(pt_in + pt_out))
    pi = round(pi,3)
    
    return pi

# Taking the iteration value from the user
num_iter = int(input("Enter the no. of iterations: "))
print(pi_est(num_iter))
