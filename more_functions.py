def sum_undefined(x,y):
    return x+y
# if we don't specify the return value a function is going to return None, however we can specify the return value


def sum_defined(x: int, y: int) -> int:
    return x+y
# also we can specify the type of the parameters and return value
# note that in this scenario our function is not going to raise any errors even if we call it with strings
# print(sum_defined("1","2"))

import tkinter


def parabola(x):
    return x*x/100


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width()/2
    y_origin = page.winfo_height()/2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")


def plot(page, x, y):
    page.create_line(x, y, x+1, y+1, fill="red")


def plot_parabola(canvas, x):
    for i in range(-x,x):
        plot(canvas, i, -parabola(i))
    # Parameter names and variable names can be the same in Python without causing any issues; however,
    # it's generally recommended to use different names for clarity and to avoid confusion. besides it creates shadowing
    # Shadowing: If you use the same name for a parameter and a variable within the function, you're essentially
    # shadowing the outer variable with the parameter. While Python allows this, it can lead to confusion,
    # especially if you intend to use the outer variable but forget that it's being shadowed by the parameter.
    # canvas parameter here shadowed by canvas object in code down below


root = tkinter.Tk()
root.title = "Parabola"
root.geometry("640x480")

canvas = tkinter.Canvas(root, width=640, height=480)
canvas.grid(row=0, column=0)
draw_axes(canvas)
plot_parabola(canvas, 100)

# plot(page, x, parabola(x)) will give an error since page defined within a function and has local scope
# so another thing to mention here is : In programming, the term "scope" refers to the region of code where a particular
# variable, function, or other identifier is accessible or visible.
# The scope defines the visibility and lifetime of  variables and other identifiers within a program.

# there are 4 types of functions in python but 2 of them is important

# Global Scope: Variables defined outside of any function or class have global scope. They can be accessed from
# anywhere in the program, including within functions and classes.

# Local Scope: Variables defined within a function have local scope. They can only be accessed within the function
# in which they are defined.

# so we can access a global scope in local function but we can only access a local scope within function
# unless there is a shadowing

# In python defining a module(global scope), class(global scope), function(local scope) changes the scope, to display
# a scope we can use locals() function

print(*locals(), sep="\n")
# this is going to print our global scope

root.mainloop()