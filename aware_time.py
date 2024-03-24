# it's fairly easy to convert UTC to any local time using the pytz but going the other way does present a problem
# so that's converting local time back to UTC(in the UK for example the clocks went back one hour at 2.00 on sunday 25th
# of october so if you have a local time of 1.30 on that day and there's no way to tell
# if that was 1.30 that happened before the clocks changed or afterwards of course I'm talking daylight saving time)

# safest way to deal with local times is to immediately convert them to UTC when you get them in working UTC
# only converting the back to local time when you display them to the users of your program
# everything else they are all other times it's actually UTC that really gets rid all lot of the problem

# in the first date time example all three of the times we printed out were naive that was there's no time zone
# information associated with them all we got was the local time or the UTC times now pytz is there to help us
# it provides a localized function that can be used to convert naive local datetime into an aware date time

import datetime
import pytz

naive_local = datetime.datetime.now()
naive_utc = datetime.datetime.utcnow()

print("naive local time = {}".format(naive_local))
print("naive utc time = {}".format(naive_utc))

print("-"*60)

aware_local = pytz.utc.localize(naive_local)
aware_utc = pytz.utc.localize(naive_utc)

print("aware local time = {} {}".format(aware_local, aware_local.tzname()))
print("aware utc time = {} {}".format(aware_utc, aware_utc.tzname()))

# both of the where times are showing their time zones as UTC which isn't really what we want at all
# pytz documentation states localize() method is used to localize a naive date time(date time without timezone information)

# if the original date time hasn't got time zone information itself then pytz is going to have a hard time
# working out what it should be at all so all it can really do is provide an offset and set the time zone to UTC
# fortunately the standard pytz module provides an astimezone() method this converts and aware time to use the specified
# time zone or the local time zone if none is given that is key there so the correct way to deal with this is to take
# the advice given above : always work in UTC and only convert to local time when you're displaying that time on the screen to the user

time = datetime.datetime.utcnow()
aware_time = pytz.utc.localize(time).astimezone()

print(time)
print(aware_time, aware_time.tzname())

# it actually contains the time zone but then we use the as timezone method to convert it to a time zone
# we actually want and defaulting at this stage for the computer local time because:
# we didn't provide a  tz info in the brackets there's as a parameter