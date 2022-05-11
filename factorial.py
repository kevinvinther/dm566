
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
def computeFactorialOfInputAndReturnDoesNotWork(x):
    if x <= 1:
        return x
    return x * computeFactorialOfInputAndReturnDoesNotWork(x - 1) # factorial function

# result = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
print(computeFactorialOfInputAndReturn(7))
