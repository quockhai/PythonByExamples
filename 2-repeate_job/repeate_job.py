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