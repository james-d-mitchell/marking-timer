#!/usr/bin/env python3
"""
A simple script for timing exam marking per script.
"""

import statistics
import sys
import time


def time_string(val):
    return "%dm%ds" % (int(val) / 60, int(val % 60))


last_time = time.time()
times = []
while True:
    val = input(
        "Press return when you've marked the next script or escape to stop!"
    )
    if val == "\u001B":
        if len(times) != 0:
            print(
                "mean %s, min %s, count %d, total %s"
                % (
                    time_string(statistics.mean(times)),
                    time_string(min(times)),
                    len(times),
                    time_string(sum(times)),
                )
            )
        sys.exit(0)
    now = time.time()
    elapsed = now - last_time
    last_time = now
    times.append(elapsed)
    print(
        "last script marked in %s, mean %s, min %s, count %d, total %s"
        % (
            time_string(elapsed),
            time_string(statistics.mean(times)),
            time_string(min(times)),
            len(times),
            time_string(sum(times)),
        )
    )
