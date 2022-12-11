from math import radians, cos, sin, asin, sqrt
import itertools

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in km between two points in decimal degrees
    """

    # convert to radians
    lon1, lat1, lon2, lat2 = map(radians [lon1, lat1, lon2, lat2])

    # formula

    dlon = lon2 - lon1
    dlat = lat2- lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # radius of earth in km

    return c * r

route = [[42.27743578594554, -71.82775497436525], [42.277435, -71.827743], 
        [42.27661, -71.827838], [42.276473, -71.827912], 
        [42.276319, -71.828084], [42.276207, -71.828304], 
        [42.275815, -71.828081], [42.275924, -71.827641], 
        [42.276004, -71.827391], [42.276038643072916, -71.82741165161134]]

for i in route:
    i[0], i[1] = i[1], i[0]

routeddiffs = []

test = [x - y for x, y in itertools.izip(route[1:], route)]


for x, y in route:
    difference = haversine(x[1], x[0], y[1], y[0])
    routeddiffs.extend(difference)