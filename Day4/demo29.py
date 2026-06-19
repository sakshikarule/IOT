def sum(p1,p2):
    return p1 + p2

def diff(p1,p2):
    return p1 - p2

def calculate(p1, p2, func):
    return func(p1,p2)

def outer():
    print("inside outer() function")

    def inner():
        print("inside inner() function")

    return inner

print(f"10 + 20 = {sum(10, 20)}")
print(f"20 - 10 = {diff(20, 10)}")    

res = calculate(20, 10, sum)
print(f"sum = {res}")

res = calculate(20, 10, diff)
print(f"diff = {res}")

func = outer()

print(f"type(func) = {type(func)}")

func()