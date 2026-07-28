import json

# Defining a Driver class
class Driver:
    def __init__(self, name, talent, longevity, aggression, moxie, humour, scrupulousness):
        self.name = name
        self.talent = talent
        self.longevity = longevity
        self.aggression = aggression
        self.moxie = moxie
        self.humour = humour
        self.scrupulousness = scrupulousness

# Loading individual drivers from drivers.json
def load_drivers(filepath):
    with open(filepath, "r") as f:                  #Reads the .json file
        raw_data = json.load(f)

    drivers = []
    for entry in raw_data:                          #Iterates over entries in .json and appends to drivers list
        drivers.append(Driver(**entry))

    return drivers                                  #Use this to load all drivers e.g. all_drivers = load_drivers("drivers.json")
