# if we are dealing with dates rather than just times,we want to actually do just we are going to use the
# date time module even if time does include dates

import datetime

print(datetime.datetime.utcnow())
print(datetime.datetime.now())
print(datetime.datetime.today())

# datetime.today() and the datetime.now() methods appeared to do the same thing because they returned the same date
# and the same time other than the milliseconds in the end but the now method can be more precise and more importantly
# now allows us to specify a timezone by providing a datetime.tzinfo object

# datetime.tzinfo abstract base class for timezone information systems which means by absract class is
# datetime.tzinfo object cannot be created. Python datetime has the ability to cope with aware dates
# but the actual method required to do so is only defined by the language and not implemented so part of the rationale
# for this seems to be that the local time can actually mean different things to different people
# and as a result it's best left to the developer to implement datetime.tzinfo in a way that is meaningful to them

import pytz

# pytz is a library that eals with the complexity of time zones and daylight saving time and it's not part of the standart
# library that comes with Python but it's generally speakingconsidered to be the best approach to dealing with time zones

country = "Europe/Berlin"

tz_to_display = pytz.timezone(country)
# pytz.timezone() returns a datetime.tzinfo object for the given timezone

local_time = datetime.datetime.now(tz=tz_to_display)
print("Time in {} is {}".format(country.split("/")[1], local_time))
# with that object and datetime.now method we can display time info for any chosen country
# but the required string is difficult to sort if you wanted to provide the entire list to a user
# so is moscow really in Europe and will most people really know to look there what we can do is we can print the
# entire list of valid strings that the pytz.timezone method accepts quite easily


# for country, country_name in pytz.country_names.items():
#     print("{} : {}".format(country, country_name))

# countries isn't actually good enough for getting the timezone and that's because many countries
# have got more than one timezone and so it is possible to retrieve a list of all
# the time zones for a country code and display them after the country name
# so we might be tempted to just use the same key then pytz.time_zones dictionary


for country, country_name in pytz.country_names.items():
    try:
        print(country_name)
        for timezone in pytz.country_timezones[country]:
            tz_to_display = pytz.timezone(timezone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\tTime in {} is {}".format(timezone.split("/")[1], local_time))

    except KeyError:
        print("{} : {} : time zone is not defined".format(country, country_name))

# for some countries time zone is not defined so we must do some error handling

# timezone data itself comes from a data base that's maintained by IANA in which is the internet assigned names authority
# it's often referred to as the Olsen database timezone and Daylight Saving Time changes and is pretty much considered the
# definitive source of information on these now it is kept up-to-date and used toupdate the time zone information on most computers
