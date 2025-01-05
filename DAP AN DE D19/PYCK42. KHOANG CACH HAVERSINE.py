from math import *
long1, lat1 = map(float, input().split())
long2, lat2 = map(float, input().split())
delLat = lat2 - lat1
delLong = long2 - long1
a = sin(delLat / 2) ** 2 + cos(lat1) * cos(lat2) * (sin(delLong / 2) ** 2)
c = 2 * asin(sqrt(a))
R = 6371.0
d = R * c
print(f"{d:.2f}")
