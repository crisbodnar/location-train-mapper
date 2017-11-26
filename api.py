import json
import urllib.request


def get_stop_trip_uids(stop_uid: str, date: str, time: str) -> [str]:
    req_url = 'http://journeyplanner.silverrailtech.com/journeyplannerservice/v2/REST/DataSets/UKNationalRailRT/StopTimetable?ApiKey=1333ECBD-2A86-08A5-7168-D325C905A731&StopUid={}&Time={}T{}&TimeBand=100&MaxTripCount=20&CheckRealTime=True&ReturnNotes=False&format=json'.format(stop_uid, date, time)

    with urllib.request.urlopen(req_url) as url:
        data = json.loads(url.read().decode())

    uids = []
    trips = data["Trips"]
    for trip in trips:
        summary = trip['Summary']
        uids.append(summary['TripUid'])

    return uids


def get_near_trip_uids(latitude: float, longitude: float, radius: int, date: str, time: str, time_band: int) -> [str]:
    data_link = "http://journeyplanner.silverrailtech.com/journeyplannerservice/v2/REST/DataSets/UKNationalRailRT/NearbyTransitStops?ApiKey=1333ECBD-2A86-08A5-7168-D325C905A731&GeoCoordinate={},{}&MaximumDistanceInMetres={}&WalkSpeed=&MaximumStopsToReturn=&ReturnPolylineInformation=False&Time={}T{}&TimeBand={}&TransactionId=&format=json".format(latitude, longitude, radius, date, time, time_band)
    with urllib.request.urlopen(data_link) as url:
        data = json.loads(url.read().decode())

    trip_uids = []
    stop_uids = []
    try:
        stop_paths = data['TransitStopPaths']
    except KeyError:
        print('No train was found. Try increasing the radius')
        return []

    for stop_path in stop_paths:
        stop = stop_path['TransitStop']
        stop_uids.append(stop['StopUid'])

    for stop_uid in stop_uids:
        trip_uids += get_stop_trip_uids(stop_uid, date, time)
    return set(trip_uids)