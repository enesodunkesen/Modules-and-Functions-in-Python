def python_food():
    text = "spam and eggs"
    left_margin = 80-len(text)//2
    print(" "*left_margin, text)


python_food()  # output: spam and eggs
# Python functions return a result that's important so if you don't tell the function what result to return
# then function is going to return None automatically

print(python_food())  # output: spam and eggs`\n`None
# by adding a parameter and instead of printing the hard coded it on python_food
# we can print the parameter that was passed to this function


def centre_text(text):
    text = str(text)
    left_margin = 80-len(text)//2
    print(" "*left_margin, text)


centre_text("spam and eggs")
centre_text("spam and spam and eggs")
centre_text("spam and spam and spam and spam")

# text is called parameter it needs a single argument between the parenthesis, but we can define functions with
# multiple parameters to add more functionality to our function


def centre_texts(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    left_margin = 80-len(text)//2
    print(" "*left_margin, text)
# parameters are called positional args and the fact that it's a plural rather than arg gives an indication of what the
# asterix(*) means so if our parameter is prefixed with a stab then asterix, and it represents a variable
# number of arguments and what that really means is you can pass as many as you want



centre_texts("first", "second", 3, 4, "spam")
# Positional arguments allow a function to accept an arbitrary number of arguments without explicitly naming them.
# The *args parameter in a function definition collects any number of positional arguments into a tuple.
# These arguments are accessed by their position in the function call.


def centre_texts_seperator(*args, sep=" | "):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = 80-len(text)//2
    print(" "*left_margin, text)


# default values are values assigned to function parameters in the function definition. When a parameter has a
# default value, it means that the function can be called without providing an argument for that parameter.
# If an argument is not provided for a parameter with a default value, the default value is used.

centre_texts_seperator("first", "second", 3, 4, "spam")
centre_texts_seperator("first", "second", 3, 4, "spam", sep=" : ")
# Keyword arguments allow you to specify arguments by parameter name when calling a function. This means
# you can provide arguments to a function in any order, as long as you specify the parameter names. Keyword arguments
# are particularly useful when a function has many parameters or when you want to make your code more readable.

# Combining default values with keyword arguments allows for even more flexibility in function calls, as you can choose
# which parameters to customize while leaving others to their default values.


def centre_texts_final(*args, **kwargs):
    text = ""
    i = 0
    while i < (len(args)-1):
        text += str(args[i]) + kwargs["sep"]
        i += 1
    text += str(args[i]) + kwargs["end"]
    left_margin = 80-len(text)//2
    print(" "*left_margin, text)

# Keyword arguments allow passing a variable-length list of keyworded arguments to a function.
# The **kwargs parameter in a function definition collects any number of keyword arguments into a dictionary where
# the keys are the argument names.These arguments are accessed by their keyword.


centre_texts_final("first", "second", 3, 4, "spam", sep=" ~ ", end="@@@")

# one last note : In a function signature,
# the / symbol separates positional-only parameters from parameters that can be specified positionally or by keyword.
# Parameters listed before the / can only be passed positionally, meaning they cannot be specified using kwargs
#
# *: In a function signature, the * symbol indicates the start of keyword-only parameters.
# Parameters listed after the * must be specified using keyword arguments.
