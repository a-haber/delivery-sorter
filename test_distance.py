"""Test for distance.py module"""

from distance import *

def test_distance_calc():
    # set up (lat, long) coords
    a = (50.0657, 5.7132)
    b = (58.6373, 3.0689)
    distance1 = distance_calc(a,b)
    assert abs(968000-distance1) < 1000 #distance ~ 968km to nearest km

    # set up (x,y) coords
    p = (6,-4)
    q = (3, 0)
    assert distance_calc(p,q,Cartesian=True) == 5.0

def test_closest_mean():
    test_pt = (50.0657, 5.7132)
    test_means = [(30.1857, 5.7132), (50.0661, 5.6527), (78.7264, -0.3213)]
    assert closest_mean(test_pt, test_means) == (50.0661, 5.6527)

def test_group_by_means():
    coords = [(1.0,1.0),(2.0,2.0),(49.3,30.2),(1.0,-0.5),(50.1,4.1),(49.7,17.8)]
    means = [(0.5,1.5),(50.0,25.0)]
    grouped = group_by_means(coords, means)
    assert len(grouped) == len(means)
    assert type(grouped) == list
    assert type(grouped[0]) == list
    assert type(grouped[0][0]) == tuple

def test_centroid():
    array = [(0.,0.),(5.0,10.0),(10.0,5.0)]
    assert centroid(array) == (5.0,5.0)

def test_lat_lon_centroid():
    array1 = [(0.,0.),(5.0,10.0),(10.0,5.0)]
    centre = lat_lon_centroid(array1)
    # ensure resulting centroid is approximately (5.0,5.0)
    for coord in centre:
        assert abs (coord-5.0) < 0.1
    array2 = [(0.11028,0.27366),(5.048299,10.016623),(10.016266,5.00539),\
        (40.939377,35.12711),(53.949127,-4.51358)]
    lat,lon = lat_lon_centroid(array2)
    assert round(lat,6) == 22.276843
    assert round(lon,6) == 8.897985