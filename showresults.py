import pandas as pd
import matplotlib.pyplot as plt

from data import navigate_directory
navigate_directory() # navigate to folder in order to read files


def plot(groups):
    """Show points on a map - first scattered, then grouped"""

    # ungrouped first
    df = pd.read_excel(r'.\exampledatabase.xlsx')
    BBox = (df.Longitude.min(), df.Longitude.max(), df.Latitude.min(), df.Latitude.max())

    background = plt.imread(r'.\map.png')

    fig, ax = plt.subplots()
    ax.scatter(df.Longitude, df.Latitude, zorder=1, c='b', s=10)

    ax.set_xlim(BBox[0],BBox[1])
    ax.set_ylim(BBox[2],BBox[3])

    ax.imshow(background, zorder=0, extent=BBox, aspect=1.8)
    plt.show()

    # then grouped

    # colours for each group
    colours = ['c','m','y','g','r','slategrey','orangered', 'lavender', 'b','pink','yellow','darkgreen','firebrick','silver','coral', 'lightsteelblue']
    x = int(len(groups) / len(colours)) + 1
    colours *= x
    
    # set up pyplot figure
    plt.figure()
    
    # plot background
    background = plt.imread(r'.\map.png')
    plt.imshow(background, extent=BBox, zorder=0, aspect=1.6)

    # plot coordinates, marking those which are deliverers differently
    for group in groups:
        x = groups.index(group)
        for item in group:
            if item.deliverer:
                edge = 'gainsboro'
            else:
                edge = 'k'
            plt.plot(item.longitude, item.latitude, marker='o', markersize=12,\
                markeredgecolor=edge, markerfacecolor=colours[x])
    plt.grid()
    plt.show()

from analysis import groups
plot(groups)
