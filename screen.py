import tkinter
import os
root = tkinter.Tk()

root.title = "screen"
root.geometry("640x480-8-200")

label = tkinter.Label(root, text="Tkinter grid demo")
label.grid(row=0, column=0, columnspan=3)
#
# configure columns
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=3)
root.columnconfigure(3, weight=3)
root.columnconfigure(4, weight=3)

# configure rows
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=10)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=3)
root.rowconfigure(4, weight=3)

file_list = tkinter.Listbox(root, relief="sunken", borderwidth=2)
file_list.grid(row=1, column=0, rowspan=2, sticky="news")

for zone in os.listdir("\\Windows\\System32"):
    file_list.insert(tkinter.END, zone)
    # list-boxes got insert method with that method we can add elements to them.
    # note that index is tkinter.END, so we are actually appending elements(in this case zones)

list_scroll = tkinter.Scrollbar(root, orient="vertical", command=file_list.yview)
list_scroll.grid(row=1, column=1, rowspan=2, sticky="nsw")
file_list["yscrollcommand"] = list_scroll.set

# frame for the radio buttons
option_frame = tkinter.LabelFrame(root, text="File Details")
option_frame.grid(row=1, column=2, sticky="ne")

# radio buttons
rbvalue = tkinter.IntVar()
rbvalue.set(1)
# in order to create 3 radio buttons that all share the same variable in Python relies on the Tkinter control variables
# that can be bound to one or more widgets. tkinter.IntVar is that variable.
# the reason we are doing this is only one can be selected any one time so as you click on each one the one that
# was previously selected is automatically un-selected now the mechanism to do this

rb1 = tkinter.Radiobutton(option_frame, text="Filename", value=1, variable=rbvalue)
rb2 = tkinter.Radiobutton(option_frame, text="Path", value=2, variable=rbvalue)
rb3 = tkinter.Radiobutton(option_frame, text="Timestamp", value=3, variable=rbvalue)
# now radio buttons share the same variable

rb1.grid(row=0, column=0, sticky="w")
rb2.grid(row=1, column=0, sticky="w")
rb3.grid(row=2, column=0, sticky="w")

# widget to display the result
result_label = tkinter.Label(root, text="Result")
result_label.grid(row=2, column=2, sticky="nw")
result = tkinter.Entry(root)
result.grid(row=2, column=2, columnspan=2, sticky="sw")

# frame for the  time spinners
time_frame = tkinter.LabelFrame(root, text="Time")
time_frame.grid(row=3, column=0, sticky="new")

# time spinners
hour_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=23, increment=1)
minute_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59, increment=1)
seconds_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59, increment=1)

hour_spinner.grid(row=0, column=0)
tkinter.Label(time_frame, text=":").grid(row=0, column=1)
minute_spinner.grid(row=0, column=2)
tkinter.Label(time_frame, text=":").grid(row=0, column=3)
seconds_spinner.grid(row=0, column=4)

time_frame["padx"] = 36

# frame for date spinners
date_frame = tkinter.Frame(root)
date_frame.grid(row=4, column=0, sticky="new")

# labels for spinners
dayLabel = tkinter.Label(date_frame, text="Day")
monthLabel = tkinter.Label(date_frame, text="Month")
yearLabel = tkinter.Label(date_frame, text="Year")
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

# date spinners
day_spinner = tkinter.Spinbox(date_frame, width=5, from_=1, to=31, increment=1)
month_spinner = tkinter.Spinbox(date_frame, width=5, values=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                                             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
year_spinner = tkinter.Spinbox(date_frame, width=5, from_=2000, to=2099, increment=1)

day_spinner.grid(row=1, column=0, sticky='w')
month_spinner.grid(row=1, column=1, sticky='w')
year_spinner.grid(row=1, column=2, sticky='w')

# Buttons
okButton = tkinter.Button(root, text="OK")
cancelButton = tkinter.Button(root, text="Cancel", command=root.quit)
# note that when we use parentheses after the method name(root.quit) were actually calling the method
# and the result of the method assigned to the command property. the quit method returns none so the result
# is clicking the cancel button does nothing because root mainly hasn't been started at a point when quit is executed
# the loop is not terminated so the incorrect assignment doesn't cause problems, but it also doesn't work either

okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

root.mainloop()
