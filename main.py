import math
import os


def distance(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon2 = math.radians(lon2)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # apply the Haversine formula to calc distance
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = 6371 * c # 6371 = earths radius
    return distance

# function for finding the nearest neighbor to a given point (lat,lon)
def nearest_neighbor(lat, lon, points):
    min_distance = float('inf')
    nearest_neighbor = None
    for point in points:
        d = distance(lat, lon, point[0], point[1])
        if d < min_distance:
            min_distance = d
            nearest_neighbor = point
    return nearest_neighbor



# list of points (tracks)

points = [
    ( 26.0347,   50.5089   ), #Bahrain
    ( 21.6334,   39.1035   ), #Saudi
    ( -37.8490,  144.9680  ), #Australia
    ( 40.4083,   49.8622   ), #Azerbaijan
    ( 25.9566,   -80.2310  ), #Miami
    ( 44.3447,   11.7155   ), #Imola
    ( 43.7347,   7.4197    ), # Monaco
    ( 41.5728,   2.2661    ), # Spain
    ( 45.5079,   -73.5290  ), # Canada
    ( 47.2183,   14.7606   ), #Austria
    ( 52.0786,   -1.0169   ), # Great Britain
    ( 47.5106,   -19.2556  ), #Hungary
    ( 50.4373,   5.9750    ), #Belgium
    ( 52.3744,   4.5397    ), #Netherlands
    ( 45.6237,   9.2844    ), #Monza
    ( 1.2931,    103.8550  ), #Singapore
    ( 34.8414,   136.5460  ), #Japan
    ( 25.4861,   51.4523   ), #Qatar
    ( 30.1375,   -97.6400  ), #COTA
    ( 19.4052,   -99.0930  ), #Mexico
    ( -23.7010,  -46.6980  ), #Brazil
    ( 36.1068,   -115.1600 ), #Las Vegas
    ( 24.4749,   54.6038   ), #Abu Dhabi
]

#uses the nearest neighbor algorithm to find the shortest path between points
total_distance = 0
current_point = points[0]
path = [current_point]
points.remove(current_point)
while len(points) > 0:
    next_point = nearest_neighbor(current_point[0], current_point[1], points)
    path.append(next_point)
    points.remove(next_point)
    total_distance += distance(current_point[0], current_point[1], next_point[0], next_point[1])
    current_point = next_point

# print the order of the points in path
print("order of points:")
for point in path:
    print(point)

#print total distance
print("Total Distance: %.2f kilometers" % total_distance)
