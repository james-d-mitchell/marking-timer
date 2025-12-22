#!/usr/bin/env python3
"""
A simple script for timing exam marking per script.
"""

# TODO include whether the mean is going up or down

import statistics
import time
from datetime import datetime


LAST_MEAN = None


def time_string(val):
    val = int(val)
    h = int(val / 60 / 60)
    m = int((val / 60) - (h * 60))
    s = int(val % 60)
    return (str(h) + "h" if h else "") + (str(m) + "m" if m else "") + str(s) + "s"


def pause_until_resumed():
    now = datetime.now()
    input(now.strftime("%H:%M:%S") + ": PAUSED. Press return to start the next script.")


def quartiles(vals):
    vals = sorted(vals)
    n = len(vals)
    return [
        vals[0],
        vals[round(n / 4)],
        vals[n // 2],
        vals[(3 * n) // 4],
        vals[-1],
    ]


def print_stats(times, elapsed):
    global LAST_MEAN
    mean = statistics.mean(times)
    if LAST_MEAN is not None:
        if mean > LAST_MEAN:
            prefix = "\033[91m"
            pm = "+"
        else:
            prefix = "\033[92m"
            pm = "-"
        mean = f"{prefix}{time_string(mean)} ({pm}{time_string(mean - LAST_MEAN)})\033[0m\033[1m"
    else:
        mean = time_string(mean)
    LAST_MEAN = statistics.mean(times)

    elapsed, total = (time_string(x) for x in (elapsed, sum(times)))
    print(
        f"\033[1m ===> number {len(times)} marked in {elapsed}, mean {mean}, total {total}\033[0m"
    )
    print(
        "\033[1m ===> quartiles |{}-[{}-{}-{}]-{}|\033[0m".format(
            *(time_string(x) for x in quartiles(times))
        )
    )


times = []
number_of_pauses = 0
try:
    extra_time = 0
    while True:
        last_time = time.time()
        now = datetime.now()
        from_user = input(
            now.strftime("%H:%M:%S")
            + ": Press return when you've marked the next script or ctrl-c to stop (p: pause, t: remove last)! "
        )
        if from_user in ["p", "P"]:
            extra_time = time.time() - last_time
            number_of_pauses += 1
            pause_until_resumed()
            continue
        elif from_user in ["t", "T"]:
            print(
                "\033[1m ===> Removing the last submitted time of {time_string(times.pop())\033[0m"
            )
            elapsed = times[-1]
            print_stats(times, elapsed)
            continue
        now = time.time()
        elapsed = now - last_time + extra_time
        extra_time = 0
        times.append(elapsed)
        print_stats(times, elapsed)


except KeyboardInterrupt:
    if len(times) != 0:
        plural = "s" if number_of_pauses > 1 else ""
        print(
            f"\n\033[1m ===> You marked {len(times)} scripts in {time_string(sum(times))}, with {number_of_pauses} pause{plural}, mean {time_string(statistics.mean(times))}, max {time_string(max(times))}, min {time_string(min(times))} !!\n🌈 🦄 🌈\033[0m"
        )
