from data import *
from distance import *
import matplotlib.pyplot as plt

# get (lon,lat) coords of addresses in database.xlsx
# sourced from google sheets extension Geocode by Awesome Table
datalist = build_data_list()
coords = [item.coordinates for item in datalist]
deliverer_coords = [item.coordinates for item in datalist if item.deliverer]

k = len(deliverer_coords) # number of groups to form
means = deliverer_coords

def plot(coords_list, means_list):
    """Plot all coordinates in coloured groups, with corresponding means also plotted"""
    # colours for each group
    colours = ['c','m','y','g','r','slategrey','orangered'] 
    cluster_colours = ['b','pink','yellow','darkgreen','firebrick','silver','coral']
    
    # set up pyplot figure
    plt.figure()

    # plot means
    for item in means_list:
        plt.plot(item[0], item[1], marker = 'o', markersize=5,\
        markeredgecolor = 'k', markerfacecolor=colours[means_list.index(item)])
    
    # plot coordinates, marking those which are deliverers differently
    for item in coords_list:
        x = means_list.index(closest_mean(item, means_list))
        if item in deliverer_coords:
            plt.plot(item[0], item[1], marker='o', markersize=20,\
            markeredgecolor='k', markerfacecolor=colours[x])
        else:
            x = means_list.index(closest_mean(item, means_list))
            plt.plot(item[0], item[1], marker='o', markersize=10,\
            markeredgecolor='none', markerfacecolor=cluster_colours[x])
    plt.grid()
    plt.axis('square')
    plt.show()

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

def run():
    plot(coords, means)
    iterate(20, means)

run()