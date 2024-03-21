print(dir())
# output : ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__'...]
# Without arguments, return the list of names in the current local scope.


def my_function():
    x, y = 5, 4
    print(f"this is a local scope and it contains {dir()}")


my_function()

print(dir(__builtins__))
# output : ['ArithmeticError', 'AssertionError', 'AttributeError', ... ,'tuple', 'type', 'vars', 'zip']
# With an argument, attempt to return a list of valid attributes for that object.

# when we import a module, define a function or create a class- our global scope is going to include them
import turtle
print(dir())
# output : [..., 'my_function', 'turtle']

help(turtle)
# we can access docs for a module by right clicking its name while pressing ctrl
# or we can get information about module with using help() function
