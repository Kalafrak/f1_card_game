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

    #__str__ method allows us to call e.g. print(player_card) and automatically inherit this formatting
    def __str__(self):
        return f"{'=' * 21}\n|{self.name:^19}|\n| {'Talent:':<16}{self.talent} |\n| {'Longevity:':<16}{self.longevity} |\n| {'Aggression:':<16}{self.aggression} |\n| {'Moxie:':<16}{self.moxie} |\n| {'Humour:':<16}{self.humour} |\n| {'Scrupulousness:':<16}{self.scrupulousness} |\n{'=' * 21}"

# Loading individual drivers from drivers.json
def load_drivers(filepath):
    with open(filepath, "r") as f:                  #Reads the .json file
        raw_data = json.load(f)

    drivers = []
    for entry in raw_data:                          #Iterates over entries in .json and appends to drivers list
        drivers.append(Driver(**entry))

    return drivers                                  #Use this to load all drivers e.g. all_drivers = load_drivers("drivers.json")
