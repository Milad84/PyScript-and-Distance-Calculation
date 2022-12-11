from math import radians, cos, sin, asin, sqrt
import itertools

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

route = [[42.27743578594554, -71.82775497436525], [42.277435, -71.827743], 
        [42.27661, -71.827838], [42.276473, -71.827912], 
        [42.276319, -71.828084], [42.276207, -71.828304], 
        [42.275815, -71.828081], [42.275924, -71.827641], 
        [42.276004, -71.827391], [42.276038643072916, -71.82741165161134]]

routeddiffs = []

for i in range(len(route)): # need to use range len idiom (bad practice) to grab next index value without using itertools
    lat1 = route[i][0]
    lon1 = route[i][1]
    lat2 = route[i + 1][0]
    lon2 = route[i + 1][1]

    difference = haversine(lon1 = lon1, lat1 = lat1, lon2 = lon2, lat2= lat2)
    routeddiffs.extend(difference)

for x, y in route:
    difference = haversine(x[1], x[0], y[1], y[0])
    routeddiffs.extend(difference)