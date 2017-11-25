# GeoRequest - Nearby stations

import json
import urllib.request

data_link = "http://journeyplanner.silverrailtech.com/journeyplannerservice/v2/REST/DataSets/UKNationalRailRT/NearbyTransitStops?ApiKey=1333ECBD-2A86-08A5-7168-D325C905A731&GeoCoordinate=52.21650468937126%2C-1.415133326455713&MaximumDistanceInMetres=30000&WalkSpeed=&MaximumStopsToReturn=&ReturnPolylineInformation=False&Time=2017-11-25T11%3A45&TimeBand=60&FilterInactiveStops=True&TransactionId=&format=json"
with urllib.request.urlopen(data_link) as url:
	data = json.loads(url.read().decode())

transit_stop_paths = data["TransitStopPaths"]
routes = []

for path in transit_stop_paths:
	stop = path["TransitStop"]
	routes += stop["Routes"].split(";")
	
routes_array = set(routes)
