
"""
initialization
while  condition:
    statement(s)
    modification

# while condition is true loop body will be executed

initialization
while  condition:
    statement(s)
    modification
else:
    statement(s)

# when condition will become False then else block will be execeuted only once
    
"""
num = int(input("Enter number : "))

# print(f"Table of {num} : ")
# i = 1
# while i <= 10:
#     print(num * i)
#     i += 1

fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
else:
    print(f"i({i}) exceeds num({num})")

print(f"{num}! = {fact}")