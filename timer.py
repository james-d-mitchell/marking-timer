#!/usr/bin/env python3
"""
A simple script for timing exam marking per script.
"""

import statistics
import time


def time_string(val):
    return "%dm%ds" % (int(val) / 60, int(val % 60))


def pause_until_resumed():
    input("PAUSED. Press return to start the next script.")


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


times = []
try:
    extra_time = 0
    while True:
        last_time = time.time()
        from_user = input(
            "Press return when you've marked the next script or ctrl-c to stop!  Enter p to pause: "
        )
        if from_user in ["p", "P"]:
            extra_time = time.time() - last_time
            pause_until_resumed()
            continue
        now = time.time()
        elapsed = now - last_time + extra_time
        extra_time = 0
        times.append(elapsed)
        print(
            "\033[1m ===> number %d marked in %s, mean %s, total %s\033[0m"
            % (
                len(times),
                time_string(elapsed),
                time_string(statistics.mean(times)),
                time_string(sum(times)),
            )
        )
        print(
            "\033[1m ===> quartiles |%s-[%s-%s-%s]-%s|\033[0m"
            % tuple(map(time_string, quartiles(times)))
        )


except KeyboardInterrupt:
    if len(times) != 0:
        print(
            "\n\033[1m ===> You marked %d scripts in %s, mean %s, max %s, min %s !!\n🌈 🦄 🌈\033[0m"
            % (
                len(times),
                time_string(sum(times)),
                time_string(statistics.mean(times)),
                time_string(max(times)),
                time_string(min(times)),
            )
        )
