from approximate_time import approximate_time
from datetime import datetime
routes = [[1, [[51.4952103,-0.1460866], [50.8296233,-0.143276]],
            ["Wed Aug 27 13:08:45 +0000 2008", "Wed Aug 27 14:08:45 +0000 2008"]],
        [2, [[51.5052103,-0.1560866], [50.4396233,-0.113276]],
            ["Wed Aug 27 16:08:45 +0000 2008", "Thu Aug 28 17:08:45 +0000 2008"]],
        [3, [[53.5052103,-0.1560866], [49.4396233,-0.113276]],
            ["Wed Aug 27 16:08:45 +0000 2008", "Wed Aug 27 17:08:45 +0000 2008"]]]
tweet = {"id" : 3, "created_at" : "Wed Aug 27 14:08:45 +0000 2008",
        "text" : "this is a tweet", "coordinates" : [51.017290, -0.160528]}
def get_routeid_by_tweet(routes, tweet):
    """
    INPUTS
    routes: list of routes, route: list (routeid, list of coordinates), coordinate: lat, lon
    tweet: dict of attributes with keys (id, created_at, text, coordinates)

    OUTPUT
    routeid of best guess from the tweet
    """
    route_times = []
    tweet_time_epoch = datetime.strptime(tweet["created_at"], "%a %b %d %H:%M:%S %z %Y").timestamp()
    for route in routes:
        route_times.append([route[0], abs(approximate_time(route[1][0], route[2][0], route[1][1], route[2][1],
                tweet["coordinates"]) - tweet_time_epoch)])
    return sorted(route_times, key = lambda x: x[1])


if __name__ == "__main__":
    print (get_routeid_by_tweet(routes, tweet))
