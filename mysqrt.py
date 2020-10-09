"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 7: Iteration in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.8.5
"""
import math

def mysqrt(a):
    """
        Loop to calculate the square root of a given number. X is the initial estimate (in this case 10) and improves until it quits changing

        a: integer
        return: the value of the square root
    """
    x = 10
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x

def test_square_root():
    """
        Test and print the differences between the mysqrt function and the math.sqrt function
    """
    # Print table header
    print("a".ljust(5) + "mysqrt(a)".ljust(15) + "math.sqrt(a)".ljust(15) + "diff".ljust(4) + "\n" + " ".rjust(4, "-") + " ".rjust(15, "-") + " ".rjust(15, "-") + "----")
    # begin looping through the integers
    for i in range(1, 10, 1):
        my_square_root = mysqrt(i)
        math_square_root = math.sqrt(i)
        diff = my_square_root - math_square_root
        print(str(float(i)).ljust(5) + str(round(my_square_root, 10)).ljust(15) + str(round(math_square_root, 10)).ljust(15) + str(diff))

# Call the test_square_root function and display results
test_square_root()