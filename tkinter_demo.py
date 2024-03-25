try:
    import tkinter
except ImportError:
    import Tkinter  #python 2

# Python provides access to the TKwidget tool kit what that means is that it allows gui programs to be created
# TK toolkit was developed to work with scripting language called TCL and the tkinter Python binding works by actively
# sending TCL code to a TCL interpreter but that's actually embedded in the Python interpreters so no need to load
# anything extra there are other graphic libraries available but tkinter has the advantage that it's part
#  of the standard Python  language and has a disadvantage in that the documentation isn't brilliant

print(tkinter.TkVersion)
print(tkinter.TclVersion)

main_window = tkinter.Tk()
# we should create a Tk object with Tk() method then we should call mainloop() method from this object to open it
main_window.title("hello world!")
# title() method sets the title of our window
main_window.geometry("640x480")
# geometry method expect a string containing four components. we got 2 in it at the moment, we got the width the height
# but we can also specify the left and the top offsets from the edge of the screen the width and height are separated by x
# as you saw and really look like the normal way of expressing screen resolution you normally talk in these terms
# 640 by 480 but the 2 offset are separate from the size by each other by using either plus or minus
main_window.geometry("640x480+8+300")


# the applications widgets can be placed on that window using one of three different geometry managers
# pack manager most commonly used and the reason for that is the first and probably the easiest to become familiar with
# one thing to note here is that everything in tk is a window and objects are placed in a hierarchy
# in our example on the screen main window is the root window so everything else must be placed within it or within
# one of the child windows not every window can have children but every window (except the root one)
# must have a master window to see the effects of positioning widgets

root = main_window
label = tkinter.Label(root, text="hello world")
label.pack(side="top")
# we have created a label application widget and placed it with using pack manager

canvas = tkinter.Canvas(root, relief="raised", borderwidth=1)
canvas.pack(side="left")
# with using fill= kwarg we can resize our application widget to fill a side or both
# but keep that in mind using tkinter.X and left or right sides will result application widget to not fill side
# it's also valid for tkinter.Y and top or bottom sides to prevent this we should also use expand= kwarg with True

button1 = tkinter.Button(root, text="button1")
button2 = tkinter.Button(root, text="button2")
button3 = tkinter.Button(root, text="button3")

button1.pack(side="top", anchor="s")
button2.pack(side="top", anchor="w")
button3.pack(side="top", anchor="e")
# when widgets share the same side they are placed adjacent to each other in the order that they're packed
# to change order we can use before=/after= kwargs to place application widget before/after another
# in this case the buttons are actually centered against the canvas which is to left of it and is not always preferable
# want so we can change this by setting the anchor kwarg which takes values corresponding to the
# four main points of the compass(s,w,n,e) for the center which is the default

# widgets packed with vertical edge that's left or right can only have a vertical position altered by anchor the ones
# packed horizontal edge top and bottom can only have their horizontal positions change although we can place widgets
# inside a frame to both group them together and position them a little bit better, pack is really only suitable for
# very simple layouts so of the 3 geometry managers that are part of Python part of Tkinter pack is really the
# most basic pf the 3 and the options are still a little bit limited as a result
main_window.mainloop()
