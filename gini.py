# How to use:
# look at solution sheet 12 for an example
# for head line = short
# G(little finger)
#    straight
# p(PE = no) = 1/2
# p(PE = yes) = 1/2
#    bent
# p(PE = no) = 2/2
# p(PE = yes) = 0/2
#
# WHen you have found these values, put them into the function
# With this example, you would write: 
# gini(0,2,1,1) and then get 0.25 which is the correct answer
# remember! you split on the lower value
def g(a,b):
    sum = (a+b)**2
    return 1 - ((a**2)/sum)+((b**2)/sum)

def gini(a,b,c,d):
    return (((a+b)/(a+b+c+d))*g(a,b)) + (((c+d)/(a+b+c+d)) * g(c,d))

print(gini(0,2,1,1))