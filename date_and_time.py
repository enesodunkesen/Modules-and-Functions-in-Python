import time
# We can get information on the current time zone via time.timezone and time.tzname (these aren't functions)
# time.timezone is an int and time.tzname is a tuple containing two strings :
# time.tzname[0] is the name of the non-DST timezone and time.tzname[1] is the name of the DST timezone
# before relying on the DST timezone name we need to check the value of time.daylight if this is non-zero
# then a DST timezone is defined and you can trust that at that point the second string
# in the time.tzname tuple otherwise you shouldn't use the second string

print("The epoch on this system starts at : {}".format(time.strftime("%c", time.gmtime(0))))
# strftime() is a method used to format a time struct (t) into a string according to the format specified

print("Current timezone is {} with an offset of {}".format(time.tzname[0], time.timezone))
# timezone returns a number of seconds offset from UTC so in other words :
# it will be negative for the country's east of the Greenwich Meridian and most of Western Europe (in Tr it is -10800)
# it will be positive for the country's west of Greenwich Meridian (in the UK it is 0)
# ("offset" typically refers to the displacement or difference between a reference point and another point,
# usually used to locate or access data within a data structure like an array or a file)

if time.daylight:
    print("\tDaylight for this location is in effect")
    print("\tDST timezone is {}".format(time.tzname[1]))
# timezone uses the non-DST when calculating the offset
# which means that you also have to check to see if daylight savings in effect and if it is, apply that correction also

print("Local time is : {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
print("UTC time is : {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())))
