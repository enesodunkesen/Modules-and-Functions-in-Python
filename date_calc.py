# there are actually several pitfalls which just a really they're waiting to trap the unwary
# now there is two main sources of problems with dates and times first is localization and second is daylight saving
# and they can really complicates things if you don't handle them correctly or not handled correctly

import time
# Python standard library provides three modules to help us deal with dates and times and that's the' \
# `time`, `date time` and `calendar` modules

print(time.gmtime(0))
# gmtime() method is used to convert a specified time expressed in seconds since the
# epoch (January 1, 1970, 00:00:00 UTC) into a time tuple representing Coordinated Universal Time (UTC).
# The returned named tuple represents the time broken down into its components:
# year, month, day, hour, minute,second, day of the week, day of the year, and whether daylight saving time is in effect

print(time.localtime())
# localtime() method is used to convert a specified time expressed in seconds since the epoch.
# just like in gmtime() returned time is a named tuple and it contains same structures

print(time.time())
# time() method returns the current system time in seconds since the epoch as a floating-point number.
# This value is commonly referred to as a timestamp and is often used for measuring time intervals,
# calculating the duration of operations, or for other time-related calculations.

now = time.localtime()
print(now[0], now.tm_year)
print(now[1], now.tm_mon)
print(now[2], now.tm_mday)

# A named tuple in Python is a lightweight data structure that behaves like a standard tuple,
# but with the added functionality of allowing access to its elements by name as well as by index.
# It is similar to a regular tuple but provides more readable and self-documenting code by assigning names to each item




