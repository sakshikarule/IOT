
# global variable
num = 10

def function1():
    # local variable
    num = 20
    print(f"inside function1() : num = {num}")

def function2():
    global num
    num = 20
    print(f"inside function2() : num = {num}")

def function3():
    # nonlocal num      # error
    num = 20
    print(f"inside function3() : num = {num}")
    def inner():
        # global num
        nonlocal num
        print(f"inside inner() : num = {num}")
        num = 30
        print(f"inside inner() : num = {num}")

    inner()
    print(f"inside function3() : num = {num}")


print(f"inside main program before : num = {num}")
# function1()
# function2()
function3()
print(f"inside main program after : num = {num}")
