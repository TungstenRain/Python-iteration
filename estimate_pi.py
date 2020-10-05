"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 7: Iteration in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.8.5
"""
import math

def factorial(n):
    """
        Compute factorial of n recursively

        return: factorial of n
    """
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        return (n * recurse)

def estimate_pi():
    """
        Computes a numerical approximation of pi

        Algorithm derived from Srinivasa Ramanujan
        from: http://en.wikipedia.org/wiki/Pi

        return: estimate of pi
    """
    # Initiate variables
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        numerator = factorial(4*k) * (1103 + (26390 * k))
        denominator = (factorial(k)**4) * (396**(4 * k))
        term = factor * numerator / denominator
        total += term

        if abs(term) < 1e-15:
            break
        k += 1
    
    return 1 / total

print(estimate_pi())
print(math.pi)