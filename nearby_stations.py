# GeoRequest - Nearby stations

import json
import urllib.request
from points import Coordinate, coord_in_array
from api import get_near_trip_uids


latitude = 52.21650468937126
longitude = -1.415133326455713
uids = get_near_trip_uids(latitude, longitude, 30000, '2017-11-25', '11:45', 60)

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

    our_point = Coordinate(52.2865397, -1.5818545)
    if not coord_in_array(route_path[uid], our_point):
        del route_path[uid]

print('The train service is:')
for key, value in route_path.items():
    print(key)

