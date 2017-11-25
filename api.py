import json
import urllib.request


def get_stop_trip_uids(stop_uid: str) -> [str]:
    req_url = 'http://journeyplanner.silverrailtech.com/journeyplannerservice/v2/REST/DataSets/UKNationalRailRT/StopTimetable?ApiKey=1333ECBD-2A86-08A5-7168-D325C905A731&StopUid={}&TripFilter=Departing&Time=2017-11-25T05:15&TimeBand=100&MaxTripCount=20&CheckRealTime=True&ReturnNotes=False&format=json'.format(stop_uid)

    with urllib.request.urlopen(req_url) as url:
        data = json.loads(url.read().decode())

    uids = []
    trips = data["Trips"]
    for trip in trips:
        summary = trip['Summary']
        uids.append(summary['TripUid'])

    return uids
