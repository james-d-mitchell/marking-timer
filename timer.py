#!/usr/bin/env python
"""
"""

import statistics
import time


def time_string(val):
    return "%dm%ds" % (int(val) / 60, int(val % 60))


last_time = time.time()
times = []

while True:
    input()
    now = time.time()
    elapsed = now - last_time
    last_time = now
    times.append(elapsed)
    print(
        "last script marked in %s, mean %s, count %d, total %s"
        % (
            time_string(elapsed),
            time_string(statistics.mean(times)),
            len(times),
            time_string(sum(times))
        )
    )
