# place manager is even simpler than pack and it be useful when some specific situations however it works by:
# specifying absolute positions for at least one window, windows that can be position relative to another window
# and unless you know the screen size of your program will be running on the use of absolute positioning
# is not recommended now for more complicated layouts which really means anything but the most trivial layouts you

# get much better results using the grid manager.
# it works by positioning widgets in a grid. the grid doesn't really exist until you start adding things to it
# at which point its dimensions are calculated automatically this the way to go.  just bear in mind that widgets in the
# same column can be lineup above or below each other and also widgets in the same row can also be lined up next to each
# other and approximation to the previous rather hideous example can be quickly created using a grid
import tkinter

root = tkinter.Tk()

root.title("hello world!")
root.geometry("640x480-8-200")

label = tkinter.Label(text="Hello World!")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(root)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief= 'raised', borderwidth=1)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(root)
rightFrame.grid(row=1, column=2, sticky="n")
# in grid methods we can set the sticky= kwarg to position buttons more accurately. that can be used to change
# the position of the widgets within their cells or labels it uses compass points just as we saw with pack and it can
# be used to align the widget left right top or bottom (the default if you don't specify is center)
# so what the sticky property does is it takes the same compass points anchor does when using pack


button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame,text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# configure columns
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
# note that columnconfigure() and grid_columnconfigure are actually the same 


leftFrame.config(relief="sunken", borderwidth=1)
rightFrame.config(relief="sunken", borderwidth=1)
leftFrame.grid(sticky="ns")
rightFrame.grid(sticky="new")
# we can give them a border and change their appearance, so they show up better. we should use sticky in our code
# to expand the left frames so that's the full height of its rows and the right frame to be the full width of its column

# button2.grid(sticky="ew")
# this is where the weight option comes into play so the weight option is quite important in deciding the
# behavior of widgets within cells so unless a weight has been set for a column or row them some options including
# sticky won't do anything else you can see in this example here on line 39 it had no effect on button 2 the right
# frame only has one column so if we set its weight first then button 2 sticky option will work

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky="ew")
root.mainloop()
