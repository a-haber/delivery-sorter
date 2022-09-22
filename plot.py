from data import *
from distance import *
import matplotlib.pyplot as plt

# get (lon,lat) coords of addresses in database xlsx
# sourced from google sheets extension Geocode by Awesome Table
datalist = build_data_list()
coords = [item.coordinates for item in datalist]
deliverer_coords = [item.coordinates for item in datalist if item.deliverer]

k = len(deliverer_coords) # number of groups to form
means = deliverer_coords

def plot(coords_list, means_list):
    """Plot all coordinates in coloured groups, with corresponding means also plotted"""
    # colours for each group
    colours = ['c','m','y','g','r','slategrey','orangered', 'lavender'] 
    cluster_colours = ['b','pink','yellow','darkgreen','firebrick','silver','coral', 'lightsteelblue']
    
    # make sure list of colours is as long as the number of groups there are
    x = int(k / len(colours)) + 1
    colours *= x
    cluster_colours *= x
    
    # set up pyplot figure
    plt.figure()

    # plot means
    for item in means_list:
        plt.plot(item[0], item[1], marker = 'o', markersize=5,\
        markeredgecolor = 'k', markerfacecolor=colours[means_list.index(item)])
    
    # plot coordinates, marking those which are deliverers differently
    for item in coords_list:
        if item in deliverer_coords:
            x = deliverer_coords.index(item)
            plt.plot(item[0], item[1], marker='o', markersize=20,\
            markeredgecolor='k', markerfacecolor=colours[x])
        else:
            x = means_list.index(closest_mean(item, means_list))
            plt.plot(item[0], item[1], marker='o', markersize=10,\
            markeredgecolor='none', markerfacecolor=cluster_colours[x])
    plt.grid()
    plt.axis('square')
    plt.show()

def iterate(n, start_means, showplot=False):
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
        
        if showplot:
            plot(coords, new_means)
            plt.show()
        
        if grouped == group_by_means(coords, new_means): # previous grouping same as next grouping
            print("Iteration finished converging, no new changes")
            return grouped
        else:
            return iterate(n-1, new_means, showplot=showplot)


def create_groups():
    """Use iterative process to sort all items into groups"""
    result = iterate(25, means)
    # create groups
    groups = [[] for i in range(k)] # k is number of deliverers=number of groups
    for point in datalist:
        for i in range(k):
            if point.coordinates in result[i]:
                groups[i].append(point)
                break

    # if deliverer has changed group, move them back to their original group
    for subgroup in groups:
        for item in subgroup:
            if item.deliverer:
                x = deliverer_coords.index(item.coordinates) # 'original' group
                y = groups.index(subgroup) # group after iterating
                if x != y:
                    subgroup.remove(item) # remove from 'wrong' group
                    groups[x].append(item) # add back to original group
    return groups
    
def run():
    print("Plotting original scheme...")
    plot(coords, means)
    print("Iterating...")
    iterate(25, means, showplot=True) # set showplot=True to show plotting at each step
    
if __name__ == "__main__":
    run()