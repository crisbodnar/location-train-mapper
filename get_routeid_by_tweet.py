def get_routeid_by_tweet(routes, tweet):
    """
    INPUTS
    routes: list of routes, route: list (routeid, list of coordinates), coordinate: lat, lon
    tweet: dict of attributes with keys (id, created_at, text, coordinates)

    OUTPUT
    routeid of best guess from the tweet
    """
