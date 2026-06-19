def toupper(func):

    def inner():
        return func().upper()
    
    return inner

@toupper
def msg():
    return "Good Morning !!!"

message = msg()
print(f"messagge = {message}")