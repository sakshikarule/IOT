# Funcations

#   def function_name():
#       statement(s)

#   def function_name(parameter):
#       statement(s)

#   def function_name(parameter1, parameter2):
#       statement(s)
#       return result

#   actual arguments    - arguments
#   formal arguments    - parameters

def function1():
    print("funcation() is called")

def function2(param):
    print(f"param = {param}")
    print(f"type(param) = {type(param)}")

def function3(param1, param2):
    return param1 + param2

print("program started")

   
# function1()
# function2(10)
# function2('A')
# function2(3.142)
# function2('sunbeam')
     
ret = function3(10,20)
print(f"ret = {ret}")
ret= function(1.5,2.5)
print(f"ret = {ret}")
ret = function3('sun', 'beam')
print(f"ret = {ret}")

ret = function3("sun", 10)

print("program finished")
