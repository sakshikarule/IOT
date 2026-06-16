# input() function is used to take value from user
# returns value in type str

# typecasting - changing type of value
#   int(value)  - type will be changed to int
#   float(value)  - type will be changed to float
#   str(value)  - type will be changed to str

print("Enter value1 : ", end=" ")
value1 = input()
print(f"value1 = {value1}")
print(f"type(value1) = {type(value1)}")

print("Enter value2 : ",end=" ")
value2 = input()
print(f"value2 = {value2}")
print(f"type(value2) = {type(value2)}")

print("Enter value3 : ", end="")
value3 = float(input())
print(f"value3 = {value3}")
print(f"type(value3) = {type(value3)}")