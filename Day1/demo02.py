# data types
# numbers - int, float, complex
# Text - str
# seqence types - list, tuple, range
# mapping types - dict
# set types - set
# boolean types - bool

# ; - used to seperate statements on single line
# '' or "" can be used to define a string

num = 10
print("type(num)=",type(num))
print("num = ", num)

character = 'A'
print("type(character) =",type(character))
print("character = ", character)

str = "sunbeam"
print("type(str)= ",type(str))
print("string = ", string)

pi = 3.412
print("type(pi) = ", type(pi))
print("pi = ", pi)

status = True
print("type(status) = ", type(status))
print("state = ", state)

# F-string / format string
#   string prefixed with f      eg f""
#   format string will contail multiple place holders {}
#   all place holders will be replaced by variable values/expression result

print(f"num = {num}")
print(f"character = {character}")
print(f"pi = {pi}")
print(f"string = {string}")
print(f"state = {state}")

print(f"10 + 20 = {10 + 20}")
print(f"num + 100 = {num + 100}")

new_string = f"{string} infotech"
print(f"new_string = {new_string}")

