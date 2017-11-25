# GeoRequest - Nearby stations

import json
import urllib.request
from points import Coordinate, coord_in_array

data_link = "http://journeyplanner.silverrailtech.com/journeyplannerservice/v2/REST/DataSets/UKNationalRailRT/StopTimetable?ApiKey=1333ECBD-2A86-08A5-7168-D325C905A731&Stop=PAD&TripFilter=Departing&Time=2017-11-25T05:15&TimeBand=100&MaxTripCount=20&CheckRealTime=True&ReturnNotes=False&format=json"
with urllib.request.urlopen(data_link) as url:
    data = json.loads(url.read().decode())

uids = []
trips = path["Trips"]
for trip in trips:
    summary = trip['Summary']
    uids.append(summary['TripUid'])

uids = set(uids)
route_path = {}

for uid in uids:
	tripDate = "2017-11-25"
	new_url = 'http://journeyplanner.silverrailtech.com/journeyplannerservice/v2/REST/DataSets/UKNationalRailRT/Trip?ApiKey=1333ECBD-2A86-08A5-7168-D325C905A731&checkRealTime=true&format=json&tripDate={}&tripUid={}'.format(tripDate, uid)
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

for key, value in route_path.items():
	print(key)

