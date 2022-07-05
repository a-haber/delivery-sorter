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