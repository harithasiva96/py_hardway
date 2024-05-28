   # Created a function and put multiple arguments in args as list.
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
  # Passing positional arguments to the function.
print_two("Python", "UNIX")

def print_two_again(arg1, arg2):
  # Its ok to avoid args in line 3, if we pass multiple arguments directly in the function.
    print(f"arg1: {arg1}, arg2: {arg2}")
print_two_again("Python", "UNIX")

def print_one(arg1):
    print(f"arg1: {arg1}")
print_one("Hello!!")

def print_none():
    print("I got nothin'.")
print_none()

def practice(x,y):
    print(f"I am {x}. I am {y}.")
    # Key word arguments.
practice(x="Happy", y="Healthy")
