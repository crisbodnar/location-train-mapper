# GeoRequest - Nearby stations

import json
import urllib.request
from points import Coordinate, coord_in_array
from api import get_stop_trip_uids

data_link = "http://journeyplanner.silverrailtech.com/journeyplannerservice/v2/REST/DataSets/UKNationalRailRT/NearbyTransitStops?ApiKey=1333ECBD-2A86-08A5-7168-D325C905A731&GeoCoordinate=52.21650468937126,-1.415133326455713&MaximumDistanceInMetres=30000&WalkSpeed=&MaximumStopsToReturn=&ReturnPolylineInformation=False&Time=2017-11-25T11:45&TimeBand=60&TransactionId=&format=json"
with urllib.request.urlopen(data_link) as url:
    data = json.loads(url.read().decode())

uids = []
stop_uids = []
stop_paths = data['TransitStopPaths']

for stop_path in stop_paths:
    stop = stop_path['TransitStop']
    stop_uids.append(stop['StopUid'])

for stop_uid in stop_uids:
    uids += get_stop_trip_uids(stop_uid)

uids = set(uids)
print(uids)
route_path = {}

for uid in uids:
    tripDate = "2017-11-25"
    new_url = 'http://journeyplanner.silverrailtech.com/journeyplannerservice/v2/REST/DataSets/UKNationalRailRT/Trip' + \
              '?ApiKey=1333ECBD-2A86-08A5-7168-D325C905A731&format=json&checkRealTime=false&' + \
              'tripDate={}&tripUid={}'.format(tripDate, uid)
    with urllib.request.urlopen(new_url) as url:
        new_data = json.loads(url.read().decode())

    polyline = new_data["Summary"]["Polyline"]
    coordinates = polyline.split(";")
    route_path[uid] = []
    for coordinate_pair in coordinates:
        latitude, longitude = coordinate_pair.split(",")
        route_path[uid].append(Coordinate(float(latitude), float(longitude)))

    our_point = Coordinate(51.5185911, -0.7209129)
    if not coord_in_array(route_path[uid], our_point):
        del route_path[uid]

print('The train service is:')
for key, value in route_path.items():
    print(key)

