
# define some constants
PI = 3.142

# define few functions
def sum(p1, p2):
    return p1 + p2

def diff(p1, p2):
    return p1 - p2

def factorial(n):
    fact = 1 ;  i = 1
    while i <= n:
        fact *= i
        i += 1
    return fact

print(f"__name__ = {__name__}")
print(f"PI = {PI}")
print(f"sum(10, 20) = {sum(10, 20)}")
print(f"diff(20, 10) = {diff(20, 10)}")
print(f"5! = {factorial(5)}")