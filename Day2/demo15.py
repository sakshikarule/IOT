def function(p1,p2,p3):
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    print(f"p3 = {p3}")

    # function1(10, 20, 30)
# function1(10, 20)       # error
# function1()             # error

# default parameters
def function1(p1 = 0, p2 = 0, p3 = 0):
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    print(f"p3 = {p3}")

# function1(10, 20, 30)
# function1(10, 20)           # for p3 default value will be used
# function1()                 # for all parameters default value will be used

# keyword arguments
#   function arguments can be passed in key value pair
# function1(p2=20, p3=30)
# function1(p2=20)

# function1(10, p2=20, p3=30)
# function1(p1=10, p2=20, 30)   # error
