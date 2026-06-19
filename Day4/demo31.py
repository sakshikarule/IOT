def function1(print_msg):
    print("adding extra functinality")
    print_msg()

def decorator(print_msg):
    def inner():
        print("adding extra functionality")

    return inner

@decorator
def print_msg():
    print("Good Morning !!!")

print_msg = decorator(print_msg)

print_msg()

function1(print_msg)