
def changecase(n):
    def changecase(func):
        def inner():
            if n == 1:
                return func().upper()
            else:
                return func().lower()
        return inner
    return changecase

@changecase(2)
def msg():
    return "Good Morning !!!"

message = msg()
print(f"message = {message}")