import numpy as np
from haversine import haversine

def distance_calc(a, b, Cartesian=False):
    """Input two coordinates, each of the form (latitude, longitude) <- default
    or Cartesian coordinates (x, y)
    Output: distance in [m]"""
    if Cartesian:
        squared_dist = (a[0]-b[0])**2 + (a[1]-b[1])**2
        return np.sqrt(squared_dist)
    else:
        return 1000*haversine(a,b)

def closest_mean(point, meanlist):
    """Closest 'mean' to a point given a list of 'means' (points)"""
    distances = []
    for mean in meanlist:
        distance = distance_calc(point, mean)
        distances.append(distance)
        if distance == min(distances):
            closest_mean = mean
    return closest_mean

def group_by_means(coords_list, means_list):
    """Group list of coordinates by nearest mean to each coordinate
    Returns a list of lists
    [[mean 1 is closest], [mean 2 is closest], ...]"""
    k = len(means_list)
    grouped = [[] for j in range(k)]
    for point in coords_list:
        x = means_list.index(closest_mean(point, means_list))
        grouped[x].append(point)
    return grouped

def centroid(arr):
    """Centroid of an array (list) of points"""
    length = len(arr)
    sum_x, sum_y = np.sum(arr, axis=0)
    return sum_x/length, sum_y/length

"""Note that the above centroid() function calculates the centroid of 
Cartesian coordinates ie. those on a flat plane. Therefore it is not necessarily accurate
for (lat,lon) coordinates, but can still be used as an approximation - this will be better when
the coordinates are close together, which they are in the intended use case.
The below function was then created to get a more realistic estimate of centroids.
On testing for the sort of data this application is designed for, the two functions are
equivalent up to 5 decimal places, which corresponds to ~1m of error - completely acceptable for
this use case"""

def lat_lon_centroid(arr):
    """Centroid of an array of (lat,lon) coordinates
    assuming spherical geometry of earth"""
    # convert lat/lon to Cartesian coordinates for each location.
    X, Y, Z = 0, 0, 0
    for coord in arr:
        # convert to radians
        lat = coord[0]*np.pi/180
        lon = coord[1]*np.pi/180
        X += np.cos(lat) * np.cos(lon)
        Y += np.cos(lat) * np.sin(lon)
        Z += np.sin(lat)
    
    # Compute average x, y and z coordinates.
    n = len(arr)
    X /= n
    Y /= n
    Z /= n

    # Convert average x, y, z coordinate back to latitude and longitude.
    # then convert back to degrees
    Lon = np.arctan2(Y, X) * 180/np.pi
    Hyp = np.sqrt(X*X + Y*Y)
    Lat = np.arctan2(Z, Hyp) * 180/np.pi

    return Lat, Lon

