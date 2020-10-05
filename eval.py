"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 7: Iteration in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.8.5
"""
def user_input():
    """
        Request user to enter a string to be evaluated

        return: string to be evaluated
    """
    return input("Please enter something to be evaluated by the function eval. Type 'done' when finished.\nEnter text here: ")

def evaluate_string():
    """
        Evaluate a string provided by the user
    """
    print("Welcome to the evaluation program.\n")
    to_be_evaluated = user_input()
    while to_be_evaluated != "done":
        print(str(eval(to_be_evaluated)))
        to_be_evaluated = user_input()
    
    print("Thank you for trying this out.")

evaluate_string()