routes = [[1, [[51.4952103,-0.1460866], [50.8296233,-0.143276]]],
        [2, [[51.5052103,-0.1560866], [50.4396233,-0.113276]]]]
tweet = {"id" : 3, "created_at" : "Wed Aug 27 14:08:45 +0000 2008",
        "text" : "this is a tweet", "coordinates" : [51.087290, -0.160528]}
def get_routeid_by_tweet(routes, tweet):
    """
    INPUTS
    routes: list of routes, route: list (routeid, list of coordinates), coordinate: lat, lon
    tweet: dict of attributes with keys (id, created_at, text, coordinates)

    OUTPUT
    routeid of best guess from the tweet
    """
    
