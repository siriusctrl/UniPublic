import math

def newton(n, e):
    theta = n/2
    error = 99999
    count = 0

    while(error > e):
        theta -= (theta**2 - n) / (2*theta)
        error = theta**2 - n
        count += 1

    print("guess", count, "times")
    return theta
