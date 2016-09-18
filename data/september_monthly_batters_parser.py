import json
import lxml
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

STAT_COUNT = 14

players = [
    {
        "name": "Ben Revere",
        "id": 519184,
        "pitches": []
    },
    {
        "name": "Josh Donaldson",
        "id": 518626,
        "pitches": []
    },
    {
        "name": "Jose Bautista",
        "id": 430832,
        "pitches": []
    },
    {
        "name": "Edwin Encarnacion",
        "id": 429665,
        "pitches": []
    },
    {
        "name": "Troy Tulowitzki",
        "id": 453064,
        "pitches": []
    },
    {
        "name": "Justin Smoak",
        "id": 475253,
        "pitches": []
    },
    {
        "name": "Russell Martin",
        "id": 431145,
        "pitches": []
    },
    {
        "name": "Ryan Goins",
        "id": 572365,
        "pitches": []
    },
    {
        "name": "Kevin Pillar",
        "id": 607680,
        "pitches": []
    }
]

for player in players:

    month_url = "http://www.brooksbaseball.net/h_tabs.php?player={}&balls=-1&strikes=-1&b_hand=-1&time=month&minmax=ci&var=ra&s_type=16&gFilt=allmlb&startDate=09/01/2015&endDate=10/01/2015".format(player["id"])

    data = urlopen(month_url)
    soup = BeautifulSoup(data, "lxml")
    data = soup.find("table")

    # # This is the name of the all the stats we are trying to get
    stats_names = data.findAll("th")

    # Essentially the table data in array form of HTML elements
    stats = data.findAll("td")

    for stat in range(0, len(stats)):
        stats[stat] = re.sub("<.*?>", "", str(stats[stat]))

    for stat in range(0, len(stats), STAT_COUNT):
        player["pitches"].append(stats[stat:stat+STAT_COUNT])

def obj_dict(obj):
    return obj.__dict__

with open("september_monthly_batters.json", "w") as outputfile:
    json.dump(players, outputfile, default=obj_dict)
