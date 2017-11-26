#!/usr/bin/env python3.6
from datetime import datetime
from points import Coordinate

start_co = [51.4952103,-0.1460866]
finish_co = [50.8296233,-0.143276]
start_time = "Wed Aug 27 13:08:45 +0000 2008"
finish_time = "Thu Aug 28 14:08:45 +0000 2008"
tweet_co = [51.087290, -0.160528]

def approximate_time(start_co: Coordinate, start_time: str, finish_co: Coordinate, finish_time: str,
                     tweet_co: Coordinate):
    """
    INPUTS
    start_co: coordinates of start location
    finish_co: coordinates of finish location
    start_time: start time in utc string
    finish_time: finish time in utc string
    tweet_co: coordinates of input location

    OUTPUT
    time of location in epoch
    """
    start_time_epoch = datetime.strptime(start_time, "%Y-%m-%dT%H:%M").timestamp()
    finish_time_epoch = datetime.strptime(finish_time, "%Y-%m-%dT%H:%M").timestamp()

    interval_time = (finish_time_epoch - start_time_epoch) / (tweet_co.distance(start_co) / start_co.distance(finish_co))
    return start_time_epoch + interval_time

    # delta = finish_co.distance(tweet_co.y) / tweet_co.distance(start_co.x)
    #
    # result_time_epoch = (finish_time_epoch + start_time_epoch * delta) / (1 + delta)
    # return result_time_epoch

