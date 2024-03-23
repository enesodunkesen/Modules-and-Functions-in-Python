import time
import random
from time import time as timer

sleep_time = (random.random())*6
input("press enter to start")
time.sleep(sleep_time)
time_before = timer()
input("press enter to stop")
time_after = timer()

print(f"your reaction time was {(time_after-time_before):0.3f} seconds")

# we could have used 3 other clocks instead of time() and they are perf_counter(), monotonic() and process_time()
# check information about these clocks

print("time(): \t\t {}".format(time.get_clock_info("time")))
# monotonic means is not subject to system clock adjustments (such as changes due to time synchronization or
# daylight saving time), making it suitable for measuring intervals in a monotonic fashion.
print("perf_counter(): \t\t {}".format(time.get_clock_info("perf_counter")))
print("monotonic():\t\t {}".format(time.get_clock_info("monotonic")))
print("process_time():\t\t {}".format(time.get_clock_info("process_time")))


