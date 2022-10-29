#!/usr/bin/env python3
"""
A simple script for timing exam marking per script.
"""

import statistics
import time
from datetime import datetime


def time_string(val):
    val = int(val)
    h = int(val / 60 / 60)
    m = int((val / 60) - (h * 60))
    s = int(val - (m * 60))
    return (str(h)+"h" if h else "") + (str(m)+"m" if m else "") + str(s)+"s"


def pause_until_resumed():
    now = datetime.now()
    input(
        now.strftime("%H:%M:%S")
        + ": PAUSED. Press return to start the next script."
    )


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
                "\033[1m ===> Removing the last submitted time of %s\033[0m"
                % time_string(times.pop()),
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
        print(
            "\n\033[1m ===> You marked %d scripts in %s, with %d pause%s, mean %s, max %s, min %s !!\n🌈 🦄 🌈\033[0m"
            % (
                len(times),
                time_string(sum(times)),
                number_of_pauses,
                "s" if number_of_pauses > 1 else "",
                time_string(statistics.mean(times)),
                time_string(max(times)),
                time_string(min(times)),
            )
        )
