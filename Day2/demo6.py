# to create a block of statements use indentation (tab)

"""
if condition:
    statement(s)

if condition:
    statement(s)
else:
    statement(s)

if condition:
    statement(s)
elif condition:
    statement(s)    
else:
    statement(s)    
    
"""

n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))

max = 0

if n1 == n2:
    print("n1 and n2 are equal")
    max = n1
elif n1 > n2:
      print("n1 is greater")
else:
     print("n2 is greater")
     max = n2
print(f"Maximum value : {max}")     