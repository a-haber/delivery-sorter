import numpy as np
import random # for testing with random coordinates
import matplotlib.pyplot as plt # for plotting some coords

# SOME USEFUL CONSTANTS
lim = 200 # range to test within (max distance either side of origin)
num_points = 500
k = 3 # number of initial 'means'

# randomise coordinates within the given x-y range
coords = []
for i in range(num_points):
    x = random.randint(-lim, lim)
    y = random.randint(-lim, lim)
    coords.append((x,y))

# select k random points from the coordinates
# prevent against repeated means
indices = random.sample(range(0, len(coords)-1), k)
means = [coords[i] for i in indices]

def distance_between_points(a,b):
    """Distance between two coordinates, each of the form (x,y)"""
    squared_dist = (a[0]-b[0])**2 + (a[1]-b[1])**2
    return np.sqrt(squared_dist)

# find the closest mean to each point
# return array of closest means, in same order as coords
def closest_mean(point, meanlist):
    """Closest mean to a point given a list of means"""
    distances = []
    for mean in meanlist:
        distance = distance_between_points(point, mean)
        distances.append(distance)
        if distance == min(distances):
            closest_mean = mean
    return closest_mean

def group_by_means(coords_list, means_list):
    """Group list of coordinates by nearest mean
    Returns a list of lists
    [[values closest to mean 1], [mean 2 is closest], ...]"""
    grouped = [[] for j in range(k)]
    for point in coords_list:
        x = means_list.index(closest_mean(point, means_list))
        grouped[x].append(point)
    return grouped

def plot(coords_list, means_list):
    colours = ['c','m','y'] 
    cluster_colours = ['b', 'pink', 'yellow']
    plt.figure()
    # plot means
    for item in means_list:
        plt.plot(item[0], item[1], marker = 'o', markersize=5,\
        markeredgecolor = 'k', markerfacecolor=colours[means_list.index(item)])
    # plot coordinates, marking those which are means differently
    for item in coords_list:
        x = means_list.index(closest_mean(item, means_list))
        if item in means_list:
            plt.plot(item[0], item[1], marker='o', markersize=20,\
            markeredgecolor='k', markerfacecolor=colours[x])
        else:
            x = means_list.index(closest_mean(item, means_list))
            plt.plot(item[0], item[1], marker='o', markersize=10,\
            markeredgecolor='none', markerfacecolor=cluster_colours[x])
    plt.grid()
    plt.axis('square')
    plt.show()
plot(coords, means)

def centroid(arr):
    """Centroid of an array (list) of points"""
    length = len(arr)
    sum_x, sum_y = np.sum(arr, axis=0)
    return sum_x/length, sum_y/length

def iterate(n, start_means):
    """Iterate  to a depth of n, plotting each time
    Break the loop if there is no change in groupings"""
    grouped = group_by_means(coords, start_means)
    if n == 0: # finished iterating
        print("Iteration finished to full depth")
        return grouped
    else:
        new_means = []
        for i in range(k):
            new_means.append(centroid(grouped[i]))
        plot(coords, new_means)
        plt.show()
        if grouped == group_by_means(coords, new_means): # previous grouping same as next grouping
            print("Iteration finished converging, no new changes")
            return grouped
        else:
            iterate(n-1, new_means)

iterate(20, means)