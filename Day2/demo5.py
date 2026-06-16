str = """This is a
        multiline string"""

print(f"str = {str}")
print(f"type(str) = {type(str)}")

#   # is a single line comment
#   multiline strings can be used to give multiline comments (do not assign value to the variable)


"""
operators:
    - Arithmetic operators :    +, -, *, /, %, **, //
    - Relational operators :    <, >, <=, >=, ==, !=
    - Logical operators    :    and, or, not
    - Bitwise operators    :    &, |, ^, ~, <<, >>
    - assignment operators :    =, +=, -=, ...., &=, |=, ...
"""
"""

le = int(input("Enter rectangle length : "))
br =   int(input("Enter rectangle breadth : "))

area = le * br

print(f"Length = {le}, Breadth = {br}")
print(f"Area of a reactangle = {area}")

"""
"""
radius = int(input("Enter radius of a circle : "))

area = 3.142 * radius ** 2

print(f"Radius of a circle = {radius}")
print(f"Area of a circle = {area}")

"""
# relational operators always results in True or false
num1 = 100
num2 = 200

print(f"num1 < num2 = {num1 < num2}")  #True
print(f"num1 > num2 = {num1 > num2}")  #False
print(f"num1 == num2 = {num1 == num2}") #false
print(f"num1 != num2 = {num1 != num2}") #True