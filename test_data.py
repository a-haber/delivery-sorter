"""Test for data.py module"""

from data import *

def test_create_Deliverable_object():
    # create an object
    id = "test_id001"
    house_no = None
    street = "Street Ave"
    town = "City Name"
    postcode = "AA1 1AA"
    latitude, longitude = 50.00001, -0.15001
    d = Deliverable(id, house_no, street, town, postcode, latitude, longitude)

    assert d.id == id
    assert d.house_no == None
    assert d.street == street
    assert d.town == town
    assert d.postcode == postcode
    assert d.deliverer == False
    assert d.status == "Normal"
    assert d.coordinates == (latitude, longitude)

def test_split_address():
    # create test addresses
    addresses = ["55 Avenue Lane, London, TQ4 4AA", "4Street St., london, AB30ff",
    "177 My Place, Newcastle,TY55 9PP", "Harrington Drive,Petergrad,0192AA"]
    assert split_address(addresses[0]) == ('55', 'Avenue Lane', 'London', 'TQ4 4AA')
    assert split_address(addresses[1])[0] == '4'
    assert len(split_address(addresses[2])) == 4
    assert split_address(addresses[3])[0] == None

def test_build_data_list():
    datalist = build_data_list()
    assert len(datalist) > 0
    assert type(datalist) == list
    assert type(datalist[0]) == Deliverable
