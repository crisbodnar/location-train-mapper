# GeoRequest - Nearby stations

import json
import urllib.request
from points import Coordinate, coord_in_array
from api import get_near_trip_uids
from approximate_time import approximate_time
from datetime import datetime
import math


latitude = 52.294031
longitude = -1.630698
uids = get_near_trip_uids(latitude, longitude, 30000, '2017-11-26', '10:40', 60)

route_path = {}

our_point = Coordinate(52.2865397, -1.5818545)
tweet_time = '2017-11-26T12:34'
tweet_time_epoch = datetime.strptime(tweet_time, "%Y-%m-%dT%H:%M").timestamp()
time_err = 600000

# Get the uids of the routes which have a point we are very near to
for uid in uids:
    new_url = 'http://journeyplanner.silverrailtech.com/journeyplannerservice/v2/REST/DataSets/UKNationalRailRT/Trip' + \
              '?ApiKey=1333ECBD-2A86-08A5-7168-D325C905A731&format=json&checkRealTime=false&' + \
              'tripDate={}&tripUid={}'.format(tweet_time, uid)
    with urllib.request.urlopen(new_url) as url:
        new_data = json.loads(url.read().decode())

    polyline = new_data["Summary"]["Polyline"]
    coordinates = polyline.split(";")
    route_path[uid] = []
    for coordinate_pair in coordinates:
        latitude, longitude = coordinate_pair.split(",")
        route_path[uid].append(Coordinate(float(latitude), float(longitude)))

    if not coord_in_array(route_path[uid], our_point):
        del route_path[uid]

# Go through all routes and calculate the expected time at our point
for uid in uids:
    new_url = 'http://journeyplanner.silverrailtech.com/journeyplannerservice/v2/REST/DataSets/UKNationalRailRT/Trip' + \
              '?ApiKey=1333ECBD-2A86-08A5-7168-D325C905A731&format=json&checkRealTime=false&' + \
              'tripDate={}&tripUid={}'.format(tweet_time, uid)
    with urllib.request.urlopen(new_url) as url:
        data = json.loads(url.read().decode())

    # Get start and arrival time
    trip_start_time = data['Summary']['TripStartTime']
    stops = data['TripStops']
    last_stop = stops[len(stops) - 1]
    arrival_time = last_stop['ArrivalTime']

    # Get start and dest locations
    start_pos = stops[0]['TransitStop']['Position']
    lat, long = start_pos.split(',')
    start_pos_cord = Coordinate(float(lat), float(long))
    dest_pos = stops[len(stops) - 1]['TransitStop']['Position']
    lat, long = dest_pos.split(',')
    dest_pos_cord = Coordinate(float(lat), float(long))

    epoch_time = approximate_time(start_pos_cord, trip_start_time, dest_pos_cord, arrival_time, our_point)
    if math.fabs(epoch_time - tweet_time_epoch) < time_err:
        print('The train service is:')
        print(uid)
        exit()


# for key, value in route_path.items():
#     print(key)

