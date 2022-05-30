
# computeFactorialOfInputAndReturn
# ----
#
# Description
# ------------
# Th-is is a function that takes in a number and returns the factorial of that number
# It is a function because it calls itself until it reaches the base case of 1
#
# Params
# ------
# x
#  a number which we will use for factorial
#
# Returns
# -------
# Factorial of the number
def factorial(x):
    if x <= 1:
        return x
    return x * factorial(x - 1) # factorial function
