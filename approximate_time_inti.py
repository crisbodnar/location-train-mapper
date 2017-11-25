#!/usr/bin/env python3.6
from math import sin, cos, sqrt, atan2, radians
import csv
import sys

start_co = [51.4952103,-0.1460866]
end_co = [50.8296233,-0.143276]
start_time = ["16:57"]
finish_time = ["15:57"]
input_co = [51.087290, -0.160528]

tweet_time_format = "Thu Nov 16 16:25:18 +0000 2017"
av_speed = 201.000
# av_speed = 201 km/h

def approximate_time(start_co, start_time, finish_co, finish_time, input_co):
    
    """

    INPUTS
    start: coordinates of start
    finish: coordinates of finish

    OUTPUT
    coordinates | INPUTS

    """

    start_co[0] = lat1
    start_co[1] = lon1
    finish_co[0] = lat2
    finish_co[1] = lon2

    def process_total_travel_time(start_time, finish_time):
    	#reformat "15:57" -> 15:57:00
    	start_time += ":00"
    	finish_time += ":00"

    	start_time_cum = (start_time.split(":")[0] * 60) + (start_time.split(":")[1] * 60)
    	finish_time_cum = (finish_time.split(":")[0] * 60) + (finish_time.split(":")[1] * 60)

    	return finish_time_cum - start_time_cum

	def calc_distance(lon1, lat1, lon2, lat2):
		# approximate radius of earth in km
		R = 6373.0
		lat1 = radians(lat1)
		lon1 = radians(lon1)

		lat2 = radians(lat2)
		lon2 = radians(lon2)

		dlon = lon2 - lon1
		dlat = lat2 - lat1

		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
		c = 2 * atan2(sqrt(a), sqrt(1 - a))

		distance = R * c

		print("Result:", distance)
		#print("Should be:", 278.546, "km")
		return distance

	distance = calc_distance(lon1, lat1, lon2, lat2)
	av_speed = 201.000
	time_travelled = distance / av_speed
	start_time_cum = (start_time.split(":")[0] * 60) + (start_time.split(":")[1] * 60)
	final_time = start_time_cum + time_travelled

	#convert to final format

	return final_time










