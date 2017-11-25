#!/usr/bin/env python3.6
from datetime import datetime

start_co = [51.4952103,-0.1460866]
finish_co = [50.8296233,-0.143276]
start_time = "Wed Aug 27 13:08:45 +0000 2008"
finish_time = "Wed Aug 27 14:08:45 +0000 2008"
tweet_co = [51.087290, -0.160528]

def approximate_time(start_co, start_time, finish_co, finish_time, tweet_co):
    """
    INPUTS
    start_co: coordinates of start location
    finish_co: coordinates of finish location
    start_time: start time in utc string
    finish_time: finish time in utc string
    tweet_co: coordinates of input location

    OUTPUT
    time of location utc datetime
    """
    start_time_epoch = datetime.strptime(start_time, "%a %b %d %H:%M:%S %z %Y").timestamp()
    finish_time_epoch = datetime.strptime(finish_time, "%a %b %d %H:%M:%S %z %Y").timestamp()

    delta = (finish_co[0] - tweet_co[0]) / (tweet_co[0] - start_co[0])

    result_time_epoch = (finish_time_epoch + start_time_epoch * delta) / (1 + delta)

    return datetime.utcfromtimestamp(result_time_epoch).strftime("%a %b %d %H:%M:%S %z %Y")

print (approximate_time(start_co, start_time, finish_co, finish_time, tweet_co))
