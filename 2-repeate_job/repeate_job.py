#!/usr/bin/env python3

import schedule
import time


def job(t):
    print("I'm working ...", t)
    return


schedule.every().day.at("15:10").do(job, 'It it 15:10')

while True:
    schedule.run_pending()
    time.sleep(60)


# # Task scheduling
# # After every 10mins geeks() is called.
# schedule.every(10).minutes.do(geeks)

# # After every hour geeks() is called.
# schedule.every().hour.do(geeks)

# # Every day at 12am or 00:00 time bedtime() is called.
# schedule.every().day.at("00:00").do(bedtime)

# # After every 5 to 10mins in between run work()
# schedule.every(5).to(10).minutes.do(work)

# # Every monday good_luck() is called
# schedule.every().monday.do(good_luck)

# # Every tuesday at 18:00 sudo_placement() is called
# schedule.every().tuesday.at("18:00").do(sudo_placement)

# # Loop so that the scheduling task
# # keeps on running all time.
# while True:
#     # Checks whether a scheduled task
#     # is pending to run or not
#     schedule.run_pending()
#     time.sleep(1)
