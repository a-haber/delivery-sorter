import pandas as pd

class Deliverable:
    """This class represents an address to deliver to"""

    def __init__(self, id, house_no, street, town, postcode,
                 latitude, longitude, deliverer=False):

        self.id = id
        self.house_no = house_no
        self.street = street
        self.town = town
        self.postcode = postcode
        self.latitude = latitude
        self.longitude = longitude
        self.coordinates = (latitude, longitude)
        
        if deliverer: # if deliverer == True
            self.status = "Deliverer"
        else:
            self.status = "Normal"
        self.deliverer = deliverer # ie. True or False
        
    def __repr__(self):
        d = "\nID:              {}\n".format(self.id)
        d += "house number:    {}\n".format(self.house_no)
        d += "street:          {}\n".format(self.street)
        d += "town:            {}\n".format(self.town)
        d += "postcode:        {}\n".format(self.postcode)
        d += "status:          {}\n".format(self.status)
        return d

def split_address(address):
    """Split a full address string into (house number), street, town, postcode
    NB - ASSUMES street, town, postcode SEPARATED WITH COMMAS!"""
    intermediate = address
    # If the address starts with a house number, extract that information
    # !!THIS DOES NOT WORK IF THE HOUSE NUMBER HAS A LETTER eg. 17A, 5B etc!!
    i = 1
    while address[0:i].isnumeric():
        i += 1
    if i == 1:
        house_no = None
    else:
        house_no = address[0:i-1]
        intermediate = address[i-1:]
    
    # Use commas to separate rest of address into [st, town, postcode]
    details = []
    i = 0
    for j in range(len(intermediate)):
        if intermediate[j] == ",":
            details.append(intermediate[i:j])
            i = j+1
    details.append(intermediate[i:])
    
    # Remove any leading spaces
    test = [x[1:] if x[0]==" " else x for x in details]
    st, town, postcode = test[0], test[1], test[2]
    
    return house_no, st, town, postcode


def build_data_list():
    """Create a list of Deliverable objects from an excel spreadsheet of data"""
    # read excel spreadsheet into pandas df dataframe - change address location as needed
    df = pd.read_excel (r'..\database.xlsx')

    # initialise list
    items = []
    for i in range(len(df)):
        id = df.at[i, "ID"]
        latitude = df.at[i, "Latitude"]
        longitude = df.at[i, "Longitude"]
        # get address, then split into components
        address = str(df.at[i, "Address"])
        house_no, street, town, postcode = split_address(address)
        # check if the address corresponds to a deliverer
        if pd.isnull(df.at[i, "Deliverer?"]):
            # if Deliverer? value is empty then the address is not a deliverer
            d = Deliverable(id, house_no, street, town, postcode, latitude, longitude)
        else:
            d = Deliverable(id, house_no, street, town, postcode, latitude, longitude, deliverer=True)
        items.append(d)
    return items