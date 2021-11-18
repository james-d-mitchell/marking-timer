#!/usr/bin/env python3
"""
A simple script for timing exam marking per script.
"""

import statistics
import time


def time_string(val):
    return "%dm%ds" % (int(val) / 60, int(val % 60))


last_time = time.time()
times = []
try:
    while True:
        input(
            "Press return when you've marked the next script or ctrl-c to stop!"
        )
        now = time.time()
        elapsed = now - last_time
        last_time = now
        times.append(elapsed)
        print(
            "\033[1m ===> number %d marked in %s, mean %s, max %s, min %s, total %s\033[0m"
            % (
                len(times),
                time_string(elapsed),
                time_string(statistics.mean(times)),
                time_string(max(times)),
                time_string(min(times)),
                time_string(sum(times)),
            )
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
