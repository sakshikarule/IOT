
# Multiple Assignment

var = 10
print(f"var = {var}")

var1 = var2 = var3 = 10
print(f"var1 = {var1}")
print(f"var2 = {var2}")
print(f"var3 = {var3}")

var1, var2, var3 = 10, 20, 30
print(f"var1 = {var1}")
print(f"var2 = {var2}")
print(f"var3 = {var3}")

c1, c2, c3 = "sun"
print(f"c1 = {c1}, c2 = {c2}, c3 = {c3}")

def calculate(op1, op2):
    sum = op1 + op2
    diff = op1 - op2
    return sum, diff

s, d = calculate(200, 100)

print(f"s = {s}")
print(f"d = {d}")